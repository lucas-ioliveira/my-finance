from django.views import View
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.db.models import Sum

from datetime import datetime, timedelta

from wallet.models import Revenue, Expense, Investments
from dashboard.utils import Dashboard

@method_decorator(login_required, name='dispatch')
class DashboardView(View):
    def get(self, request):
        data_limite = datetime.now() - timedelta(days=30)

        revenues_total = Revenue.objects.filter(
            user=request.user, active=True, status='Pago', payment_date__gte=data_limite
        ).aggregate(total_revenues=Sum('amount'))['total_revenues'] or 0

        expense_total = Expense.objects.filter(
            user=request.user, active=True, due_date__gte=data_limite
        ).aggregate(total_expenses=Sum('amount'))['total_expenses'] or 0

        investments_total = Investments.objects.filter(
            user=request.user, active=True, status='Realizado', investment_date__gte=data_limite
        ).aggregate(total_investments=Sum('amount'))['total_investments'] or 0

        balance = revenues_total - expense_total - investments_total

        recent_transactions = Dashboard.get_crud_events(request.user)

        exchange_rates = Dashboard.get_exchange_rates()

        context = {
            'revenues_total': revenues_total,
            'expense_total': expense_total,
            'investments_total': investments_total,
            'balance': balance,
            'recent_transactions': recent_transactions,
            'exchange_rates': exchange_rates,
        }
        return render(request, 'dashboard.html', context)

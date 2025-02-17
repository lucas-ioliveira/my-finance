from django.views import View
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.db.models import Sum

from datetime import datetime
import calendar

from wallet.models import Revenue, Expense, Investments
from dashboard.utils import Dashboard

@method_decorator(login_required, name='dispatch')
class DashboardView(View):
    def get(self, request):
        today = datetime.now().date()
        
        # Obtendo o primeiro e último dia do mês corretamente
        first_day = today.replace(day=1)
        last_day = today.replace(day=calendar.monthrange(today.year, today.month)[1])

        revenues_total = Revenue.objects.filter(
            user=request.user, active=True, status='Pago',
            payment_date__gte=first_day, payment_date__lte=last_day
        ).aggregate(total_revenues=Sum('amount'))['total_revenues'] or 0

        expense_total = Expense.objects.filter(
            user=request.user, active=True,
            due_date__gte=first_day, due_date__lte=last_day
        ).aggregate(total_expenses=Sum('amount'))['total_expenses'] or 0

        investments_total = Investments.objects.filter(
            user=request.user, active=True, status='Realizado',
            investment_date__gte=first_day, investment_date__lte=last_day
        ).aggregate(total_investments=Sum('amount'))['total_investments'] or 0

        date_filter = request.GET.get('date_filter')
        if date_filter:
            initial_date = request.GET.get('initial_date')
            final_date = request.GET.get('final_date')

            revenues_total = Revenue.objects.filter(
                user=request.user, active=True, status='Pago',
                payment_date__gte=initial_date, payment_date__lte=final_date
            ).aggregate(total_revenues=Sum('amount'))['total_revenues'] or 0

            expense_total = Expense.objects.filter(
                user=request.user, active=True,
                due_date__gte=initial_date, due_date__lte=final_date
            ).aggregate(total_expenses=Sum('amount'))['total_expenses'] or 0

            investments_total = Investments.objects.filter(
                user=request.user, active=True, status='Realizado',
                investment_date__gte=initial_date, investment_date__lte=final_date
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

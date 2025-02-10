from django.views import View
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.db.models import Sum

from datetime import datetime, timedelta

from wallet.models import Revenue, Expense, Investments

@method_decorator(login_required, name='dispatch')
class DashboardView(View):
    def get(self, request):
        data_limite = datetime.now() - timedelta(days=30)

        revenues_total = Revenue.objects.filter(user=request.user, active=True, status='Pago', payment_date__gte=data_limite).aggregate(total_revenues=Sum('amount'))
        expense_total = Expense.objects.filter(user=request.user, active=True, due_date__gte=data_limite).aggregate(total_expenses=Sum('amount'))
        investments_total = Investments.objects.filter(user=request.user, active=True, status='Realizado' , investment_date__gte=data_limite).aggregate(total_investments=Sum('amount'))

        context = {
            'revenues_total': revenues_total['total_revenues'],
            'expense_total': expense_total['total_expenses'],
            'investments_total': investments_total['total_investments'],
        }
        
        return render(request, 'dashboard.html', context)

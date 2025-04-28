from django.views import View
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from dashboard.services.service import DashboardService
from dashboard.repositories.repository import DashboardRepository


@method_decorator(login_required, name='dispatch')
class DashboardView(View):
    def get(self, request):
        data = DashboardService.get_balance(request)

        recent_transactions = DashboardRepository.get_crud_events(request.user)
        exchange_rates = DashboardService.get_exchange_rates()

        context = {
            'revenues_total': data.get('revenues_total'),
            'expense_total': data.get('expense_total'),
            'investments_total': data.get('investments_total'),
            'balance': data.get('balance'),
            'recent_transactions': recent_transactions,
            'exchange_rates': exchange_rates,
        }
        return render(request, 'dashboard/dashboard.html', context)

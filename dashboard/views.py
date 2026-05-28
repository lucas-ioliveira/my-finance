import json

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

        rev_total = float(data.get('revenues_total') or 0)
        exp_total = float(data.get('expense_total') or 0)
        inv_total = float(data.get('investments_total') or 0)

        context = {
            'revenues_total': data.get('revenues_total'),
            'expense_total': data.get('expense_total'),
            'investments_total': data.get('investments_total'),
            'balance': data.get('balance'),

            # Dados do Gráfico de Pizza
            'pie_labels': json.dumps(['Receitas', 'Despesas', 'Investimentos']),
            'pie_data': json.dumps([rev_total, exp_total, inv_total]),
            
            # Dados do Gráfico de Barras (Despesas por Categoria vindos do Service)
            'bar_labels': json.dumps(data.get('bar_labels', [])),
            'bar_data': json.dumps(data.get('bar_data', [])),
        }
        return render(request, 'dashboard/dashboard.html', context)

import calendar
import requests
from datetime import datetime

from wallet.repositories.expense.repository import ExpenseRepository
from wallet.repositories.investments.repository import InvestmentsRepository
from wallet.repositories.revanue.repository import RevenueRepository


class DashboardService:

    @staticmethod
    def get_balance(request):
        today = datetime.now().date()

        # Obtendo o primeiro e último dia do mês corretamente
        first_day = today.replace(day=1)
        last_day = today.replace(day=calendar.monthrange(today.year, today.month)[1])

        expense_total = ExpenseRepository.get_total_value(request.user, first_day, last_day)
        investments_total = InvestmentsRepository.get_total_value(request.user, first_day, last_day)
        revenues_total = RevenueRepository.get_total_value(request.user, first_day, last_day)

        date_filter = request.GET.get('date_filter')
        if date_filter:
            initial_date = request.GET.get('initial_date')
            final_date = request.GET.get('final_date')

            expense_total = ExpenseRepository.get_total_value(request.user, initial_date, final_date)
            investments_total = InvestmentsRepository.get_total_value(request.user, initial_date, final_date)
            revenues_total = RevenueRepository.get_total_value(request.user, initial_date, final_date)

        balance = revenues_total - expense_total - investments_total

        data = {
            'balance': balance,
            'expense_total': expense_total,
            'investments_total': investments_total,
            'revenues_total': revenues_total,
        }

        return data

    @staticmethod
    def get_exchange_rates():
        coin_list = []

        url = 'https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL'

        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            data = response.json()
            for key, value in data.items():
                coin_list.append(value)

            return coin_list
        else:
            raise Exception(f"Erro externo: {response.status_code} - {response.text}")

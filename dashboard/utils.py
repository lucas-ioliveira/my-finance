from wallet.models import Revenue, Expense, Investments
from easyaudit.models import CRUDEvent
import requests


class Dashboard:

    @staticmethod
    def get_recent_transactions():
        revenue = Revenue.objects.all().order_by('-created_at')[:5]
        expense = Expense.objects.all().order_by('-created_at')[:5]
        investments = Investments.objects.all().order_by('-created_at')[:5]
        combined = list(revenue) + list(expense) + list(investments)

        return sorted(combined, key=lambda x: x.created_at, reverse=True)

    @staticmethod
    def get_crud_events(user):
        create = CRUDEvent.objects.filter(user=user, event_type=CRUDEvent.CREATE).order_by('-datetime')[:5]
        update = CRUDEvent.objects.filter(user=user, event_type=CRUDEvent.UPDATE).order_by('-datetime')[:5]
        delete = CRUDEvent.objects.filter(user=user, event_type=CRUDEvent.DELETE).order_by('-datetime')[:5]
        combined = list(create) + list(update) + list(delete)

        return sorted(combined, key=lambda x: x.datetime, reverse=True)[:3]

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

from django.shortcuts import get_object_or_404
from django.db.models import Sum

from wallet.models import Investments


class InvestmentsRepository:

    @staticmethod
    def get_all(user):
        return Investments.objects.filter(user=user, active=True)

    @staticmethod
    def get_all_by_search(user, search):
        return Investments.objects.filter(user=user, active=True, description__icontains=search)

    @staticmethod
    def get_all_status():
        return Investments.STATUS_CHOICES

    @staticmethod
    def get_by_investment_date(initial_date, final_date, user):
        return Investments.objects.filter(investment_date__range=[initial_date, final_date], user=user)

    @staticmethod
    def create(user, description, notes, amount, category, investment_date, investment_method, receipt):
        investment = Investments(
            user=user, description=description, notes=notes, amount=amount, category_id=category,
            investment_date=investment_date, investment_method=investment_method, receipt=receipt
        )
        investment.save()

    @staticmethod
    def update(investments_id, description, notes, amount, category, investment_date, due_date, investment_method, receipt, status):
        investments = get_object_or_404(Investments, id=investments_id)
        investments.description = description
        investments.notes = notes
        investments.amount = amount
        investments.category_id = category
        investments.investment_date = investment_date
        investments.due_date = due_date
        investments.investment_method = investment_method
        investments.receipt = receipt
        investments.status = status
        investments.save()

    @staticmethod
    def delete(investments_id, active):
        category = get_object_or_404(Investments, id=investments_id)
        category.active = active
        category.save()

    @staticmethod
    def clone(investments_id):
        investments = get_object_or_404(Investments, id=investments_id)
        investments.pk = None
        investments.save()

    @staticmethod
    def get_total_value(user, first_day, last_day):
        return Investments.objects.filter(
            user=user, active=True, status='Realizado',
            investment_date__gte=first_day, investment_date__lte=last_day
        ).aggregate(total_investments=Sum('amount'))['total_investments'] or 0

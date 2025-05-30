from django.shortcuts import get_object_or_404
from django.db.models import Sum

from wallet.models import Revenue


class RevenueRepository:
    @staticmethod
    def get_all(user):
        return Revenue.objects.filter(user=user, active=True)

    @staticmethod
    def get_all_by_search(user, search):
        return Revenue.objects.filter(user=user, active=True, description__icontains=search)

    @staticmethod
    def get_all_status():
        return Revenue.STATUS_CHOICES

    @staticmethod
    def get_by_payment_date(initial_date, final_date, user):
        return Revenue.objects.filter(payment_date__range=[initial_date, final_date], user=user)

    @staticmethod
    def create(user, description, notes, amount, category, payment_date, payment_method, receipt):

        revenue = Revenue(
            user=user, description=description, notes=notes, amount=amount, category_id=category,
            payment_date=payment_date, payment_method=payment_method, receipt=receipt
        )
        revenue.save()

    @staticmethod
    def update(revenue_id, description, notes, amount, category, payment_date, payment_method, receipt, status):
        revenue = get_object_or_404(Revenue, id=revenue_id)
        revenue.description = description
        revenue.notes = notes
        revenue.amount = amount
        revenue.category_id = category
        revenue.payment_date = payment_date
        revenue.payment_method = payment_method
        revenue.receipt = receipt
        revenue.status = status
        revenue.save()

    @staticmethod
    def delete(revenue_id, active):
        revenue = get_object_or_404(Revenue, id=revenue_id)
        revenue.active = active
        revenue.save()

    @staticmethod
    def clone(revenue_id):
        revenue = get_object_or_404(Revenue, id=revenue_id)
        revenue.pk = None
        revenue.save()

    @staticmethod
    def get_total_value(user, first_day, last_day):
        return Revenue.objects.filter(
            user=user, active=True, status='Pago',
            payment_date__gte=first_day, payment_date__lte=last_day
        ).aggregate(total_revenues=Sum('amount'))['total_revenues'] or 0

    @staticmethod
    def get_by_filters_for_the_report(**filters):
        return Revenue.objects.filter(**filters)

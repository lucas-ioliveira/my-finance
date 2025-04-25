from django.shortcuts import get_object_or_404
from django.db.models import Q

from dateutil.relativedelta import relativedelta

from wallet.models import Expense


class ExpenseRepository:
    @staticmethod
    def get_all(user):
        return Expense.objects.filter(user=user, active=True)

    @staticmethod
    def get_all_by_search(user, search):
        return Expense.objects.filter(user=user, active=True, description__icontains=search)

    @staticmethod
    def get_all_status():
        return Expense.STATUS_CHOICES

    @staticmethod
    def get_by_filters(filter_type, initial_date, final_date, user):
        if filter_type == 'payment_date' and initial_date and final_date:
            expense = Expense.objects.filter(payment_date__range=[initial_date, final_date], user=user)
        elif filter_type == 'due_date' and initial_date and final_date:
            expense = Expense.objects.filter(due_date__range=[initial_date, final_date], user=user)
        elif filter_type == 'todos' and initial_date and final_date:
            expense = Expense.objects.filter(
                Q(payment_date__range=(initial_date, final_date))
                | Q(due_date__range=(initial_date, final_date)),
                user=user
            )

        return expense

    @staticmethod
    def create(user, description, notes, amount, category_id, due_date, payment_date, payment_method, receipt, repeat):

        for i in range(repeat):
            expense = Expense(
                user=user,
                description=description,
                notes=notes,
                amount=amount,
                category_id=category_id,
                due_date=due_date,
                payment_date=payment_date,
                payment_method=payment_method,
                receipt=receipt
            )
            expense.save()
            due_date += relativedelta(months=1)

    @staticmethod
    def update(expense_id, description, notes, amount, category, payment_date, due_date, payment_method, receipt, status):
        expense = get_object_or_404(Expense, id=expense_id)
        expense.description = description
        expense.notes = notes
        expense.amount = amount
        expense.category_id = category
        expense.payment_date = payment_date
        expense.due_date = due_date
        expense.payment_method = payment_method
        expense.receipt = receipt
        expense.status = status
        expense.save()

    @staticmethod
    def delete(expense_id, active):
        expense = get_object_or_404(Expense, id=expense_id)
        expense.active = active
        expense.save()

    @staticmethod
    def clone(expense_id):
        expense = get_object_or_404(Expense, id=expense_id)
        expense.pk = None
        expense.save()

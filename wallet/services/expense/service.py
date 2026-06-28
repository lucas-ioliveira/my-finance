from django.core.paginator import Paginator
from django.http import FileResponse, HttpResponse

from datetime import datetime

from wallet.repositories.expense.repository import ExpenseRepository


class ExpenseService:

    @staticmethod
    def get_all(request):
        user = request.user
        search = request.GET.get('search')
        date_filter = request.GET.get('date_filter')
        page = request.GET.get('page')
        expense = ExpenseRepository.get_all(user)

        if search:
            expense = ExpenseRepository.get_all_by_search(user, search)

        if date_filter:
            filter_type = request.GET.get('filter_type')
            initial_date = request.GET.get('initial_date')
            final_date = request.GET.get('final_date')

            if filter_type:
                expense = ExpenseRepository.get_by_filters(filter_type, initial_date, final_date, user)

        paginator = Paginator(expense, 6)
        return paginator.get_page(page)

    @staticmethod
    def create(request):
        user = request.user
        description = request.POST.get('descricao')
        notes = request.POST.get('observacao')
        category_id = request.POST.get('categoria')
        payment_method = request.POST.get('forma_pagamento')
        receipt = request.FILES.get('file')

        try:
            amount = float(request.POST.get('valor').replace(',', '.'))
        except (ValueError, AttributeError):
            raise Exception('Informe um valor válido para a despesa.')

        try:
            due_date = datetime.strptime(request.POST.get('data_vencimento'), "%Y-%m-%d").date()
        except (ValueError, TypeError):
            raise Exception('Informe uma data de vencimento válida.')

        payment_date = request.POST.get('data_pagamento')
        if payment_date:
            try:
                payment_date = datetime.strptime(payment_date, "%Y-%m-%d").date()
            except ValueError:
                raise Exception('Informe uma data de pagamento válida.')

        else:
            payment_date = None

        repeat = request.POST.get('repeat')
        try:
            repeat = int(repeat)
        except (ValueError, TypeError):
            repeat = 1

        ExpenseRepository.create(user, description, notes, amount, category_id, due_date, payment_date, payment_method, receipt, repeat)

    @staticmethod
    def update(request, expense_id):
        description = request.POST.get('descricao_edit')
        notes = request.POST.get('observacao_edit')
        valor_edit = request.POST.get('valor_edit')
        amount = float(valor_edit.replace(',', '.'))
        category = request.POST.get('categoria_edit')
        if request.POST.get('data_pagamento_edit'):
            payment_date = request.POST.get('data_pagamento_edit')
        else:
            payment_date = None
        due_date = request.POST.get('data_vencimento_edit')
        payment_method = request.POST.get('forma_pagamento_edit')
        receipt = request.POST.get('file_edit')
        status = request.POST.get('status_edit')

        ExpenseRepository.update(expense_id, description, notes, amount, category, payment_date, due_date, payment_method, receipt, status)

    @staticmethod
    def delete(expense_id):
        active = False
        ExpenseRepository.delete(expense_id, active)

    @staticmethod
    def download_receipt(request, expense_id):
        expense = ExpenseRepository.get_by_id(expense_id, request.user)

        if not expense.receipt:
            return

        file = expense.receipt.open("rb")

        return FileResponse(
            file,
            as_attachment=False,
            filename=expense.receipt.name.split("/")[-1]
        )

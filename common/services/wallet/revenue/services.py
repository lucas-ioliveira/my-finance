from django.core.paginator import Paginator

from common.repositories.wallet.revanue.repository import RevenueRepository


class RevenueService:
    @staticmethod
    def get_all(request):
        user = request.user
        search = request.GET.get('search')
        date_filter = request.GET.get('date_filter')
        page = request.GET.get('page')
        revenue = RevenueRepository.get_all(user)

        if search:
            revenue = RevenueRepository.get_all_by_search(user, search)

        if date_filter:
            filter_type = request.GET.get('filter_type')
            initial_date = request.GET.get('initial_date')
            final_date = request.GET.get('final_date')

            if filter_type == 'payment_date' and initial_date and final_date:
                revenue = RevenueRepository.get_by_payment_date(initial_date, final_date, user)

        paginator = Paginator(revenue, 6)
        return paginator.get_page(page)

    @staticmethod
    def create(request):
        user = request.user
        description = request.POST.get('descricao')
        notes = request.POST.get('observacao')
        amount = request.POST.get('valor')
        amount = float(amount.replace(',', '.'))
        category = request.POST.get('categoria')
        payment_date = request.POST.get('data_pagamento')
        payment_method = request.POST.get('forma_pagamento')
        receipt = request.FILES.get('file')

        RevenueRepository.create(user, description, notes, amount, category, payment_date, payment_method, receipt)

    @staticmethod
    def update(request, revenue_id):
        description = request.POST.get('descricao_edit')
        notes = request.POST.get('observacao_edit')
        valor_edit = request.POST.get('valor_edit')
        amount = float(valor_edit.replace(',', '.'))
        category = request.POST.get('categoria_edit')
        payment_date = request.POST.get('data_pagamento_edit')
        payment_method = request.POST.get('forma_pagamento_edit')
        receipt = request.POST.get('file_edit')
        status = request.POST.get('status_edit')

        RevenueRepository.update(revenue_id, description, notes, amount, category, payment_date, payment_method, receipt, status)

    @staticmethod
    def delete(revenue_id):
        active = False
        RevenueRepository.delete(revenue_id, active)

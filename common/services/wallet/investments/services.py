from django.core.paginator import Paginator

from common.repositories.wallet.investments.repository import InvestmentsRepository


class InvestmentsService:

    @staticmethod
    def get_all(request):
        user = request.user
        search = request.GET.get('search')
        page = request.GET.get('page')
        investments = InvestmentsRepository.get_all(user)

        if search:
            investments = InvestmentsRepository.get_all_by_search(user, search)

        date_filter = request.GET.get('date_filter')
        if date_filter:
            filter_type = request.GET.get('filter_type')
            initial_date = request.GET.get('initial_date')
            final_date = request.GET.get('final_date')

            if filter_type == 'investment_date' and initial_date and final_date:
                investments = InvestmentsRepository.get_by_investment_date(initial_date, final_date, user)

        paginator = Paginator(investments, 6)
        return paginator.get_page(page)

    @staticmethod
    def create(request):
        user = request.user
        description = request.POST.get('descricao')
        notes = request.POST.get('observacao')
        amount = request.POST.get('valor')
        amount = float(amount.replace(',', '.'))
        category = request.POST.get('categoria')

        if request.POST.get('data_investimento'):
            investment_date = request.POST.get('data_investimento')
        else:
            investment_date = None

        investment_method = request.POST.get('metodo_investimento')
        receipt = request.FILES.get('file')

        InvestmentsRepository.create(user, description, notes, amount, category, investment_date, investment_method, receipt)

    @staticmethod
    def update(request, investments_id):
        description = request.POST.get('descricao_edit')
        notes = request.POST.get('observacao_edit')
        valor_edit = request.POST.get('valor_edit')
        amount = float(valor_edit.replace(',', '.'))
        category = request.POST.get('categoria_edit')

        if request.POST.get('data_investimento_edit'):
            investment_date = request.POST.get('data_investimento_edit')
        else:
            investment_date = None

        due_date = request.POST.get('data_vencimento_edit')
        investment_method = request.POST.get('metodo_investimento_edit')
        receipt = request.POST.get('file_edit')
        status = request.POST.get('status_edit')

        InvestmentsRepository.update(investments_id, description, notes, amount, category, investment_date, due_date, investment_method, receipt, status)

    @staticmethod
    def delete(investments_id):
        active = False
        InvestmentsRepository.delete(investments_id, active)

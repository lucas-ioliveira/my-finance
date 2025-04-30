from django.views import View
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from wallet.services.category.service import CategoryService
from wallet.repositories.category.repository import CategoryRepository

from wallet.services.expense.service import ExpenseService
from wallet.repositories.expense.repository import ExpenseRepository

from wallet.services.investments.service import InvestmentsService
from wallet.repositories.investments.repository import InvestmentsRepository

from wallet.services.revenue.services import RevenueService
from wallet.repositories.revanue.repository import RevenueRepository


@method_decorator(login_required, name='dispatch')
class CategoryView(View):
    def get(self, request):
        try:
            categories = CategoryService.get_all(request)
            return render(request, 'wallet/category.html', {'categories': categories})
        except Exception:
            messages.error(request, "Erro ao listar categorias!")
            return redirect('dashboard')

    def post(self, request):
        try:
            CategoryService.create(request)
            messages.success(request, "Categoria cadastrada com sucesso!")
            return redirect('category')
        except Exception:
            messages.error(request, "Erro ao cadastrar categoria!")
            return redirect('category')


@method_decorator(login_required, name='dispatch')
class CategoryEditView(View):
    def post(self, request, category_id):
        try:
            CategoryService.update(request, category_id)
            messages.success(request, "Categoria atualizada com sucesso!")
            return redirect('category')
        except Exception:
            messages.error(request, "Erro ao atualizar categoria!")
            return redirect('category')


@method_decorator(login_required, name='dispatch')
class CategoryDeleteView(View):
    def post(self, request, category_id):
        try:
            CategoryService.delete(category_id)
            messages.success(request, "Categoria removida com sucesso!")
            return redirect('category')
        except Exception:
            messages.error(request, "Erro ao remover categoria!")
            return redirect('category')


@method_decorator(login_required, name='dispatch')
class RevenueView(View):
    def get(self, request):
        try:
            categorias = CategoryRepository.get_all(request.user)
            status = RevenueRepository.get_all_status()
            revenue = RevenueService.get_all(request)

            context = {
                'revenue': revenue,
                'status': status,
                'categorias': categorias
            }
            return render(request, 'wallet/revenue.html', context)
        except Exception:
            messages.error(request, "Erro ao listar receitas!")
            return redirect('dashboard')

    def post(self, request):
        try:
            RevenueService.create(request)
            messages.success(request, "Receita cadastrada com sucesso!")
            return redirect('revenue')
        except Exception:
            messages.error(request, "Erro ao cadastrar receita!")
            return redirect('revenue')


@method_decorator(login_required, name='dispatch')
class RevenueEditView(View):
    def post(self, request, revenue_id):
        try:
            RevenueService.update(request, revenue_id)
            messages.success(request, "Receita atualizada com sucesso!")
            return redirect('revenue')
        except Exception:
            messages.error(request, "Erro ao atualizar receita!")
            return redirect('revenue')


@method_decorator(login_required, name='dispatch')
class RevenueDeleteView(View):
    def post(self, request, revenue_id):
        try:
            RevenueService.delete(revenue_id)
            messages.success(request, "Receita removida com sucesso!")
            return redirect('revenue')
        except Exception:
            messages.error(request, "Erro ao remover receita!")
            return redirect('revenue')


@method_decorator(login_required, name='dispatch')
class RevenueCloneView(View):
    def post(self, request, revenue_id):
        try:
            RevenueRepository.clone(revenue_id)
            messages.success(request, "Receita clonada com sucesso!")
            return redirect('revenue')
        except Exception:
            messages.error(request, "Erro ao clonar receita!")
            return redirect('revenue')


@method_decorator(login_required, name='dispatch')
class ExpenseView(View):
    def get(self, request):
        try:
            categorias = CategoryRepository.get_all(request.user)
            status = ExpenseRepository.get_all_status()
            expense = ExpenseService.get_all(request)
            context = {
                'expense': expense,
                'status': status,
                'categorias': categorias,
            }
            return render(request, 'wallet/expense.html', context)
        except Exception:
            messages.error(request, "Erro ao listar despesas!")
            return redirect('dashboard')

    def post(self, request):
        try:
            ExpenseService.create(request)
            messages.success(request, "Despesa cadastrada com sucesso!")
            return redirect('expense')
        except Exception as e:
            messages.error(request, str(e))
            return redirect('expense')


@method_decorator(login_required, name='dispatch')
class ExpenseEditView(View):
    def post(self, request, expense_id):
        try:
            ExpenseService.update(request, expense_id)
            messages.success(request, "Despesa atualizada com sucesso!")
            return redirect('expense')
        except Exception:
            messages.error(request, "Erro ao atualizar despesa!")
            return redirect('expense')


@method_decorator(login_required, name='dispatch')
class ExpenseDeleteView(View):
    def post(self, request, expense_id):
        try:
            ExpenseService.delete(expense_id)
            messages.success(request, "Despesa removida com sucesso!")
            return redirect('expense')
        except Exception:
            messages.error(request, "Erro ao remover despesa!")
            return redirect('expense')


@method_decorator(login_required, name='dispatch')
class ExpenseCloneView(View):
    def post(self, request, expense_id):
        try:
            ExpenseRepository.clone(expense_id)
            messages.success(request, "Despesa clonada com sucesso!")
            return redirect('expense')
        except Exception:
            messages.error(request, "Erro ao clonar despesa!")
            return redirect('expense')


@method_decorator(login_required, name='dispatch')
class InvestmentsView(View):
    def get(self, request):
        try:
            categorias = CategoryRepository.get_all(request.user)
            status = InvestmentsRepository.get_all_status()
            investments = InvestmentsService.get_all(request)
            context = {
                'investments': investments,
                'status': status,
                'categorias': categorias
            }
            return render(request, 'wallet/investments.html', context)
        except Exception:
            messages.error(request, "Erro ao listar investimentos!")
            return redirect('dashboard')

    def post(self, request):
        try:
            InvestmentsService.create(request)
            messages.success(request, "Investimento cadastrada com sucesso!")
            return redirect('investments')
        except Exception as e:
            messages.error(request, str(e))
            return redirect('investments')


@method_decorator(login_required, name='dispatch')
class InvestmentsEditView(View):
    def post(self, request, investments_id):
        try:
            InvestmentsService.update(request, investments_id)
            messages.success(request, "Investimento atualizado com sucesso!")
            return redirect('investments')
        except Exception:
            messages.error(request, "Erro ao atualizar investimento!")
            return redirect('investments')


@method_decorator(login_required, name='dispatch')
class InvestmentsDeleteView(View):
    def post(self, request, investments_id):
        try:
            InvestmentsService.delete(investments_id)
            messages.success(request, "Investimento removido com sucesso!")
            return redirect('investments')
        except Exception:
            messages.error(request, "Erro ao remover investimento!")
            return redirect('investments')


@method_decorator(login_required, name='dispatch')
class InvestmentsCloneView(View):
    def post(self, request, investments_id):
        try:
            InvestmentsRepository.clone(investments_id)
            messages.success(request, "Investimento clonado com sucesso!")
            return redirect('investments')
        except Exception:
            messages.error(request, "Erro ao clonar investimento!")
            return redirect('investments')

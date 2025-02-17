from django.views import View
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.paginator import Paginator

from datetime import datetime

from dateutil.relativedelta import relativedelta

from wallet.models import Category, Expense, Revenue, Investments

@method_decorator(login_required, name='dispatch')
class CategoryView(View):
    def get(self, request):
        categories = Category.objects.all().filter(user=request.user, active=True)
        if request.GET.get('search'):
            search = request.GET.get('search')
            categories = Category.objects.filter(user=request.user, active=True).filter(name__icontains=search)
        
        paginator = Paginator(categories, 6)
        page = request.GET.get('page')
        categories = paginator.get_page(page)
        
        return render(request, 'category.html', {'categories': categories})
    
    def post(self, request):
        user = request.user
        name = request.POST.get('name')
        description = request.POST.get('description')
        category = Category(user=user, name=name, description=description)
        category.save()
        messages.success(request, "Categoria cadastrada com sucesso!")
        return redirect('category')


@method_decorator(login_required, name='dispatch')
class CategoryEditView(View):
    def post(self, request, category_id):
        name = request.POST.get('name_edit')
        description = request.POST.get('description_edit')
        category = get_object_or_404(Category, id=category_id)
        category.name = name
        category.description = description
        category.save()
        messages.success(request, "Categoria atualizada com sucesso!")
        return redirect('category')

@method_decorator(login_required, name='dispatch')
class CategoryDeleteView(View):
    def post(self, request, category_id):
        # import ipdb; ipdb.set_trace()
        category = get_object_or_404(Category, id=category_id)
        category.active = False
        category.save()
        messages.success(request, "Categoria removida com sucesso!")
        return redirect('category')

#Receitas
@method_decorator(login_required, name='dispatch')
class RevenueView(View):
    def get(self, request):
        categorias = Category.objects.all().filter(user=request.user, active=True)
        status = Revenue.STATUS_CHOICES
        revenue = Revenue.objects.filter(user=request.user, active=True)
        
        if request.GET.get('search'):
            search = request.GET.get('search')
            revenue = revenue.filter(description__icontains=search)
        
        date_filter = request.GET.get('date_filter')
        if date_filter:
            filter_type = request.GET.get('filter_type')
            initial_date = request.GET.get('initial_date')
            final_date = request.GET.get('final_date')

            if filter_type == 'payment_date' and initial_date and final_date:
                revenue = revenue.filter(payment_date__range=[initial_date, final_date])

        paginator = Paginator(revenue, 6)
        page = request.GET.get('page')
        revenue = paginator.get_page(page)
        
        context = {
            'revenue': revenue,
            'status': status,
            'categorias': categorias
        }
        return render(request, 'revenue.html', context)
    
    def post(self, request):
        user = request.user
        description = request.POST.get('descricao')
        notes = request.POST.get('observacao')
        amount = request.POST.get('valor')
        amount = float(amount.replace(',', '.'))
        category = request.POST.get('categoria')
        payment_date = request.POST.get('data_pagamento')
        payment_method = request.POST.get('forma_pagamento')
        receipt = request.FILES.get('file')
        # import ipdb; ipdb.set_trace()

        revenue = Revenue(user=user, description=description, notes=notes, amount=amount, category_id=category, 
                          payment_date=payment_date, payment_method=payment_method, receipt=receipt)
        revenue.save()
        messages.success(request, "Receita cadastrada com sucesso!")
        return redirect('revenue')


@method_decorator(login_required, name='dispatch')
class RevenueEditView(View):
    def post(self, request, revenue_id):
        description = request.POST.get('descricao_edit')
        notes = request.POST.get('observacao_edit')
        valor_edit = request.POST.get('valor_edit')
        amount = float(valor_edit.replace(',', '.'))
        category = request.POST.get('categoria_edit')
        payment_date = request.POST.get('data_pagamento_edit')
        payment_method = request.POST.get('forma_pagamento_edit')
        receipt = request.POST.get('file_edit')
        status = request.POST.get('status_edit')

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
        messages.success(request, "Receita atualizada com sucesso!")
        return redirect('revenue')
    

@method_decorator(login_required, name='dispatch')
class RevenueDeleteView(View):
    def post(self, request, revenue_id):
        # import ipdb; ipdb.set_trace()
        revenue = get_object_or_404(Revenue, id=revenue_id)
        revenue.active = False
        revenue.save()
        messages.success(request, "Receita removida com sucesso!")
        return redirect('revenue')

@method_decorator(login_required, name='dispatch')
class RevenueCloneView(View):
    def post(self, request, revenue_id):
        revenue = get_object_or_404(Revenue, id=revenue_id)
        revenue.pk = None
        revenue.save()
        messages.success(request, "Receita clonada com sucesso!")
        return redirect('revenue')


# Despesas
@method_decorator(login_required, name='dispatch')
class ExpenseView(View):
    def get(self, request):
        categorias = Category.objects.filter(user=request.user, active=True)
        status = Expense.STATUS_CHOICES
        expense = Expense.objects.filter(user=request.user, active=True)

        search = request.GET.get('search')
        if search:
            expense = expense.filter(description__icontains=search)

        date_filter = request.GET.get('date_filter')
        if date_filter:
            filter_type = request.GET.get('filter_type')
            initial_date = request.GET.get('initial_date')
            final_date = request.GET.get('final_date')

            if filter_type == 'payment_date' and initial_date and final_date:
                expense = expense.filter(payment_date__range=[initial_date, final_date])
            elif filter_type == 'due_date' and initial_date and final_date:
                expense = expense.filter(due_date__range=[initial_date, final_date])
            elif filter_type == 'todos' and initial_date and final_date:
                expense = expense.filter(payment_date__range=[initial_date, final_date], due_date__range=[initial_date, final_date])

        paginator = Paginator(expense, 6)
        page = request.GET.get('page')
        expense = paginator.get_page(page)

        context = {
            'expense': expense,
            'status': status,
            'categorias': categorias,
        }
        return render(request, 'expense.html', context)
    
    def post(self, request):
        # import ipdb; ipdb.set_trace()
        user = request.user
        description = request.POST.get('descricao')
        notes = request.POST.get('observacao')
        category_id = request.POST.get('categoria')
        payment_method = request.POST.get('forma_pagamento')
        receipt = request.FILES.get('file')

        # Tratamento do valor
        try:
            amount = float(request.POST.get('valor').replace(',', '.'))
        except (ValueError, AttributeError):
            messages.error(request, "Valor inválido.")
            return redirect('expense')

        # Conversão de datas
        try:
            due_date = datetime.strptime(request.POST.get('data_vencimento'), "%Y-%m-%d").date()
        except (ValueError, TypeError):
            messages.error(request, "Data de vencimento inválida.")
            return redirect('expense')

        payment_date = request.POST.get('data_pagamento')
        if payment_date:
            try:
                payment_date = datetime.strptime(payment_date, "%Y-%m-%d").date()
            except ValueError:
                messages.error(request, "Data de pagamento inválida.")
                return redirect('expense')
        else:
            payment_date = None

        # Repetição
        repeat = request.POST.get('repeat')
        try:
            repeat = int(repeat)
        except (ValueError, TypeError):
            repeat = 1 

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

        messages.success(request, "Despesas cadastradas com sucesso!")
        return redirect('expense')


@method_decorator(login_required, name='dispatch')
class ExpenseEditView(View):
    def post(self, request, expense_id):
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
        messages.success(request, "Despesa atualizada com sucesso!")
        return redirect('expense')
    

@method_decorator(login_required, name='dispatch')
class ExpenseDeleteView(View):
    def post(self, request, expense_id):
        # import ipdb; ipdb.set_trace()
        expense = get_object_or_404(Expense, id=expense_id)
        expense.active = False
        expense.save()
        messages.success(request, "Despesa removida com sucesso!")
        return redirect('expense')

@method_decorator(login_required, name='dispatch')
class ExpenseCloneView(View):
    def post(self, request, expense_id):
        expense = get_object_or_404(Expense, id=expense_id)
        expense.pk = None
        expense.save()
        messages.success(request, "Despesa clonada com sucesso!")
        return redirect('expense')

# Investimentos
@method_decorator(login_required, name='dispatch')
class InvestmentsView(View):
    def get(self, request):
        categorias = Category.objects.all().filter(user=request.user, active=True)
        status = Investments.STATUS_CHOICES
        investments = Investments.objects.filter(user=request.user, active=True)
        
        if request.GET.get('search'):
            search = request.GET.get('search')
            investments = investments.filter(description__icontains=search)
        
        date_filter = request.GET.get('date_filter')
        if date_filter:
            filter_type = request.GET.get('filter_type')
            initial_date = request.GET.get('initial_date')
            final_date = request.GET.get('final_date')

            if filter_type == 'investment_date' and initial_date and final_date:
                investments = investments.filter(investment_date__range=[initial_date, final_date])
        
        paginator = Paginator(investments, 6)
        page = request.GET.get('page')
        investments = paginator.get_page(page)
        
        
        context = {
            'investments': investments,
            'status': status,
            'categorias': categorias
        }
        return render(request, 'investments.html', context)
    
    def post(self, request):
        # import ipdb; ipdb.set_trace()
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
        
        expense = Investments(user=user, description=description, notes=notes, amount=amount, category_id=category, 
                          investment_date=investment_date, investment_method=investment_method, receipt=receipt)
        expense.save()
        messages.success(request, "Investimento cadastrada com sucesso!")
        return redirect('investments')


@method_decorator(login_required, name='dispatch')
class InvestmentsEditView(View):
    def post(self, request, investments_id):
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
        messages.success(request, "Investimento atualizado com sucesso!")
        return redirect('investments')
    

@method_decorator(login_required, name='dispatch')
class InvestmentsDeleteView(View):
    def post(self, request, investments_id):
        investments = get_object_or_404(Investments, id=investments_id)
        investments.active = False
        investments.save()
        messages.success(request, "Investimento removido com sucesso!")
        return redirect('investments')

@method_decorator(login_required, name='dispatch')
class InvestmentsCloneView(View):
    def post(self, request, investments_id):
        investments = get_object_or_404(Investments, id=investments_id)
        investments.pk = None
        investments.save()
        messages.success(request, "Investimento clonada com sucesso!")
        return redirect('investments')
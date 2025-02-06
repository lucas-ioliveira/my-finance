from django.views import View
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


from wallet.models import Category, Expense, Revenue

@method_decorator(login_required, name='dispatch')
class CategoryView(View):
    def get(self, request):
        categories = Category.objects.all().filter(user=request.user, active=True)
        if request.GET.get('search'):
            search = request.GET.get('search')
            categories = Category.objects.filter(user=request.user, active=True).filter(name__icontains=search)
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


@method_decorator(login_required, name='dispatch')
class RevenueView(View):
    def get(self, request):
        categorias = Category.objects.all().filter(user=request.user, active=True)
        status = Revenue.STATUS_CHOICES
        revenue = Revenue.objects.all().filter(user=request.user, active=True)
        if request.GET.get('search'):
            search = request.GET.get('search')
            revenue = Revenue.objects.filter(user=request.user, active=True).filter(description__icontains=search)
        
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
        category = request.POST.get('categoria')
        payment_date = request.POST.get('data_pagamento')
        payment_method = request.POST.get('forma_pagamento')
        receipt = request.FILES.get('file')
        import ipdb; ipdb.set_trace()

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
        import ipdb; ipdb.set_trace()
        revenue = get_object_or_404(Revenue, id=revenue_id)
        revenue.active = False
        revenue.save()
        messages.success(request, "Receita removida com sucesso!")
        return redirect('revenue')
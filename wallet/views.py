from django.views import View
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import JsonResponse

import json
from wallet.models import Category

@method_decorator(login_required, name='dispatch')
class CategoryView(View):
    def get(self, request):
        categories = Category.objects.all().filter(user=request.user, active=True)
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
        return render(request, 'revenue.html')
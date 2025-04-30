from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views import View
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import JsonResponse

from accounts.forms import CustomUserCreationForm
from accounts.services.service import AccountService
from accounts.repositories.repository import AccountRepository


class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        messages.success(self.request, "Bem-vindo!")
        return super().form_valid(form)


class RegisterUserView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('login')


class CustomLogoutView(LogoutView):
    def get(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


method_decorator(login_required, name='dispatch')


class CustomPasswordChangeView(PasswordChangeView):
    template_name = 'accounts/profile.html'
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        messages.success(self.request, "Sua senha foi alterada com sucesso!")
        return super().form_valid(form)


method_decorator(login_required, name='dispatch')


class EnderecoView(View):
    def get(self, request):
        try:
            cep_info = AccountService.get_cep_info(request)
            return JsonResponse({'cep_info': cep_info}, status=200)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)


method_decorator(login_required, name='dispatch')


class ProfileView(View):
    def get(self, request):
        try:
            user = request.user
            info_pessoais = AccountRepository.get_by_id(user.id)
            info_contato = AccountRepository.get_contact_details(user)

            context = {
                'info_pessoais': info_pessoais,
                'info_contato': info_contato if info_contato else None
            }
            return render(request, 'accounts/profile.html', context)
        except Exception:
            messages.error(request, "Erro ao acessar suas informações!")
            return redirect('dashboard')

    def post(self, request):
        previous_page = request.META.get("HTTP_REFERER")

        if request.POST.get('info') == 'info_pessoais':
            try:
                AccountService.update_user(request)
                messages.success(request, "Suas informações pessoais foram atualizadas com sucesso!")
                return redirect(previous_page)
            except Exception as e:
                messages.error(request, f"Erro ao atualizar suas informações pessoais: {str(e)}")
                return redirect(previous_page)

        elif request.POST.get('info') == 'info_contato':
            try:
                AccountService.update_contact_details(request)
                messages.success(request, "Seu endereço foi atualizado com sucesso!")
                return redirect(previous_page)
            except Exception as e:
                messages.error(request, f"Erro ao atualizar seu endereço: {str(e)}")
                return redirect(previous_page)

        messages.error(request, "Erro ao atualizar suas informações!")
        return redirect(previous_page)

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.contrib.auth.views import LogoutView
from django.contrib import messages
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from accounts.forms import CustomUserCreationForm
from accounts.models import ContactDetails
from accounts.utils import Accounts


class RegisterUserView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'register.html' 
    success_url = reverse_lazy('login')



class CustomLogoutView(LogoutView):
    def get(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


# class UserProfileUpdateView(LoginRequiredMixin, UpdateView):
#     model = User
#     form_class = UserProfileForm
#     template_name = 'profile.html'
#     success_url = reverse_lazy('profile')

#     def get_object(self, queryset=None):
#         return self.request.user
    
#     def form_valid(self, form):
#         messages.success(self.request, "Seu perfil foi atualizado com sucesso!")
#         return super().form_valid(form)

@login_required
def buscar_endereco(request):
    if request.method == "GET":
        # import ipdb; ipdb.set_trace()
        cep = request.GET.get("cep")
        try:
            cep_info = Accounts.get_cep_info(cep)
            return JsonResponse({'cep_info': cep_info}, status=200)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "CEP inválido"}, status=400)

@login_required
def user_profile(request):
    user = request.user
    previous_page = request.META.get("HTTP_REFERER")
    
    info_pessoais = get_object_or_404(User, id=user.id)
    info_contato = get_object_or_404(ContactDetails, user=user)
    context = {
        'info_pessoais': info_pessoais,
        'info_contato': info_contato
    }

    if request.method == 'GET':
        return render(request, 'profile.html', context)

    elif request.method == 'POST':
        if request.POST.get('info') == 'info_pessoais':
            nome = request.POST.get('nome', user.first_name)
            sobrenome = request.POST.get('sobrenome', user.last_name)
            email = request.POST.get('email', user.email)
            
            user.first_name = nome
            user.last_name = sobrenome
            user.email = email
            user.save()
            messages.success(request, "Suas informações pessoais foram atualizadas com sucesso!")
            return redirect(previous_page)

        elif request.POST.get('info') == 'info_contato':
            Accounts.atualizar_info_contato(user, request.POST)
            messages.success(request, "Seu endereço foi atualizado com sucesso!")
            return redirect(previous_page)
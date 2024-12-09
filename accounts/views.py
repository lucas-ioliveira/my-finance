from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LogoutView
from django.contrib import messages


from accounts.forms import CustomUserCreationForm, UserProfileForm


class RegisterUserView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'register.html' 
    success_url = reverse_lazy('login')



class CustomLogoutView(LogoutView):
    def get(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class UserProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = 'profile.html'
    success_url = reverse_lazy('profile')

    def get_object(self, queryset=None):
        return self.request.user
    
    def form_valid(self, form):
        messages.success(self.request, "Seu perfil foi atualizado com sucesso!")
        return super().form_valid(form)
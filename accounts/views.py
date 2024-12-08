from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from accounts.forms import CustomUserCreationForm


class RegisterUserView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'register.html' 
    success_url = reverse_lazy('login')



class CustomLogoutView(LogoutView):
    def get(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
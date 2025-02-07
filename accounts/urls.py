from django.urls import path
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import views as auth_views

from accounts.views import RegisterUserView, CustomLogoutView, EnderecoView, ProfileView


urlpatterns = [
    path('login/', LoginView.as_view(form_class=AuthenticationForm, template_name='login.html'), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('register/', RegisterUserView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile/buscar-endereco/', EnderecoView.as_view(), name='buscar_endereco'),

]
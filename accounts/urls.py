from django.urls import path, reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView

from accounts.views import RegisterUserView, CustomLogoutView, UserProfileUpdateView
from accounts import views  as v

urlpatterns = [

    path('login/', LoginView.as_view(
        form_class=AuthenticationForm,
        template_name='login.html'
    ), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('register/', RegisterUserView.as_view(), name='register'),
    path('profile/', UserProfileUpdateView.as_view(), name='profile'),
]
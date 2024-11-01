from django.urls import path, reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView

from accounts.views import RegisterUserView

urlpatterns = [

    path('login/', LoginView.as_view(
        form_class=AuthenticationForm,
        template_name='login.html'
    ), name='login'),

    path('logout/', LogoutView.as_view(
        next_page=reverse_lazy('login')
    ), name='logout'),

    path('register/', RegisterUserView.as_view(), name='register'),
]
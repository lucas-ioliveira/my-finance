from django.urls import path
from django.contrib.auth import views as auth_views

from accounts.views import (CustomLoginView, CustomLogoutView, RegisterUserView,
                            CustomPasswordChangeView, EnderecoView, ProfileView,)

urlpatterns = [

    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('register/', RegisterUserView.as_view(), name='register'),
    path('alterar-senha/', CustomPasswordChangeView.as_view(), name='alterar_senha'),
    path('alterar-senha/sucesso/', auth_views.PasswordChangeDoneView.as_view(), name='alterar_senha_sucesso'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile/buscar-endereco/', EnderecoView.as_view(), name='buscar_endereco'),
]

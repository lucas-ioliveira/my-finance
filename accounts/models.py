from django.db import models
from django.contrib.auth.models import User

from common.models import Base

class ContactDetails(Base):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuário')
    phone = models.CharField(max_length=20, verbose_name='Telefone')
    cep = models.CharField(max_length=8, verbose_name='CEP')
    address = models.CharField(max_length=255, verbose_name='Logradouro')
    number_address = models.CharField(max_length=10, verbose_name='Número')
    district = models.CharField(max_length=255, verbose_name='Bairro')
    city = models.CharField(max_length=255, verbose_name='Cidade')
    state = models.CharField(max_length=2, verbose_name='UF')
    complement = models.CharField(max_length=255, verbose_name='Complemento', blank=True, null=True)

    class Meta:
        verbose_name = 'Detalhes de Contato'
        verbose_name_plural = 'Detalhes de Contato'

    def __str__(self):  
        return f'{self.address}'

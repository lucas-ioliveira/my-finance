from django.contrib.auth.models import User
from django.db import models
from common.models import Base


class Category(Base):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Revenue(Base):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuário')
    description = models.CharField(max_length=255, verbose_name='Descrição')  
    notes = models.TextField(blank=True, null=True, verbose_name='Observações')
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Valor')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, verbose_name='Categoria')
    payment_date = models.DateField(verbose_name='Data de Pagamento')
    payment_method = models.CharField(max_length=255, verbose_name='Forma de Pagamento')
    receipt = models.FileField(upload_to='receipts/revenue/', blank=True, null=True, verbose_name='Comprovante')

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.description


class Expense(Base):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuário')
    description = models.CharField(max_length=255, verbose_name='Descrição')
    notes = models.TextField(blank=True, null=True, verbose_name='Observações')
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Valor')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, verbose_name='Categoria')
    payment_date = models.DateField(verbose_name='Data de Pagamento')
    due_date = models.DateField(verbose_name='Data de Vencimento')
    is_paid = models.BooleanField(default=False, verbose_name='Pago')
    payment_method = models.CharField(max_length=255, verbose_name='Forma de Pagamento')
    receipt = models.FileField(upload_to='receipts/expense/', blank=True, null=True, verbose_name='Comprovante')

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.description

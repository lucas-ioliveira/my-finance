from django.contrib.auth.models import User
from django.db import models
from common.models import Base


class Category(Base):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuário')
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Revenue(Base):
    STATUS_CHOICES = [
        ('Pendente', 'Pendente'),
        ('Pago', 'Pago'),
        ('Cancelado', 'Cancelado'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuário')
    description = models.CharField(max_length=255, verbose_name='Descrição')  
    notes = models.TextField(blank=True, null=True, verbose_name='Observações')
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Valor')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, verbose_name='Categoria')
    payment_date = models.DateField(verbose_name='Data de Pagamento')
    payment_method = models.CharField(max_length=255, verbose_name='Forma de Pagamento')
    receipt = models.FileField(upload_to='receipts/revenue/', blank=True, null=True, verbose_name='Comprovante')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pendente', verbose_name='Status')

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.description


class Expense(Base):
    STATUS_CHOICES = [
        ('Atrasado', 'Atrasado'),
        ('Cancelado', 'Cancelado'),
        ('Pago', 'Pago'),
        ('Pendente', 'Pendente'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuário')
    description = models.CharField(max_length=255, verbose_name='Descrição')
    notes = models.TextField(blank=True, null=True, verbose_name='Observações')
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Valor')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, verbose_name='Categoria')
    payment_date = models.DateField(verbose_name='Data de Pagamento', null=True, blank=True)
    due_date = models.DateField(verbose_name='Data de Vencimento')
    payment_method = models.CharField(max_length=255, verbose_name='Forma de Pagamento')
    receipt = models.FileField(upload_to='receipts/expense/', blank=True, null=True, verbose_name='Comprovante')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pendente', verbose_name='Status')

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.description

class Investments(Base):
    STATUS_CHOICES = [
        ('Atrasado', 'Atrasado'),
        ('Cancelado', 'Cancelado'),
        ('Pendente', 'Pendente'),
        ('Realizado', 'Realizado'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuário')
    description = models.CharField(max_length=255, verbose_name='Descrição')
    notes = models.TextField(blank=True, null=True, verbose_name='Observações')
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Valor')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, verbose_name='Categoria')
    investment_date = models.DateField(verbose_name='Data do Investimento')
    investment_method = models.CharField(max_length=255, verbose_name='Método de Investimento')
    receipt = models.FileField(upload_to='receipts/expense/', blank=True, null=True, verbose_name='Comprovante')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pendente', verbose_name='Status')

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.description


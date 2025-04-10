from django.contrib import admin

from wallet.models import Category, Expense, Revenue, Investments


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'name', 'description', 'active', 'created_at', 'updated_at')
    list_display_links = ('name',)
    search_fields = list_display_links
    list_filter = search_fields


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'user', 'description', 'amount', 'category', 'payment_date', 'due_date', 'payment_method',
        'receipt', 'status', 'active', 'created_at', 'updated_at'
    )
    list_display_links = ('description', 'category')
    search_fields = list_display_links
    list_filter = search_fields


@admin.register(Revenue)
class RevenueAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'user', 'description', 'amount', 'category', 'payment_date', 'payment_method',
        'receipt', 'status', 'active', 'created_at', 'updated_at'
    )
    list_display_links = ('description', 'category')
    search_fields = list_display_links
    list_filter = search_fields


@admin.register(Investments)
class InvestmentsAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'user', 'description', 'amount', 'category', 'investment_date', 'investment_method',
        'receipt', 'status', 'active', 'created_at', 'updated_at'
    )
    list_display_links = ('description', 'category')
    search_fields = list_display_links
    list_filter = search_fields

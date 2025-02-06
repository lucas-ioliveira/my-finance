from django.contrib import admin

from wallet.models import Category, Expense, Revenue


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','user', 'name', 'description', 'active', 'created_at', 'updated_at')
    list_display_links = ('name',)
    search_fields = list_display_links
    list_filter = search_fields



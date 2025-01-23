from django.contrib import admin
from accounts.models import ContactDetails

@admin.register(ContactDetails)
class ContactDetailsAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'cep', 'address', 'number_address', 'district', 'city', 'state')
    search_fields = ('cep', 'city', 'state')
    list_filter = search_fields
    list_display_links = ('user','address', )

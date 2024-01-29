from django.contrib import admin
from apps.clients.models import Clients

class ListingClient(admin.ModelAdmin):
    list_display = ('company_name', 'responsible_name', 'cnpj_cpf', 'contact','uf', 'city', 'address', 'email', 'observations', 'autor')
    list_display_links = ('company_name', 'cnpj_cpf')


admin.site.register(Clients, ListingClient)

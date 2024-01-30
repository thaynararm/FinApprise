from django.contrib import admin
from apps.suppliers.models import Suppliers

class ListingSuppliers(admin.ModelAdmin):
    list_display = ('company_name', 'seller_name', 'cnpj_cpf', 'contact','uf', 'city', 'address', 'email', 'observations', 'autor')
    list_display_links = ('seller_name', 'cnpj_cpf')


admin.site.register(Suppliers, ListingSuppliers)

from django.contrib import admin
from apps.revenues.models import Revenues, RecipeSubcategoriesRevenues, RecipeCategoriesRevenues


class ListingRevenues(admin.ModelAdmin):
    list_display = ('description', 'date_of_competence', 'subcategory', 'source', 'value', 'delivery_date', 'receipt_account', 'receipt_status', 'comments', 'autor')
    list_display_links = ('description',)


class ListingSubcategoriesRevenues(admin.ModelAdmin):
    list_display = ('category_name', 'subcategory_name', 'autor')
    list_display_links = ('subcategory_name',)

class ListingCategoriesRevenues(admin.ModelAdmin):
    list_display = ('category_name', 'autor')
    list_display_links = ('category_name',)


admin.site.register(Revenues, ListingRevenues)
admin.site.register(RecipeSubcategoriesRevenues, ListingSubcategoriesRevenues)
admin.site.register(RecipeCategoriesRevenues, ListingCategoriesRevenues)


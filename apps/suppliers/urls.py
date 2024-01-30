from django.urls import path
from apps.suppliers.views import register_supplier


urlpatterns = [
    path('register_supplier/', register_supplier, name='register_supplier'),
]

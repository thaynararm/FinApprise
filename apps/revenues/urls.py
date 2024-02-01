from django.urls import path
from apps.revenues.views import new_revenue

urlpatterns = [
    path('new_revenue/', new_revenue, name='new_revenue')
]

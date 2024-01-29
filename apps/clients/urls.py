from django.urls import path
from apps.clients.views import register_client

urlpatterns = [
    path('register_client/', register_client, name='register_client')
]

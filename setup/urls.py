
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.index.urls')),
    path('', include('apps.clients.urls')),
    path('', include('apps.suppliers.urls')),
    path('', include('apps.users.urls')),
    # path('', include('apps.revenues.urls')),
    # path('', include('apps.expenses.urls')),
    # path('', include('apps.products.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
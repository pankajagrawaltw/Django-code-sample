from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('', include('app.core.urls')),
    path('admin/', include('app.admin_portal.urls')),
    path('django_admin/', admin.site.urls),
]

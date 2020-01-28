from django.urls import path

from app.admin_portal.views import Dashboard


urlpatterns = [
    path('dashboard', Dashboard.as_view(), name='dashboard')
]

from django.urls import path
from . import views

urlpatterns = [
    path('secretary/', views.secretary_dashboard, name='secretary_dashboard'),
    path('admin/', views.admin_dashboard, name='admin_dashboard'),
    path('professional/', views.professional_dashboard, name='professional_dashboard'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('companies/', views.company_list , name='company_list'),  # Add a trailing slash
    path('companies/<int:pk>/', views.company_detail, name='company_detail'),  # Add a slash and fix the path parameter
]

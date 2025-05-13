from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import index

router = DefaultRouter()
router.register(r'index', index)
urlpatterns = [
    path('', include(router.urls)),
]
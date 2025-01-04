from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MovieViewSet, RatingViewSet, UserViewSet

router = DefaultRouter()
router.register(r'movies', MovieViewSet)
router.register(r'ratings', RatingViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

from rest_framework import viewsets
from .models import Movie, Rating
from .serializers import MovieSerializer, RatingSerializer, UserSerializer
from django.contrib.auth.models import User

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


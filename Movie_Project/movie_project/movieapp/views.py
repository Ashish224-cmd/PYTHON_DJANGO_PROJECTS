from django.http import HttpResponse
from django.shortcuts import render, redirect
# from .forms import MovieForm
from.models import Movie

def index(request):
    movie=Movie.objects.all()
    context={'movie_list':movie}
    return (render,'index.html',context)

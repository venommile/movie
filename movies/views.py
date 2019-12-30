from django.shortcuts import render
from django.views.generic.base import View
from django.views.generic import ListView, DetailView
from .models import Movie


class MovieView(ListView):
    """Список фоильмов"""
    model = Movie
    queryset = Movie.objects.filter(draft=False)
    """Django автоматически подставляет suffix +_list"""
    #template_name = "movies/movies.html"

class MovieDetailView(DetailView):

    """Полное название фильма"""
    model = Movie
    slug_field = "url"

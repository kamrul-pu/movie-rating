from django.urls import path

from movie.rest.views.movies import MovieList

urlpatterns = [
    path("", MovieList.as_view(), name="movie-list"),
]

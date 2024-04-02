from django.urls import path

from movie.rest.views.movies import MovieList, MovieSearch


urlpatterns = [
    path("", MovieList.as_view(), name="movie-list"),
    path("/search", MovieSearch.as_view(), name="movie-search"),
]

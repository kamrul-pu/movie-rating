"""Base URLs mappings for movie app."""

from django.urls import path, include

urlpatterns = [
    path("", include("movie.rest.urls.movies"), name="movies"),
    path("/ratings", include("movie.rest.urls.ratings"), name="ratings"),
]

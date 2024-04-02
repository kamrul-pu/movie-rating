from django.urls import path

from movie.rest.views.ratings import RatingsList

urlpatterns = [
    path("", RatingsList.as_view(), name="ratings-list"),
]

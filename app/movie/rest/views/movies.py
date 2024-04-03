"""Views for movie."""

from django.db.models import Avg

from rest_framework.generics import ListCreateAPIView, ListAPIView

from rest_framework.permissions import (
    IsAuthenticated,
)

from movie.models import Movie
from movie.rest.serializers.movies import MovieListSerializer


class MovieList(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)  # Define permissions required for this view
    serializer_class = MovieListSerializer  # Specify the serializer class to be used

    def get_queryset(self):
        # Retrieve all active movies from the database
        queryset = Movie().get_all_actives()

        # Get the 'name' query parameter from the request, if present
        name = self.request.query_params.get("name", "")

        # If 'name' parameter is provided, filter queryset to include only movies with names containing the specified value (case-insensitive)
        if name:
            queryset = queryset.filter(name__icontains=name)
            # Annotate each movie in the queryset with the average rating based on associated ratings
            queryset = queryset.annotate(average_rating=Avg("movie_ratings__rating"))

        return queryset  # Return the queryset for further processing

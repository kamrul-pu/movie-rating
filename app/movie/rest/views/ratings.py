"""Views for Ratings."""

from rest_framework.generics import ListCreateAPIView

from rest_framework.permissions import (
    IsAuthenticated,
)

from movie.models import Ratings
from movie.rest.serializers.ratings import RatingsListSerializer


class RatingsList(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = RatingsListSerializer
    queryset = Ratings().get_all_actives()

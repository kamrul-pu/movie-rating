"""Serializers for Movie Model."""

from rest_framework import serializers


from movie.models import Movie


class MovieListSerializer(serializers.ModelSerializer):
    average_rating = serializers.DecimalField(
        max_digits=3,
        decimal_places=1,
        read_only=True,
    )

    class Meta:
        model = Movie
        fields = (
            "id",
            "name",
            "genre",
            "rating",
            "release_date",
            "average_rating",
        )
        read_only_fileds = (
            "id",
            "average_rating",
        )

"""Serializers for Ratings Model."""

from rest_framework import status
from rest_framework import serializers


from movie.models import Movie, Ratings


class RatingsListSerializer(serializers.ModelSerializer):
    movie = serializers.PrimaryKeyRelatedField(
        write_only=True, queryset=Movie().get_all_actives()
    )

    class Meta:
        model = Ratings
        fields = (
            "id",
            "user_id",
            "movie",
            "movie_id",
            "rating",
        )
        read_only_fileds = ("id",)

    def create(self, validated_data):
        # Retrieve the authenticated user from the request context
        user = self.context.get("request").user

        # Add the user ID to the validated data
        validated_data["user_id"] = user.id

        # Check if a rating already exists for the given user and movie
        rating = Ratings.objects.filter(
            user_id=user.id, movie=validated_data.get("movie")
        ).first()

        # If a rating already exists, raise a validation error
        if rating is not None:
            raise serializers.ValidationError(
                detail="Review of the movie for the user already exists",
                code=status.HTTP_400_BAD_REQUEST,
            )

        # Call the superclass' create method to create the rating
        return super().create(validated_data)

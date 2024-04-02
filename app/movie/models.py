"""Models for Movie related data."""

from django.db import models
from common.models import BaseModelWithUID


class Movie(BaseModelWithUID):
    name = models.CharField(
        max_length=255,
        db_index=True,
    )
    genre = models.CharField(
        max_length=128,
        db_index=True,
    )
    rating = models.CharField(
        max_length=128,
        db_index=True,
        blank=True,
    )
    release_date = models.DateField()

    class Meta:
        verbose_name_plural = "movies"

    def __str__(self) -> str:
        return f"{self.name} - {self.genre}"


class Ratings(BaseModelWithUID):
    user = models.ForeignKey(
        "core.User",
        on_delete=models.CASCADE,
        related_name="user_ratings",
    )
    movie = models.ForeignKey(
        Movie,
        on_delete=models.CASCADE,
        related_name="movie_ratings",
    )
    rating = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        default=0.0,
    )

    class Meta:
        verbose_name_plural = "ratings"
        unique_together = (
            "user",
            "movie",
        )

    def __str__(self) -> str:
        return f"{self.movie} - {self.rating}"

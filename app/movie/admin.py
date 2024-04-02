from django.contrib import admin

from movie.models import Movie, Ratings


class MovieAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "genre", "rating", "release_date")


admin.site.register(Movie, MovieAdmin)


class RatingsAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "rating",
        "status",
    )


admin.site.register(Ratings, RatingsAdmin)

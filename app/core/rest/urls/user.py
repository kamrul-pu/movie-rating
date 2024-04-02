"""Urls mappings for users."""

from django.urls import path

from core.rest.views.user import (
    MeDetail,
    UserList,
    UserDetail,
    UserRegistration,
)

urlpatterns = [
    path("", UserList.as_view(), name="user-list"),
    path("/<int:pk>", UserDetail.as_view(), name="user-details"),
    path("/registration", UserRegistration.as_view(), name="user-registration"),
    path("/me", MeDetail.as_view(), name="me-detail"),
]

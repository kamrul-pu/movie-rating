"""Url heplers for core app."""

from django.urls import reverse


def get_token_url():
    return reverse("token_obtain_pair")

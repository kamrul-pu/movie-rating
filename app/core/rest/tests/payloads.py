"""Payloads for core app."""


def superuser_create_payload():
    return {
        "full_name": "Admin",
        "phone": "017788112233",
        "email": "admin@example.com",
        "password": "testpass123",
    }

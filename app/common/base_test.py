from django.contrib.auth import get_user_model

from rest_framework.test import APITestCase, APIClient
from rest_framework import status


from core.rest.tests import urlhelpers, payloads

User = get_user_model()


class BaseTest(APITestCase):
    """Create a base test class to use multiple places"""

    def setUp(self):
        # Set up a test client
        self.client = APIClient()

        # Define payload
        self.superuser_payload = payloads.superuser_create_payload()

        # Create a superuser
        User.objects.create_superuser(
            name=self.superuser_payload["full_name"],
            phone=self.superuser_payload["phone_number"],
            email=self.superuser_payload["email"],
            password=self.superuser_payload["password"],
        )

        # Login user and assert status
        login_data = {
            "email": self.superuser_payload["email"],
            "password": self.superuser_payload["password"],
        }
        self.user_login = self.client.post(urlhelpers.get_token_url(), login_data)
        self.assertEqual(self.user_login.status_code, status.HTTP_200_OK)

        # Set token for user
        self.client.credentials(
            HTTP_AUTHORIZATION="Bearer " + self.user_login.data["access"],
        )

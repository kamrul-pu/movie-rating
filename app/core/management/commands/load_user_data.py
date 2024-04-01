import os
import json
import logging

from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

from tqdm import tqdm  # Import tqdm for progress bar

# Get the user model
User = get_user_model()

# Set up logging
logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Insert users from JSON files in a directory into the database"

    def handle(self, *args, **options):
        # Directory containing user data JSON file
        user_data_dir = "data/user_data.json"

        # Constructing absolute file path
        file_path = os.path.join(settings.REPO_DIR, user_data_dir)

        try:
            # Open the JSON file and load data
            with open(file_path, "r", encoding="utf-8") as file:
                users_data = json.load(file)
        except FileNotFoundError:
            logger.error(f"File '{file_path}' not found.")
            return
        except json.JSONDecodeError:
            logger.error(f"Invalid JSON format in file '{file_path}'.")
            return

        # Log start of data loading process
        logger.info(f"Loading users data into database......")

        try:
            # Iterate over each user data entry in the JSON file
            for user_data in tqdm(users_data["users_data"]):
                # Try to retrieve existing user by ID or email
                user, created = User.objects.get_or_create(
                    id=user_data["id"],
                    email=user_data["email"],
                    defaults={
                        "name": user_data["name"],
                        "phone": user_data["phone"],
                        "password": user_data["password"],
                        "email": user_data["email"],
                    },
                )

                # Log creation or existence of the user
                if created:
                    logger.info(f"User '{user.name}' created successfully")
                else:
                    logger.warning(f"User '{user.name}' already exists")
        except Exception as e:
            logger.error(f"An error occurred while processing user data: {str(e)}")

        # Log completion of the management script
        logger.info("Management script for loading user data finished!!!")

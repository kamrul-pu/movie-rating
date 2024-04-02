import os
import json
import logging
from datetime import datetime
import decimal

from django.conf import settings

from django.core.management.base import BaseCommand

from tqdm import tqdm  # Import tqdm for progress bar

from movie.models import Ratings

# Set up logging
logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Insert movies ratings from JSON files in a directory into the database"

    def handle(self, *args, **options):
        # Directory containing movie ratings data JSON file
        ratings_data_dir = "data/rating_data.json"

        # Constructing absolute file path
        file_path = os.path.join(settings.REPO_DIR, ratings_data_dir)

        try:
            # Open the JSON file and load data
            with open(file_path, "r", encoding="utf-8") as file:
                ratings_data = json.load(file)
        except FileNotFoundError:
            logger.error(f"File '{file_path}' not found.")
            return
        except json.JSONDecodeError:
            logger.error(f"Invalid JSON format in file '{file_path}'.")
            return

        # Log start of data loading process
        logger.info(f"Loading ratings data into database......")

        try:
            # Iterate over each ratings data entry in the JSON file
            for rating_data in tqdm(ratings_data["ratings"]):
                # Try to retrieve existing rating by user ID and movie id
                rating, created = Ratings.objects.get_or_create(
                    id=rating_data["id"],
                    user_id=rating_data["user_id"],
                    movie_id=rating_data["movie_id"],
                    defaults={
                        "rating": decimal.Decimal(rating_data["rating:"]),
                    },
                )
                # Log creation or existence of the rating
                if created:
                    logger.info(f"Rating '{rating.id}' created successfully")
                else:
                    logger.warning(f"Rating '{rating.id}' already exists")
        except Exception as e:
            logger.error(f"An error occurred while processing rating data: {str(e)}")

        # Log completion of the management script
        logger.info("Management script for loading rating data finished!!!")

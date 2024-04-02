import os
import json
import logging
from datetime import datetime

from django.conf import settings

from django.core.management.base import BaseCommand

from tqdm import tqdm  # Import tqdm for progress bar

from movie.models import Movie

# Set up logging
logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Insert movies from JSON files in a directory into the database"

    def handle(self, *args, **options):
        # Directory containing movie data JSON file
        movie_data_dir = "data/movie_data.json"

        # Constructing absolute file path
        file_path = os.path.join(settings.REPO_DIR, movie_data_dir)

        try:
            # Open the JSON file and load data
            with open(file_path, "r", encoding="utf-8") as file:
                movies_data = json.load(file)
        except FileNotFoundError:
            logger.error(f"File '{file_path}' not found.")
            return
        except json.JSONDecodeError:
            logger.error(f"Invalid JSON format in file '{file_path}'.")
            return

        # Log start of data loading process
        logger.info(f"Loading movies data into database......")

        try:
            # Iterate over each movie data entry in the JSON file
            for movie_data in tqdm(movies_data["movies"]):
                # Example date in current format (DD-MM-YYYY)
                date_str = movie_data["release_date"]

                # Split the date string into day, month, and year
                day, month, year = date_str.split("-")

                # Rearrange the parts into the YYYY-MM-DD format
                correct_date_str = f"{year}-{month}-{day}"

                # Parse the correct date string into a datetime object
                correct_date = datetime.strptime(correct_date_str, "%Y-%m-%d")
                # Try to retrieve existing movie by ID and name
                movie, created = Movie.objects.get_or_create(
                    id=movie_data["id"],
                    name=movie_data["name"],
                    defaults={
                        "genre": movie_data["genre"],
                        "rating": movie_data["rating"],
                        "release_date": correct_date,
                    },
                )

                # Log creation or existence of the movie
                if created:
                    logger.info(f"Movie '{movie.name}' created successfully")
                else:
                    logger.warning(f"Movie '{movie.name}' already exists")
        except Exception as e:
            logger.error(f"An error occurred while processing movie data: {str(e)}")

        # Log completion of the management script
        logger.info("Management script for loading movie data finished!!!")

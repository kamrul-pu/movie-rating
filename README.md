# Movie Rating System

## Introduction

This project implements a movie rating system where users can log in, add movies, view a list of all movies, rate movies, and search for specific movies to see their details along with the average rating.

## Technologies Used

- Python Django: Backend framework for building web applications
- Django REST Framework (DRF): Toolkit for building Web APIs in Django
- SQLite: Database used for storing application data you can use any database
like postgres mysql by giving the url in the environment variable
- Simple JWT: Library for implementing JWT authentication in Django

## Features

- **User Authentication:** Users can log in to the system using their credentials.
- **Add Movie:** Authenticated users can add new movies to the system.
- **View Movie List:** Users can view a list of all movies available in the system.
- **Rate Movie:** Authenticated users can rate movies by assigning a rating score.
- **Search Movie:** Users can search for specific movies by name and view their details along with the average rating.

These features cover the essential functionalities required for the movie rating system as outlined in the project question. Each feature enables users to perform various actions within the system, enhancing their overall experience.

## Setup Instructions

1. Clone the repository:

```bash
git clone https://github.com/your-username/movie-rating-system.git

2. Create a virtual environment then active the virtual environment

3. Install dependencies

```bash
pip install -r requirements/developments.txt

4. create a .env file in the same level of settings.py i.e. app/app/.env copy the dot-env.example data into .env

5. Run migrations to create the database schema:
```bash
python app/manage.py migrate

6. Load sample data provided into the database:
```bash
python app/manage.py load_user_data
python app/manage.py load_movie_data
python app/manage.py load_ratings_data

7. Run the development server:
```bash
python app/manage.py runserver

**Superuser Creation Command**: To create a superuser, run the following command in your terminal:

```bash
python app/manage.py createsuperuser

## Assumptions

- The provided sample data will be used to initialize the database.
- Proper error handling will be implemented to handle invalid requests and responses.

## How Much of the Problem Was Solved

- All required features have been implemented, including user authentication, adding movies, viewing movie lists, rating movies, and searching for specific movies.
- JSON responses are returned from API endpoints with proper error handling.
- JWT authentication is used for user login.

## Problems Faced

- No local database usage was allowed, so SQLite was chosen as a lightweight database solution.
- Implementing JWT authentication for user login required additional setup and configuration.
- Ensuring proper error handling and validation for API requests and responses.

## API Documentation

**Endpoint**: `/api/docs`
- **Description**: Documentation and endpoints of the system.

### Authentication

**Endpoint**: `/api/v1/token`
- **Description**: Generate JWT token for authentication.

### Admin Panel

**URL**: `http://localhost:8000/admin/`
- **Description**: Access the Django admin panel.

### Users

**Endpoint**: `/api/v1/users`
- **Description**: Get a list of users and create new users.

**Endpoint**: `/api/v1/users/registration`
- **Description**: Register a new user.

**Endpoint**: `/api/v1/me`
- **Description**: Get details of the currently logged-in user.

### Movies

**Endpoint**: `/api/v1/movies`
- **Description**: Get a list of movies and create new movies.

**Endpoint**: `/api/v1/movies/search?name=avengers`
- **Description**: Search for a movie by name.

**Endpoint**: `/api/v1/movies/ratings`
- **Description**: Get a list of movie ratings and create new ratings.




## Contact Information

For further inquiries about the project, please contact [Md. Kamrul Hasan] at [kamrul.h456@gmail.com].

# spotdraft-assignment

## Problem statement

make a simple Favorites app that exposes REST APIs for Star Wars data.
The app:
- MUST load planets and movies from the JSON API provided by https://swapi.dev/
- MUST expose list APIs - one for movies and one for planets
- MUST expose APIs to add a movie and planet as a favorite
- The favorite API should also allow setting a custom title/name to the movie/planet
- The planet list API must return the name, created, updated, URL, and is_favorite fields
- The movies list API must return the title, release_date, created, updated, URL and is_favorite fields
- Additionally, the list APIs must support searching by title/name

## Running the Server

1. Install the requirements with the command `pip install -r requirements.txt`
2. Run the migrations with the command `python manage.py migrate`
2. Run the server with the command `python manage.py runserver`

The API will now be available http://localhost:8000/api

## Testing the app

Run the test cases with the command `python manage.py test`

## Endpoints

The following Endpoints are available in the API.

### List Planets

**Endpoint**: `/api/planets`

**Method**: GET

**Query Params**:

Name | Description
--- | --- 
page | Page number of the results to return. 
search | Search planets with this name.

**Response**:

Name | Description
--- | --- 
count | Total count of results found. 
next | Link to the next page of results.
previous | Link to the previous page of results.
results | List of planets.

The results will be a JSON with fields
- name
- created
- edited
- url
- is_favorite


### List Films

**Endpoint**: `/api/films`

**Method**: GET

**Query Params**:

Name | Description
--- | --- 
page | Page number of the results to return. 
search | Search planets with this name.

**Response**:

Name | Description
--- | --- 
count | Total count of results found. 
next | Link to the next page of results.
previous | Link to the previous page of results.
results | List of movies.

The results will be a JSON with fields
- title
- created
- edited
- url
- is_favorite


### Add Favorite Planet

**Endpoint**: `/api/planets/favorites`

**Method**: POST

**Input Data**:

Name | Description
--- | --- 
custom_name | a custom name that can be provided to the planet. 
name | Name of the planet.

**Response**:

Name | Description
--- | --- 
name | Name of the planet saved. 
custom_name | custom_name for the planet


### List Favorite Planets

**Endpoint**: `/api/planets/favorites`

**Method**: GET

**Query Params**:

Name | Description
--- | --- 
page | Page number of the results to return. 

**Response**:

Name | Description
--- | --- 
count | Total count of results found. 
next | Link to the next page of results.
previous | Link to the previous page of results.
results | List of favorite planets.

### Add Favorite Film

**Endpoint**: `/api/films/favorites`

**Method**: POST

**Input Data**:

Name | Description
--- | --- 
custom_title | custom Title for the film. 
title | Title of the film.

**Response**:

Name | Description
--- | --- 
title | Title of the film added to favorite. 
custom_title | the custom_title provided by the user.


### List Favorite Movies

**Endpoint**: `/api/films/favorites`

**Method**: GET

**Query Params**:

Name | Description
--- | --- 
page | Page number of the results to return. 

**Response**:

Name | Description
--- | --- 
count | Total count of results found. 
next | Link to the next page of results.
previous | Link to the previous page of results.
results | List of favorite movies.
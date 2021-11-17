"""Define the services used by the sw_favs application"""
import requests
from rest_framework.exceptions import NotFound


class SwapiService:
    """Service for interacting with the Start Wars API."""

    BASE_URL = 'https://swapi.dev/api/'

    def call(self, uri, method, params, post_json=None):
        """ Function to send the HTTP request to SWAPI"""

        if method == 'GET':
            response = requests.get(self.BASE_URL + uri, params=params)
        else:
            response = requests.post(self.BASE_URL + uri, params=params, json=post_json)

        if response.status_code == 404:
            raise NotFound()

        return response.json()

    def get_planets(self, page=None, search=None):
        """Get the list of planets from the SWAPI."""
        params = {
            'page': page,
            'search': search
        }
        response = self.call('planets/', 'GET', params=params)
        return response

    def get_films(self, page=None, search=None):
        """Get the list of movies from the SWAPI."""
        params = {
            'page': page,
            'search': search
        }
        response = self.call('films/', 'GET', params=params)
        return response

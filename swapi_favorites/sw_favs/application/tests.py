"""Add the test cases for the sw_favs application app"""
from rest_framework.test import APITestCase

class ApplicationTestCases(APITestCase):

    def test_list_planets(self):
        """Test the list planets endpoint."""

        # Get the list of planets
        response = self.client.get('/api/planets')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['count'], 60)
        self.assertIsNotNone(response.json()['next'])
        self.assertIsNone(response.json()['previous'])
        self.assertEqual(response.json()['results'][0]['name'], 'Tatooine')

        # Get the next page of planets list
        response = self.client.get('/api/planets', {'page': 2})
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.json()['next'])
        self.assertIsNotNone(response.json()['previous'])
        self.assertEqual(response.json()['results'][0]['name'], 'Geonosis')

        # Test the searching of planets by name
        response = self.client.get('/api/planets', {'search': 'Utapau'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['count'], 1)
        self.assertEqual(response.json()['results'][0]['name'], 'Utapau')

    def test_list_films(self):
        """Test the list movies endpoint."""

        # Get the list of planets
        response = self.client.get('/api/films')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['count'], 6)
        self.assertIsNone(response.json()['next'])
        self.assertIsNone(response.json()['previous'])
        self.assertEqual(response.json()['results'][0]['title'], 'A New Hope')

        # Get the next page of planets list
        response = self.client.get('/api/films', {'page': 2})
        self.assertEqual(response.status_code, 404)

        # Test the searching of planets by name
        response = self.client.get('/api/films', {'search': 'empire'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['count'], 1)
        self.assertEqual(response.json()['results'][0]['title'], 'The Empire Strikes Back')

    def test_favorite_planet(self):
        """Test the endpoint for adding a planet to favorites."""

        # Get the list of planets
        response = self.client.get('/api/planets')
        self.assertEqual(response.status_code, 200)
        planet = response.json()['results'][2]

        # Add  the planet to favorites
        response = self.client.post(
            '/api/planets/favorites', data={'custom_name': "Planet1", 'name': planet['name']})
        self.assertEqual(response.status_code, 201)

        # Check that the favorite tag is set
        response = self.client.get('/api/planets')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.json()['results'][2]['is_favorite'])

        # Get the list of favorites
        response = self.client.get('/api/planets/favorites')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['count'], 1)
        self.assertEqual(response.json()['results'][0]['name'], planet['name'])

    def test_favorite_film(self):
        """Test the endpoint for adding a movie to favorites."""
        # Get the list of planets
        response = self.client.get('/api/films')
        self.assertEqual(response.status_code, 200)
        movie = response.json()['results'][2]

        # Add  the planet to favorites
        response = self.client.post(
            '/api/films/favorites', data={'custom_title': "Title1", 'title': movie['title']})
        self.assertEqual(response.status_code, 201)

        # Check that the favorite tag is set
        response = self.client.get('/api/films')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.json()['results'][2]['is_favorite'])

        # Get the list of favorites
        response = self.client.get('/api/films/favorites')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['count'], 1)
        self.assertEqual(response.json()['results'][0]['title'], movie['title'])

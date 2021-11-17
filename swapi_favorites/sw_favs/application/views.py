"""Define the views of the sw_favs application app."""
from django.db.models.query import QuerySet
from rest_framework.generics import GenericAPIView, ListCreateAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from sw_favs.application.paginating_serializers import (
    PaginatedFilmSerializer,
    PaginatedPlanetSerializer,
    FavoritePlanetSerializer,
    FavoriteFilmSerializer
)
from sw_favs.application.models import FavoritePlanet, FavoriteFilm
from sw_favs.application.swapi_integration import SwapiService


class PlanetListView(GenericAPIView):
    """View for listing the planets from the SWAPI."""
    serializer_class = PaginatedPlanetSerializer

    def get(self, request):
        """Return the list of planets for the requested page."""

        # Call the service to get the result
        service = SwapiService()

        if(request.query_params.get('search')):
            result = service.get_planets(
            page=request.query_params.get('page', None), search=request.query_params.get('search'))
        else:
            result = service.get_planets(
            page=request.query_params.get('page', 1), search=request.query_params.get('search'))

        # Call the serializer and return the response
        serializer = self.get_serializer(result)
        return Response(serializer.data)


class FilmListView(GenericAPIView):
    """View for listing the movies from the SWAPI."""
    serializer_class = PaginatedFilmSerializer

    def get(self, request):
        """Return the list of planets for the requested page."""

        # Call the service to get the result
        service = SwapiService()

        if(request.query_params.get('search') is not None):
            result = service.get_films(
            page=request.query_params.get('page', None), search=request.query_params.get('search'))
        else:
            result = service.get_films(
            page=request.query_params.get('page', 1), search=request.query_params.get('search'))

        # Call the serializer and return the response
        serializer = self.get_serializer(result)
        return Response(serializer.data)


class PlanetFavoriteListCreateView(ListCreateAPIView):
    """View for listing and creating Planet Favorites."""

    serializer_class = FavoritePlanetSerializer
    queryset = FavoritePlanet.objects.order_by('name')
    pagination_class = PageNumberPagination


class FilmFavoriteListCreateView(ListCreateAPIView):
    """View for listing and creating Movie Favorites."""

    serializer_class = FavoriteFilmSerializer
    queryset = FavoriteFilm.objects.order_by('title')
    pagination_class = PageNumberPagination

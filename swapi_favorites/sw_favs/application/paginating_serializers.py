"""Since swapi.dev paginates the results in blocks of 10, we also have to paginate."""
from django.db.models import fields
from django.db.models.base import Model
from django.urls import reverse
from rest_framework import serializers

from sw_favs.application.utils import get_id_from_url
from sw_favs.application.models import FavoritePlanet, FavoriteFilm

class PaginatedSerializer(serializers.Serializer):
    """Custom Pagination Serializer as we are rendering directly from SWAPI."""
    count = serializers.IntegerField()
    next = serializers.SerializerMethodField()
    previous = serializers.SerializerMethodField()
    route_name = None

    def get_next(self, obj):
        """Replace the SWAPI URL with our URL."""
        next_url = None
        if obj['next']:
            next_url = self.context['request'].build_absolute_uri(reverse(self.route_name))
            next_url = f'{next_url}?{obj["next"].split("?")[-1]}'
        return next_url

    def get_previous(self, obj):
        """Replace the SWAPI URL with our URL."""
        previous_url = None
        if obj['previous']:
            previous_url = self.context['request'].build_absolute_uri(reverse(self.route_name))
            previous_url = f'{previous_url}?{obj["previous"].split("?")[-1]}'
        return previous_url

class PlanetSerializer(serializers.Serializer):
    """Serializer for the Planet Resource."""
    id = serializers.SerializerMethodField()
    name = serializers.CharField(max_length=500)
    created = serializers.DateTimeField()
    edited = serializers.DateTimeField()
    url = serializers.CharField(max_length=500)
    is_favorite = serializers.BooleanField(default=False)

    def get_id(self, obj):
        """Get the ID from the SWAPI URL"""
        return get_id_from_url(obj.get('url'))


class PaginatedPlanetSerializer(PaginatedSerializer):
    """Custom Pagination Serializer as we are rendering directly from SWAPI."""
    results = PlanetSerializer(many=True)
    route_name = 'list-planets'

    def to_representation(self, instance):
        """Override the serialization to include is_favorite field."""
        ret = super().to_representation(instance)

        # For each planet in the result check if a favorite exists and populate is_favorite
        planet_names = [planet['name'] for planet in ret['results']]
        fav_planets = [
            planet.name for planet in FavoritePlanet.objects.filter(name__in=planet_names)]
        for planet in ret['results']:
            planet['is_favorite'] = True if planet['name'] in fav_planets else False
        return ret


class FilmSerializer(serializers.Serializer):
    """Serializer for the Movie Resource."""
    id = serializers.SerializerMethodField()
    title = serializers.CharField(max_length=500)
    created = serializers.DateTimeField()
    edited = serializers.DateTimeField()
    url = serializers.CharField(max_length=500)
    is_favorite = serializers.BooleanField(default=False)

    def get_id(self, obj):
        """Get the ID from the SWAPI URL"""
        return get_id_from_url(obj.get('url'))


class PaginatedFilmSerializer(PaginatedSerializer):
    """Custom Pagination Serializer as we are rendering directly from SWAPI."""
    results = FilmSerializer(many=True)
    route_name = 'list-films'

    def to_representation(self, instance):
        """Override the serialization to include is_favorite field."""
        ret = super().to_representation(instance)

        # For each movie in the result check if a favorite exists and populate is_favorite
        film_titles = [film['title'] for film in ret['results']]
        fav_films = [
            film.title for film in FavoriteFilm.objects.filter(title__in=film_titles)]
        for film in ret['results']:
            film['is_favorite'] = True if film['title'] in fav_films else False
        return ret


class FavoritePlanetSerializer(serializers.ModelSerializer):
    """Serializer for the Planet Favorite Resource."""
    custom_name = serializers.CharField()

    class Meta:
        """Options for the Planet Favorite Serializer."""
        model = FavoritePlanet
        fields = ('name', 'custom_name')


class FavoriteFilmSerializer(serializers.ModelSerializer):
    """Serializer for the Movie Favorite Resource."""
    custom_title = serializers.CharField()

    class Meta:
        """Options for the Planet Favorite Serializer."""
        model = FavoriteFilm
        fields = ('title', 'custom_title')

from django.db import models
from requests import NullHandler

class FavoritePlanet(models.Model):
    """Model for saving Planet information to the local Database."""
    custom_name = models.CharField(max_length=500, default=NullHandler)
    name = models.CharField(max_length=500)


class FavoriteFilm(models.Model):
    """Model for saving the Movie information to the local Database."""
    custom_title = models.CharField(max_length=500, default=NullHandler)
    title = models.CharField(max_length=500)

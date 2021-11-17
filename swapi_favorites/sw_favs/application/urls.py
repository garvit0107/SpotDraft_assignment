"""Define the urls of the sw_facs application app."""
from django.urls import path
from sw_favs.application import views

urlpatterns = [
    path('planets', views.PlanetListView.as_view(), name='list-planets'),
    path('planets/favorites',
         views.PlanetFavoriteListCreateView.as_view(),
         name='list-create-planet-favorites'),
    path('films', views.FilmListView.as_view(), name='list-films'),
    path('films/favorites',
         views.FilmFavoriteListCreateView.as_view(),
         name='list-create-film-favorites'),
]

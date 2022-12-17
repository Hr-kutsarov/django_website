from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('plays/', AllPlays.as_view(), name='all-plays'),
    path('plays/<slug:slug>/', PlayDetailsView.as_view(), name='play-details'),
    path('create_play/', CreatePlay.as_view(), name='create-play'),
    path('<slug:slug>/edit/', EditPlay.as_view(), name='edit-play'),
    path('<slug:slug>/delete/', DeletePlay.as_view(), name='delete-play'),
    path('search/', search_plays, name='search_results'),
    path('profile/', profile, name='profile'),

    path('news/', AllNews.as_view(), name='all-news'),
    path('create_news/', NewsCreate.as_view(), name='create-news'),
    path('news_details/<int:pk>', NewsDetails.as_view(), name='details-news'),
    path('news_edit/<int:pk>', NewsEdit.as_view(), name='edit-news'),
    path('news_delete/<int:pk>', NewsDelete.as_view(), name='delete-news'),


    path('artists/', AllArtists.as_view(), name='all-artists'),
    path('create_artist/', ArtistCreate.as_view(), name='create-artist'),
    path('artists_details/<int:pk>', ArtistDetails.as_view(), name='details-artist'),
    path('artists_edit/<int:pk>/', ArtistEdit.as_view(), name='edit-artist'),
    path('artists_delete/<int:pk>', ArtistDelete.as_view(), name='delete-artist'),

]

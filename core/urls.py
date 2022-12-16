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
    path('edit/<int:pk>', NewsEdit.as_view(), name='edit-news'),
    path('delete/<int:pk>', NewsDelete.as_view(), name='delete-news'),
]

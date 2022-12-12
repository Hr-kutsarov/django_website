from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('plays/', AllPlays.as_view(), name='all-plays'),
    path('plays/<slug:slug>/', PlayDetailsView.as_view(), name='play-details'),
    path('create_play/', CreatePlay.as_view(), name='create-play'),
    path('<slug:slug>/edit/', EditPlay.as_view(), name='edit-play'),
]

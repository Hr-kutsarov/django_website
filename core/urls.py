from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('plays/', AllPlays.as_view(), name='all-plays'),
    path('plays/<slug:slug>/', PlayDetailsView.as_view(), name='play-details')
]

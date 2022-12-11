from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('events/', AllPlays.as_view(), name='all-plays'),
]

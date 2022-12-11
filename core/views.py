from django.shortcuts import render
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from django.views.generic import TemplateView, FormView, ListView
from . models import *
from django.views import generic as views


class Home(views.TemplateView):
    template_name = 'core/home.html'
    date = datetime.now()
    extra_context = {'date': date}


class AllPlays(views.ListView):
    model = Play
    template_name = 'core/all_events.html'






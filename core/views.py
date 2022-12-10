from django.shortcuts import render
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from django.views.generic import TemplateView, FormView, ListView
from . models import *


def home(request):
    date = datetime.now()
    context = {'date': date}
    return render(request, 'core/home.html', context)


def all_events(request):
    all_events = Play.objects.all()
    context = {'all_events': all_events}
    return render(request, 'core/all_events.html', context)


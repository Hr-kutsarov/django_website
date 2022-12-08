from django.shortcuts import render
import calendar
from calendar import HTMLCalendar
from datetime import datetime


def home(request):
    date = datetime.now()

    return render(request, 'plays/home.html', {'date': date})

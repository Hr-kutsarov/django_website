from datetime import datetime

from django.shortcuts import render
from django.urls import reverse_lazy
from . models import *
from django.views import generic as views
from .forms import PlayForm


class Home(views.TemplateView):
    template_name = 'core/home.html'
    date = datetime.now()
    extra_context = {'date': date}


class AllPlays(views.ListView):
    model = Play
    context_object_name = 'plays'
    template_name = 'core/all_plays.html'


class PlayDetailsView(views.DetailView):
    model = Play
    template_name = 'core/play_details.html'
    context_object_name = 'play'


class CreatePlay(views.CreateView):
    template_name = 'core/play_create.html'
    form_class = PlayForm
    success_url = reverse_lazy('all-plays')


class EditPlay(views.UpdateView):
    model = Play
    form_class = PlayForm
    template_name = 'core/play_edit.html'
    context_object_name = 'play'
    success_url = reverse_lazy('all-plays')


class DeletePlay(views.DeleteView):
    model = Play
    template_name = 'core/delete-confirm.html'
    success_url = reverse_lazy('all-plays')


def search_plays(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        plays = Play.objects.filter(title__contains=searched)
        number_of_plays = len(plays)
        return render(request, 'core/search.html', {'plays': plays, 'searched': searched, 'number_of_plays': number_of_plays})










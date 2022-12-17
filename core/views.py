from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse_lazy
from . models import *
from django.views import generic as views
from .forms import PlayForm, NewsForm, ArtistForm
from itertools import chain


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
        artists = Artist.objects.filter(Q(first_name__contains=searched) | Q(last_name__contains=searched))
        news = News.objects.filter(title__contains=searched)
        number_of_items = len(plays) + len(artists) + len(news)
        context = {'plays': plays, 'news': news, 'artists': artists, 'searched': searched, 'number_of_plays': number_of_items}
        return render(request, 'core/search.html', context)


def profile(request):
    return render(request, 'core/profile.html', {})


class AllNews(views.ListView):
    model = News
    template_name = 'core/news_all.html'
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super(AllNews, self).get_context_data(**kwargs)
        news = News.objects.all()
        paginator = Paginator(news, self.paginate_by)

        page = self.request.GET.get('page')

        try:
            file_news = paginator.page(page)
        except PageNotAnInteger:
            file_news = paginator.page(1)
        except EmptyPage:
            file_news = paginator.page(paginator.num_pages)

        context['all_news'] = file_news
        return context


class NewsCreate(views.CreateView):
    template_name = 'core/news_create.html'
    form_class = NewsForm
    success_url = reverse_lazy('all-news')


class NewsDetails(views.DetailView):
    template_name = 'core/news_details.html'
    model = News
    context_object_name = 'news'


class NewsEdit(views.UpdateView):
    model = News
    form_class = NewsForm
    template_name = 'core/news_edit.html'
    context_object_name = 'news'
    success_url = reverse_lazy('all-news')


class NewsDelete(views.DeleteView):
    model = News
    template_name = 'core/delete-confirm.html'
    success_url = reverse_lazy('all-news')


class AllArtists(views.ListView):
    model = Artist
    context_object_name = 'artists'
    template_name = 'core/artists_all.html'


class ArtistCreate(views.CreateView):
    template_name = 'core/artists_create.html'
    form_class = ArtistForm
    success_url = reverse_lazy('all-artists')


class ArtistDetails(views.DetailView):
    model = Artist
    template_name = 'core/artists_details.html'
    context_object_name = 'artists'


class ArtistEdit(views.UpdateView):
    model = Artist
    form_class = ArtistForm
    template_name = 'core/artists_edit.html'
    context_object_name = 'artists'
    success_url = reverse_lazy('all-artists')


class ArtistDelete(views.DeleteView):
    model = Artist
    template_name = 'core/delete-confirm.html'
    success_url = reverse_lazy('all-artists')

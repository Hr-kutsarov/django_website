from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from django.urls import reverse_lazy
from . models import *
from django.views import generic as views
from .forms import PlayForm, NewsForm


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
        context = {'plays': plays, 'searched': searched, 'number_of_plays': number_of_plays}
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





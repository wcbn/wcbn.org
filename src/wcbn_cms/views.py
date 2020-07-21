from django.shortcuts import render
from django.views.generic import ListView
from .models import Article, Event, Concert


class ArticleListView(ListView):
    template_name = "articles/list.html"
    model = Article


class EventsListView(ListView):
    template_name = "layouts/main_with_aside.html"
    model = Event
    paginate_by = 20
    ordering = ['-start_date', '-start_time', '-end_date', '-end_time']

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['main'] = "events/list.html"
        ctx['aside'] = "homepage/aside.html"
        ctx['title'] = "Upcoming Events"
        return ctx


class ConcertListView(ListView):
    template_name = "layouts/main_with_aside.html"
    model = Concert
    paginate_by = 20
    ordering = ['start_date', 'start_time', 'end_date', 'end_time']

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['main'] = "events/list.html"
        ctx['aside'] = "homepage/aside.html"
        ctx['title'] = "Upcoming Concerts"
        return ctx

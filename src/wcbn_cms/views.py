from django.shortcuts import render
from django.views.generic import ListView
from .models import Article, Event, Concert


class ArticleListView(ListView):
    template_name = "articles/list.html"
    model = Article


class EventsListView(ListView):
    template_name = "layouts/with_sidebar.html"
    model = Event
    ordering = ['-start_date', '-start_time', '-end_date', '-end_time']

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['partial'] = "events/list.html"
        ctx['title'] = "Upcoming Events"
        return ctx


class ConcertListView(ListView):
    template_name = "layouts/with_sidebar.html"
    model = Concert
    ordering = ['-start_date', '-start_time', '-end_date', '-end_time']

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['partial'] = "events/list.html"
        ctx['title'] = "Upcoming Concerts"
        return ctx

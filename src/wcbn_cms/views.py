import requests
from django.shortcuts import render
from django.views.generic import ListView
from .models import Article, Event, Concert
from .services.happening_at_umich import transform_concerts


def get_happening_at_michigan(url):
    resp = requests.get(url)
    return resp.json()


class ArticleListView(ListView):
    template_name = "articles/list.html"
    model = Article


class EventsListView(ListView):
    template_name = "layouts/main_with_aside.html"
    model = Event
    paginate_by = 20
    ordering = ['-start_date', '-start_time', '-end_date', '-end_time']

    def get_context_data(self, **kwargs):
        umich_events = get_happening_at_michigan("https://events.umich.edu/list/json?filter=show:new")

        ctx = super().get_context_data(**kwargs)
        ctx['main'] = "events/list.html"
        ctx['aside'] = "events/aside.html"
        ctx['campus_events'] = transform_concerts(umich_events)
        ctx['title'] = "Upcoming Events"
        return ctx


class ConcertListView(ListView):
    template_name = "layouts/main_with_aside.html"
    model = Concert
    paginate_by = 20
    ordering = ['start_date', 'start_time', 'end_date', 'end_time']

    def get_context_data(self, **kwargs):
        umich_concerts = get_happening_at_michigan("https://events.umich.edu/list/json?filter=tags:Music,Concert,show:new")

        ctx = super().get_context_data(**kwargs)
        ctx['main'] = "events/list.html"
        ctx['aside'] = "events/aside.html"

        ctx['campus_events'] = transform_concerts(umich_concerts)
        ctx['title'] = "Upcoming Concerts"
        return ctx

import requests
from django.shortcuts import render
from django.views.generic import ListView
from django.utils import timezone
from .models import Article, Event, Concert
from .services.happening_at_umich import get_events as get_umich_events
from django.shortcuts import get_object_or_404


class ArticleListView(ListView):
    template_name = 'layouts/main_with_aside.html'
    model = Article
    paginate_by = 20

    def get_queryset(self):
        print('articles')
        pk = self.kwargs.get('pk')
        if pk:
            obj = get_object_or_404(self.model, pk=pk)
            return [obj]

        return self.model.objects.filter(published_at__lte=timezone.now()).order_by('-published_at')


class EventsListView(ListView):
    template_name = "layouts/main_with_aside.html"
    model = Event
    paginate_by = 20
    ordering = ['start_date', 'start_time', 'end_date', 'end_time']

    def get_queryset(self):
        print('events')
        pk = self.kwargs.get('pk')
        if pk:
            event_obj = get_object_or_404(self.model, pk=pk)
            return [event_obj]

        return self.model.objects.filter(start_date__gte=timezone.now())

    def get_context_data(self, **kwargs):
        umich_events = get_umich_events()

        ctx = super().get_context_data(**kwargs)
        ctx['main'] = "events/list.html"
        ctx['aside'] = "events/aside.html"
        ctx['campus_events'] = umich_events
        ctx['title'] = "Upcoming Events"
        ctx['model_name'] = 'event'
        return ctx


class ConcertListView(EventsListView):
    """
    Concerts are a type of event, so this inherits from 
    the EventsListView and overrides class members as needed
    """
    model = Concert

    def get_context_data(self, **kwargs):
        umich_concerts = get_umich_events(["Music", "Concert"])

        ctx = super().get_context_data(**kwargs)
        ctx['campus_events'] = umich_concerts
        ctx['title'] = "Upcoming Concerts"
        ctx['model_name'] = 'concert'
        return ctx

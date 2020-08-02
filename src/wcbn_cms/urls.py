from django.urls import path
from .views import *
from django.contrib.flatpages.views import flatpage
from django.views.decorators.cache import cache_page

app_name = 'wcbn_cms'
urlpatterns = [
    path('', cache_page(120)(ArticleListView.as_view()), name='cms'),
    path('events/', cache_page(120)(EventsListView.as_view()), name='events'),
    path('concerts/', cache_page(120)(ConcertListView.as_view()), name='concerts'),
    path('about/', flatpage, {'url': '/about/'}, name='about'),
    path('contact/', flatpage, {'url': '/contact/'}, name='contact')
]

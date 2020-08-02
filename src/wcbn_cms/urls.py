from django.urls import path
from .views import *
from django.contrib.flatpages.views import flatpage
from django.views.decorators.cache import cache_page
from wcbn_core.views import HomepageView

app_name = 'wcbn_cms'
urlpatterns = [
    path('articles/<int:pk>/', cache_page(1)(HomepageView.as_view()), name='articles'),

    path('events/', cache_page(1)(EventsListView.as_view()), name='events'),
    path('events/<int:pk>/', EventsListView.as_view(), name='events'),

    path('concerts/', cache_page(1)(ConcertListView.as_view()), name='concerts'),
    path('concerts/<int:pk>/', ConcertListView.as_view(), name='concerts'),

    path('about/', flatpage, {'url': '/about/'}, name='about'),
    path('contact/', flatpage, {'url': '/contact/'}, name='contact')
]

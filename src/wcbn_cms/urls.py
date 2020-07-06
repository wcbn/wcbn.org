from django.urls import path
from .views import *
from django.contrib.flatpages.views import flatpage

app_name = 'wcbn_cms'
urlpatterns = [
    path('', ArticleListView.as_view(), name='cms'),
    path('events/', EventsListView.as_view(), name='events'),
    path('concerts/', ConcertListView.as_view(), name='concerts'),
    path('about/', flatpage, {'url': '/about/'}, name='about'),
    path('contact/', flatpage, {'url': '/contact/'}, name='contact')
]

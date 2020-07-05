from django.urls import path
from .views import *

app_name = 'wcbn_cms'
urlpatterns = [
    path('', ArticleListView.as_view(), name='cms'),
    path('events/', EventsListView.as_view(), name='events'),
]

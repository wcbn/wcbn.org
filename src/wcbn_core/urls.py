from django.urls import path
from wcbn_core.views import *

app_name = 'wcbn_core'
urlpatterns = [
    path('', HomepageView.as_view(), name='homepage'),
]

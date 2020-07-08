from django.urls import path
from readback.views import *

app_name = 'readback'
urlpatterns = [
    path('schedule/', schedule, name='schedule'),
    path('playlist/', playlist, name='playlist'),
    path('djs/<int:dj_id>', dj, name='dj')
]

import requests
from django.shortcuts import render
from .transformers import transform_schedule
from django.conf import settings


def schedule(request):
    url = f'{settings.READBACK_URL}/semesters.json'
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    resp = requests.get(url, headers=headers)

    ctx = {}
    ctx['weekdays'] = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    ctx['schedule'] = transform_schedule(resp.json())
    ctx['title'] = "Schedule"
    return render(request, 'schedule.html', context=ctx)

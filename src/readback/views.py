import requests
from datetime import datetime, timedelta
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


def playlist(request):
    now = datetime.now().isoformat()
    one_day_ago = (datetime.now() - timedelta(days=1)).isoformat()
    
    url = f'{settings.READBACK_URL}/playlist/archive.json'
    params = {
         "til": now,
        "from": one_day_ago
    }
    resp = requests.get(url, params=params)

    ctx = {
        'items': resp.json()['items'],
        'playlist_limit': one_day_ago
    }

    return render(request, 'playlist.html', context=ctx)
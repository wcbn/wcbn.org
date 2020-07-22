import requests
from datetime import datetime, timedelta
from django.shortcuts import redirect, render
from .transformers import transform_schedule_table, transform_schedule_accordion
from django.conf import settings
from django.utils import timezone
from django.views.decorators.cache import cache_page


@cache_page(2* 60 * 60) # 2 hours
def schedule(request):
    url = f'{settings.READBACK_URL}/semesters.json'
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    resp = requests.get(url, headers=headers)

    ctx = {}
    ctx['weekdays'] = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    ctx['schedule_accordion'] = transform_schedule_accordion(resp.json(), ctx['weekdays'])
    ctx['schedule_table'] = transform_schedule_table(resp.json())
    ctx['title'] = "Schedule"
    return render(request, 'schedule.html', context=ctx)


def playlist(request):
    # TODO verify all timezones work
    now = timezone.now().isoformat()
    x = 1
    x_days_ago = (timezone.now() - timedelta(days=x)).isoformat()

    url = f'{settings.READBACK_URL}/playlist/archive.json'
    params = {
        "til": now,
        "from": x_days_ago
    }
    resp = requests.get(url, params=params).json()

    ctx = {
        'items': resp['items'],
        'playlist_limit': x_days_ago
    }

    return render(request, 'playlist.html', context=ctx)


def dj(request, dj_id):
    return redirect(settings.READBACK_URL + request.path)

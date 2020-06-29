import re
import json
import requests
import time
from django.shortcuts import render
from .util import get_diff_v2


def schedule(request):
    ctx = {}
    headers = {'Accept': 'application/json',
               'Content-Type': 'application/json'}
    r = requests.get('https://app.wcbn.org/semesters.json', headers=headers)
    resp = r.json()

    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    
    shows_obj = {}
    for i, day in enumerate(weekdays):
        shows_obj[day] = resp['shows'][str(i+1)] # {"Monday" : [{show1, show2}]}

    for day in shows_obj:
        for show_index, show in enumerate(shows_obj[day]):
            diff = int(get_diff_v2(show['beginning'], show['ending']))
            shows_obj[day][show_index]['diff'] = diff

    ctx['sched'] = shows_obj

    return render(request, 'schedule.html', context=ctx)

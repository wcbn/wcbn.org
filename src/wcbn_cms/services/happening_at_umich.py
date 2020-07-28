"""Simple wrapper for the "Happening @ Michigan" events API. See docs: https://events.umich.edu/feeds"""

from datetime import datetime, timedelta
import requests


def get_events(tags=[]):
    """
    Primary entrypoint for this module
    Input: tags?: string[]
    Output: event[]
    """
    try:
        url = build_url(tags)
        resp = requests.get(url)
        json_resp = resp.json()
        return transform(json_resp)
    except:
        return []


def build_url(tags=[]):
    BASE_URL = "https://events.umich.edu"

    tags_str = "tags:" + ','.join(tags) if len(tags) > 0 else ""

    today = datetime.strftime(datetime.now(), "%Y-%m-%d")
    x = 6
    x_weeks_hence = datetime.strftime(datetime.now() + timedelta(weeks=x), "%Y-%m-%d")
    time_range_str = f"range={today}to{x_weeks_hence}"

    return f"{BASE_URL}/list/json?filter=show:new,{tags_str}&{time_range_str}"


def transform(json_resp):
    LIMIT = 75
    result = []
    for key, event in json_resp.items():
        date_start = datetime.strptime(event['date_start'], '%Y-%m-%d')
        time_start = datetime.strptime(event['time_start'], '%H:%M:%S')

        new_event = {}
        new_event['month'] = datetime.strftime(date_start, '%b')
        new_event['day'] = datetime.strftime(date_start, '%d')
        new_event['title'] = event['event_title']
        new_event['location'] = event['location_name']
        new_event['time'] = time_start
        # new_event['description'] = event['description']
        new_event['url'] = event['permalink']
        result.append(new_event)

        if len(result) >= LIMIT:
            return result

    return result

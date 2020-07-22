from datetime import datetime
import time
from django.template.defaultfilters import time as time_filter

def transform_concerts(json_resp):
    LIMIT = 75
    result = []
    for key, event in json_resp.items():
        """
        Month
        Day
        Title
        Location
        Time
        Description...
        URL
        """
        # datetime_start = strptime(event['datetime_start'], '%Y%m%dT%H%M%S')
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

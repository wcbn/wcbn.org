from django import template
from django.template.defaultfilters import date, time

register = template.Library()

@register.filter
def format_event_time(event):
    """
    Input: object with required start_date, optional end_date, start_time, end_time
    """
    # format everything
    start_date = date(event.start_date, "l, N jS")
    end_date = date(event.end_date, "l, N jS")
    start_time = time(event.start_time)
    end_time = time(event.end_time)
    
    # just times
    if event.end_date in [None, event.start_date]:
        if start_time and end_time:
          return f"{start_time} - {end_time}"
        if start_time:
          return start_time
        if end_time:
          return f"Ends at {end_time}"
        return ""

    # datetimes because starts and ends on different dates
    if start_time:
        start_date = f"{start_date} {start_time}"
    if end_time:
        end_date = f"{end_date} {end_time}"

    return f"{start_date} - {end_date}" if end_date else ""

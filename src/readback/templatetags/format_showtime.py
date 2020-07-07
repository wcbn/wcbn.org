from datetime import datetime
from django import template
from django.template.defaultfilters import time as time_filter 


register = template.Library()

@register.filter
def format_showtime(isoformat):
    """
    Usage: "2018-01-09T06:00:00.000-05:00"|format_showtime
    """
    if isoformat == '':
        return ''
    dt = datetime.fromisoformat(isoformat).time()
    return time_filter(dt)

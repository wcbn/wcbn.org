from collections import deque
from datetime import datetime


def transform_schedule_accordion(resp, weekdays):
    """
    Accepts: response from /semesters.json
    Produces:
    {"Monday" : [show_objects], "Tuesday" : [show_objects], ...}
    """

    result = {}

    for index, (key, shows) in enumerate(resp['shows'].items()):
        result[weekdays[index]] = shows

    return result

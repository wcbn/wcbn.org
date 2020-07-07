from collections import deque
from datetime import datetime

def transform_schedule(resp):
    """
    Accepts: response from /semesters.json
    Produces:
    [
        [{show_name: 'tight pants', rowspan: 2}, {show_name: 'slipstream radio', rowspan: 1}, ...],
        [{show_name: 'seizure experiment', rowspan: 1}, ...]
        ...
    ]
    """

    all_shows = []
    for weekday_index, shows in resp['shows'].items():
        all_shows += shows

    unique_showtimes = get_unique_showtimes(all_shows)
    shows = assign_rowspans(all_shows, unique_showtimes)
    table_rows = create_table_rows(shows, unique_showtimes)
    return table_rows


def get_unique_showtimes(shows):
    """
    Accepts list of shows
    Returns list of unique showtimes, sorted but starting at 6am
    e.g. ['06:00', '09:00', '11:00', '12:00', '14:00', '17:00', '23:00', '00:00', '02:00', '03:00']
    """
    result = set()
    for show in shows:
        showtime = get_timestamp(show['beginning'])
        endtime = get_timestamp(show['ending'])
        result.add(showtime)
        result.add(endtime)

    result = list(result)
    result.sort()

    # move shows before 6am to end of list
    pre_six_am_count = 0
    for time in result:
        if time < '06:00':
            pre_six_am_count += 1
        else:
            break

    result = deque(result)
    result.rotate(-pre_six_am_count)
    return list(result)


def get_timestamp(isoformat):
    """
    Accepts an iso datetime e.g. "2018-01-15T06:00:00.000-05:00"
    Returns HH:MM string e.g. "06:00"
    """
    return str(datetime.fromisoformat(isoformat).time().replace(second=0,microsecond=0))



def get_shows_at(shows, showtime):
    return [s for s in shows if get_timestamp(s['beginning']) == showtime]


def create_table_rows(shows, showtimes):
    return [get_shows_at(shows, showtime) for showtime in showtimes]


def assign_rowspans(shows, showtimes):
    for index, show in enumerate(shows):
        rowspan = get_rowspan(show, showtimes)
        shows[index]['rowspan'] = rowspan
    return shows


def get_rowspan(show, showtimes):
    """
    Accepts a show obj and list of unique showtimes
    Returns distance between beginning and ending timestamps out of all showtimes
    """
    x = get_timestamp(show['beginning'])
    y = get_timestamp(show['ending'])
    if x not in showtimes or y not in showtimes:
        raise AssertionError("showtime not in showtimes")
    delta = showtimes.index(y) - showtimes.index(x)
    return max(delta, 0)

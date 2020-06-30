# import re, time, datetime

# def datetimestamp_to_time(x):
#     x = x.split("T")[1] # get timestamp
#     x = re.sub(r'\.\d+', "", x) # remove millis
#     x = time.strptime(x, '%H:%M:%S%z')
#     return x

# def get_diff(datetimestamp1, datetimestamp2):
#     t1 = datetimestamp_to_time(datetimestamp1)
#     t2 = datetimestamp_to_time(datetimestamp2)
#     return abs((time.mktime(t1) - time.mktime(t2)) / 60)

# def get_diff_v2(beginning, ending):
#     d1 = datetime.datetime.fromisoformat(beginning)
#     d2 = datetime.datetime.fromisoformat(ending)
#     delta = int((d2 - d1).seconds / 60)
#     return delta


from ics import Calendar
from datetime import datetime

def parse_ics(file_stream):
    calendar = Calendar(file_stream.read().decode())
    events = []

    for e in calendar.events:
        events.append({
            "title": e.name,
            "start": e.begin.datetime,
            "end": e.end.datetime,
            "location": e.location,
            "description": e.description
        })
    return events
from ics import Calendar

def read_ics(file):
    calendar = Calendar(file.read().decode())
    data = []
    for e in calendar.events:
        data.append({
            "title": e.name,
            "start": e.begin.datetime,
            "end": e.end.datetime
        })
    return data

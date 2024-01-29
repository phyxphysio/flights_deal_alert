from datetime import datetime as dt
import settings
import datetime


def set_dates(soonest_departure=settings.SOONEST_DEPARTURE, latest_departure=settings.LATEST_DEPARTURE):
    today = dt.now()
    soonest = today + datetime.timedelta(days=soonest_departure)
    latest = today + datetime.timedelta(days=latest_departure)
    date_from = soonest.strftime("%d/%m/%Y")
    date_to = latest.strftime("%d/%m/%Y")
    return date_from, date_to


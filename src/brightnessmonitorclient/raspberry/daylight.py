import datetime
import sunrise
from pytz import reference
from brightnessmonitorclient.api_client import update

LATITUDE = 0.0
LONGITUDE = 0.0
currenttz = reference.LocalTimezone()
currenttz.tzname(datetime.datetime.now())

def setLocation():
    update.set_location(datetime.datetime.now())
    LATITUDE = update.latitude
    LONGITUDE = update.longitude

def getSunrise():
    s = sunrise.sun(LATITUDE, LONGITUDE)
    return s.sunrise(when=datetime.datetime.now(tz=currenttz))

def getSunset():
    s = sunrise.sun(LATITUDE, LONGITUDE)
    return s.sunset(when=datetime.datetime.now(tz=currenttz))

def checkDaylight():
    if getSunrise() < datetime.datetime.now().time() < getSunset():
        return True
    else:
        return False

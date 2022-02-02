import geocoder as geo  # https://geocoder.readthedocs.io/providers/IPInfo.html
import datetime as dt
import urllib.request, json
import time

def getLatLong():
    gloc = geo.ip('me')
    # TODO: make pop up appear and have user enter their address (country/city) since ip look-up failed
    if not gloc.ok:
        pass  # https://geocoder.readthedocs.io/providers/HERE.html
    return gloc.latlng


def getDate():
    date = dt.date.today()
    return date


def getCity():
    print(geo.ip('me'))
    date = geo.ipinfo()
    print(date)
    return date.city

def getTimezone():
    offset = time.timezone if (time.localtime().tm_isdst == 0) else time.altzone
    offset = offset / 60 / 60 * -1
    return str(int(offset))

def getDefaults():
    latlong=getLatLong()
    link="https://api.sunrise-sunset.org/json?"+"lat="+str(latlong[0])+"&"+"lng="+str(latlong[1])
    tz=getTimezone()
    data = json.loads(urllib.request.urlopen(link).read().decode())
    if data['results']['sunrise'][1] == ':':
        sunrisehour = str(int(data['results']['sunrise'][0])+int(tz)) + data['results']['sunrise'][1:]
        #print(sunrisehour)
    else:
        sunrisehour = str(int(data['results']['sunrise'][0:2])+int(tz)) + data['results']['sunrise'][2:]
        #print(sunrisehour)


    if data['results']['sunset'][1] == ':':
        sunsethour = str(int(data['results']['sunset'][0]) + int(tz)) + data['results']['sunset'][1:]
        #print(sunsethour)
    else:
        sunrisehour = str(int(data['results']['sunset'][0:2])+int(tz)) + data['results']['sunset'][2:]
        #print(sunrisehour)

    return (sunrisehour,sunsethour)

if __name__ == "__main__":
    print(getDefaults())

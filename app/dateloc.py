import geocoder as geo #https://geocoder.readthedocs.io/providers/IPInfo.html
import datetime as dt

#TODO: for figuring out sunset/sunrise: https://sunrise-sunset.org/api (needs converting from UTC to local time https://stackoverflow.com/questions/68664644/how-can-i-convert-from-utc-time-to-local-time-in-python)

def getLatLong():
    gloc = geo.ip('me')
    #TODO: make pop up appear and have user enter their address (country/city) since ip look-up failed
    if not gloc.ok:
        pass #https://geocoder.readthedocs.io/providers/HERE.html
    return gloc.latlng 

def getDate():
    date = dt.date.today()
    return date

if __name__ == "__main__":
    print(getLatLong(), getDate())


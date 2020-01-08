import os
import pyowm
from datetime import datetime, timedelta

OWM_API_KEY = os.environ.get('OWM_API_KEY')
#print(OWM_API_KEY)
owm = pyowm.OWM(OWM_API_KEY)
COUNTRY = 'US'
observation = owm.weather_at_id(4407084)

w = observation.get_weather()
print(w)
print('test')
print(w.get_temperature('fahrenheit'))

description = w.get_detailed_status()
clouds = str(w.get_clouds())
temperature = w.get_temperature()
wind = w.get_wind()
rain = w.get_rain()

print('description: ' + description + "\r\n" + "cloud coverage: %" + clouds)



import os
import pyowm
from time import time, ctime

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
clouds = w.get_clouds()
temperature = w.get_temperature()
wind = w.get_wind()
rain = w.get_rain()
sunrise = w.get_sunrise_time()
sunset = w.get_sunset_time()



print("sunrise: ",ctime(sunrise))
print("sunset: ",ctime(sunset))
if clouds < 20:
	print('It should be sunny- GLASSES!')

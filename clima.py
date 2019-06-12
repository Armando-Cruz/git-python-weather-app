import urllib.request
from json import loads

def obtenerTemperatura(lat, long):
	app_id = 'your app id'
	res = urllib.request.urlopen(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={long}&appid={app_id}&units=metric')
	data = loads(res.read())
	return data['main']['temp']
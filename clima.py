import urllib.request
from json import loads

def obtenerTemperatura(lat, long):
	res = urllib.request.urlopen(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={long}&appid=c2a271768289d76eba596f4abc02cb3a&units=metric')
	data = loads(res.read())
	return data['main']['temp']
from lugar import obtenerCoordenadas
from clima import obtenerTemperatura

def obtenerClima(direccion):
	coordenadas = {}
	temperatura = 0
	try:
		coordenadas = obtenerCoordenadas(direccion)
		temperatura = obtenerTemperatura(coordenadas['lat'], coordenadas['long'])
	except Exception:
		return f'No se pudo determinar el clima de {direccion}'
	return f'Clima:\n{coordenadas["direccion"]}\nTemperatura: {temperatura}°'

print('--- Weather App ---')
direccion = input('Ciudad: ')
print(f'\n{obtenerClima(direccion)}')
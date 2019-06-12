import urllib.request
from urllib.parse import quote 
from json import loads


def obtenerCoordenadas(direccion):
	# Codifica la direccion para ser una url válida
	url = quote(direccion) 
	# Crea un obeto de tipo request 
	req = urllib.request.Request(f'https://devru-latitude-longitude-find-v1.p.rapidapi.com/latlon.php?location={url}')
	# Agrega encabezados a la petición
	req.add_header('X-RapidAPI-Key', 'efcdd99310mshb14d34b125b4ecep18fa47jsnb2fb1ae86bce')
	# Realiza la petición, devuelve un objeto de tipo httpresponse
	res = urllib.request.urlopen(req)
	# Convirtiendo json a objeto python y antes leyendo la respuesta 
	data = loads(res.read())
	resultados = data['Results']
	# Si no hay resultados
	if (len(resultados) == 0):
		raise ValueError(f'No se encontraron resultados para {direccion}') 
	return {
		'direccion': resultados[0]['name'],
		'lat': resultados[0]['lat'],
		'long': resultados[0]['lon']
	}
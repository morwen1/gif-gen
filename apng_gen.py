import os  
from apng import APNG as ap
dir_result= 'result/'
dir_data= 'imgs/'


def creacion(dir_result,dir_data):
	imgs = os.listdir(dir_data)
	imgs.sort()
	lista = []
	for i in imgs:
		lista.append(dir_data + i)
	ap.from_files(lista,delay=100).save('prueba.png')
	print(lista)
creacion(dir_result,dir_data)

import numpy as np
import cv2

def multimatz(ma,mb):
	[columa,filma,tema]= ma.shape
	[columb,filmb]=mb.shape
	mattriz= (columa,filma)
	resultado=np.zeros(mattriz)

	for fila in range(filma):
		for columnas in range(columa):
			print(ma[fila][columnas])
			print(mb[fila])
			resultado=resultado+ (ma[fila][columnas]*mb[fila])
			print(resultado)
	return resultado

def conv(ima,ker):
	[columima, filaima,temima] = ima.shape
	[columker,filasker]=ker.shape
	columnasff=columima-columker-1
	filasff= filaima - filasker-1
	mres= (columnasff,filasff)
	con=np.zeros(mres)


	for filas in range(filasff):
		for columnas in range(columnasff):
			con=multimatz(ima[filas:filas+filasker,columnas:columker+columnas],ker)
	return con


gato= r'C:\Users\Danie\Documents\ambiente\actividades\Semana Tec\gato.png'
imagen=cv2.imread(gato)
gray=cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
cv2.imshow('gris',gray)
cv2.waitKey(0)
kerfufle= np.array([[1,1,1],[0,0,0],[-1,-1,-1]])
respuesta=conv(imagen,kerfufle)
cv2.imshow('imagen',respuesta)
cv2.waitKey(0)
import numpy as np
import cv2

def multimatz(ma,mb):
	columa,filma,tema= ma.shape
	columb,filmb=mb.shape
	resultado=0.00

	for fila in range(filma):
		for columnas in range(columa):
			resultado=resultado+ (ma[fila][columnas]*mb[fila][columnas])
	return resultado

def conv(ima,ker):
	columima, filaima,temima= ima.shape
	columker,filasker=ker.shape
	columnasff=columnasima-columnasker+1
	filasff- filaima - filasker+1
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
cv2.waitkey(0)
tres=(3,3)
kerfufle= np.ones(tres)
respuesta=conv(imagen,kerfufle)
cv2.imshow('imagen',respuesta)
cv2.waitkey(0)
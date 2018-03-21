import numpy as np

#Funcion que retorna la distribucion normal con un promedio y desviacion estandar dados por parametro

def normal_dist(x,mean,sigma):
	parte1=np.sqrt(1.0/np.pi()*sigma**2)
	parte2=-((x-mean)**2)/sigma**2)
	funcion=parte1*np.exp(parte2)

	return funcion


def get_fit(filename):
	

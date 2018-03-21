import numpy as np

#Primera funcion de numeros aleatorios para probabilidad discreta
def sample_1(N):
	array=[-10,-5,3,9]
	p=[0.1,0.4,0.2,0.3]
	return np.random.choice(array,N,p)

#Segunda funcion de numeros aleatorios para probabilidad exponencial
def sample_2(N):
	scale_b=0.5
	return np.random.exponential(scale_b,N)

#Tercera funcion de numeros aleatorios que genera y retorna M promedios Sn 
a1=0
prom=[]
def get_mean(sampling_fun,N,M):
	for i in range (M):
		if(sampling_fun==sample_1):
			a1=np.mean(sample_1(N))
			prom.append(a1)
		elif(sampling_fun==sample_2):
			a1=np.mean(sample_2(N))
			prom.append(a1)

	return prom

#Genera los archivos de texto que contengan los datos de las funciones con los valores dados para el ejercicio

M=10000
lista=[sample_1,sample_2]
nombres=["sample_1","sample_2"]
N=[10,100,1000]

#Ciclo que me recorre la lista de las variables asociadas a las funciones "Sample_ 1 y 2" y crea archivos .txt para cada uno de los casos que solicitan

for i in range (len(lista)):
	for j in range(len(N)):
		valor=get_mean(lista[i],N[j],M)
		np.savetxt(nombres[i]+"_"+str(N[j])+".txt",valor)













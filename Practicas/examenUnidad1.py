def ordenar(lista,cantidad):
	if cantidad>1:
		for i in range(0,cantidad-1):
			if lista[i]>lista[i+1]:
				aux=lista[i]
				lista[i]=lista[i+1]
				lista[i+1]=aux
			ordenar(lista,cantidad-1)
			
def ordenarReversa(lista,cantidad):
	if cantidad>1:
		for f in range(0,cantidad-1):
			if lista[f]<lista[f+1]:
				aux=lista[f]
				lista[f]=lista[f+1]
				lista[f+1]=aux
			ordenarReversa(lista,cantidad-1)
			
datos=[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
ordenar(datos,len(datos))
print(datos)
ordenarReversa(datos,len(datos))
print(datos)

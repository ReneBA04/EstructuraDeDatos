#La recursividad genera pilas 

def jugar(intento = 1):
	respuesta = input(" ¿De que color es una naranja? ")
	if respuesta != "naranja":
		if intento < 3:
			print("\n Fallaste intenta de nuevo ")
			intento+=1
			jugar(intento)
	else:
		print("\n Ganaste ")

jugar()

#Se desborda la pila
def imprimir(x):
	print(x)
	imprimir(x-1)
	
imprimir(5)
# 5 a 1
def imprimir(x):
	if x>0:
		print(x)
		imprimir(x-1)
		
imprimir(5)
print("\n")
#1 a 5
def imprimir(x):
	if x>0:
		imprimir(x-1)
		print(x)
		
imprimir(5)
print("\n")

#Factorial de un número
def factorial(fact):
	if fact>0:
		valor = fact*factorial(fact-1)
		return valor
	else:
		return 1
print(f"el factorial de 4 es: {factorial(4)}")

#Método receursivo para ordenar una lista
def ordenar(lista, cant):
	if cant>1:
		for f in range(0, cant-1):
			if lista[f]>lista[f+1]:
				aux = lista[f]
				lista[f] = lista[f+1]
				lista[f+1] = aux
			ordenar(lista,cant-1)
			
datos=[60,44,22,33,2]
print(datos)
ordenar(datos,len(datos))
print(datos)

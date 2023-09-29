import random
numeroalt1 = random.randint(1, 10)
numeroalt2 = random.randint(1, 10)
resultado=[]
resultado.append(numeroalt1)
resultado.append(numeroalt2)
print(resultado)
respuesta=[]
def capturarNombre():
	print('¡Hola! ¿Cómo te llamas?')
	nombre = input()
	print(f"Bueno {nombre}, estoy pensando dos números entre 1 y 10.")

def jugar(intentos=1):
	print("adivinalos!")
	numero1=int(input("Numero 1-> "))
	numero2=int(input("Numero 2-> "))
	respuesta.append(numero1)
	respuesta.append(numero2)
	if numero1!=numeroalt1 or numero2!=numeroalt2:
		if intentos<6:
			print(f"intento {intentos} fallado Ups!, los numeros no son correctos prueba de nuevo")
			if respuesta[0]==resultado[0] and respuesta[1]==resultado[1]:
				print(f"{resultado[0]} y {respuesta[0]} son iguales al igual que {resultado[1]} y {respuesta[1]}:)")
			
			if respuesta[0]<resultado[0] and respuesta[1]==resultado[1]:
				print(f"el numero {respuesta[0]} está bajo pero el numero {respuesta[1]} es correcto")
			
			if respuesta[0]>resultado[0] and respuesta[1]==resultado[1]:
				print(f"el numero {respuesta[0]} está alto, pero el numero {respuesta[1]} es correcto")
			
			if respuesta[0]==resultado[0] and respuesta[1]<resultado[1]:
				print(f"el numero {respuesta[0]} es correcto, pero el numero {respuesta[1]} está bajo")
			
			if respuesta[0]==resultado[0] and respuesta[1]>resultado[1]:
				print(f"el numero {respuesta[0]} es correcto, pero el numero {respuesta[1]} está alto")
			intentos+=1
			jugar(intentos)
		else:
			print("Más suerte para la proxima")
	else:
		print(f"Felicidades!, Has ganado en {intentos} intentos")

capturarNombre()
jugar()

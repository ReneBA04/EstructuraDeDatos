from clasePila import Pila

def calculadora_polaca(elementos):
	pila = Pila()
for elemento in elementos:
	print ("DEBUG:", elemento)
	# Intenta convertirlo a número
	try:
		numero = float(elemento)
		pila.apilar(numero)
		print ("DEBUG: apila ", numero)
	# Si no se puede convertir a número, debería ser un operando
	except ValueError:
	# Si no es un operando válido, levanta ValueError
		if elemento not in "+-*/ %" or len(elemento) != 1:
			raise ValueError("Operando inválido")
	# Si es un operando válido, intenta desapilar y operar
	try:
		a1 = pila.desapilar()
		print ("DEBUG: desapila ",a1)
		a2 = pila.desapilar()
		print ("DEBUG: desapila ",a2)
	# Si hubo problemas al desapilar
	except ValueError:
		print ("DEBUG: error pila faltan operandos")
		raise ValueError("Faltan operandos")
	if elemento == "+":
		resultado = a2 + a1
	elif elemento == "-":
		resultado = a2 - a1
	elif elemento == "*":
		resultado = a2 * a1
	elif elemento == "/":
		resultado = a2 / a1
	elif elemento == " %":
		resultado = a2 % a1
	print ("DEBUG: apila ", resultado)
	pila.apilar(resultado)
# Al final, el resultado debe ser lo único en la Pila
return pila.desapilar()
if pila.es_vacia():
	return res
else:
	print ("DEBUG: error pila sobran operandos")
	raise ValueError("Sobran operandos")

def main():
	expresion = input("Ingrese la expresion a evaluar: ")
	elementos = expresion.split()
	print (calculadora_polaca(elementos))
	
main()

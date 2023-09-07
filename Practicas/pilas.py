class Pila:
	"""Representa una pila con operaciones de apilar, desapilar,"""
	
	def __init__(self):
		"""Crea pila vacia."""
		#El método apilar se implementará agregando el nuevo elemento al final de la lista
		self.items=[]
	
	def apilar(self, x):
		"""Agrega el elemento x a la pila"""
		x=int(input("Ingrese un numero -> "))
		self.items.append(x)
	
	def desapilar(self):
		"""Devuelve el elemento tope y lo elimina de la pila.
		si la pila esta vacia levanta una excepcion"""
		try:
			return self.items.pop()
		except IndexError:
			raise ValueError("La pila esta vacía")

	def es_vacia(self):
		"""Devuelve True si la lista está vacía, False si no."""
		return self.items == []
		
	def imprimirPila(self):
		for item in self.items:
			print(str(item))

pila = Pila()
def menu():
	x=0
	while x<=1:
		print("Elija una opcion")
		print("1)apilar")
		print("2)desapilar")
		print("3)vaciar")
		print("4)mostrar")
		print("5)salir")
		r=int(input("-> "))
		if r == 1:
			pila.apilar(0)
		if r == 2:
			print(f"se desapiló el elemento {pila.desapilar()}")
		if r == 3:
			if pila.es_vacia()==True:
				print("La pila se encuentra vacia")
			else:
				print("La pila contiene elementos")
		if r == 4:
			pila.imprimirPila()
		else:
			break
menu()

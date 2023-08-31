Alimentos = ['sandwich', 'torta', 'dobladitas', 'tacos', 'hamburguesa']
Bebidas = ['agua', 'refresco', 'jugo', 'cafe', 'te']
Nombre = []

def capturarAlumno():
	contador=0
	alumnos = int(input("Alumnos a capturar -> "))
	while contador < alumnos:
		nombre = input('Nombre -> ')
		Nombre.append(nombre)
		contador+=1
		
def asignarComida(Alimentos,Bebidas,Nombre):
	for alimentos, bebidas, nombre in zip (Alimentos,Bebidas, Nombre):
		print("la comida: {0} y la bebida: {1} se les dio al alumno: {2} ".format(alimentos, bebidas, nombre))
	for i in range(len(Nombre)):
		Nombre.pop()
		
def imprimirDatos():
	print(f"Comida {Alimentos},\nBebidas {Bebidas},\nAlumnos en fila {Nombre}")
	
def menu():
	x=1
	while x<=2:
		print("1) Capturar Alumno")
		print("2) Realizar pedido")
		print("3) Mostrar datos")
		print("4) Salir")
		r=int(input("-> "))
		if r == 1:
			capturarAlumno()
		elif r == 2:
			asignarComida(Alimentos,Bebidas,Nombre)
		elif r == 3:
			imprimirDatos()
		
menu()

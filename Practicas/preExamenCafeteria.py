alimentos = ['sandwich', 'torta', 'dobladitas', 'tacos', 'hamburguesa']
bebidas = ['agua', 'refresco', 'jugo', 'cafe', 'te']
nombre = []
ordenes = []

def capturarAlumno(contador=0):
	alumnos = int(input("Alumnos a capturar -> "))
	while contador < alumnos:
		nombres = input('Nombre -> ')
		nombre.append(nombres)
		contador+=1
	
def elegirComida(alimentos,bebidas):
	if len(nombre)==0:
		print("No hay ordenes todavia")
	else:
		for nombres in nombre:
			print(nombre)
			nombres=input("Cliente a atender -> ")
			if nombres not in nombre:
				print("Este nombre aun no ha sido registrado")
			elif nombres in nombre:
				print(f"Bienvenido {nombres}, Seleccione algo del menu :)\n")
				print(alimentos)
				print(bebidas)
				mc = input("Comida -> ")
				mb = input("Bebida -> ")
				if mc in alimentos and mb in bebidas and nombres in nombre:
					alimentos.remove(mc)
					bebidas.remove(mb)
					nombre.remove(nombres)
					ordenes.append([mc,mb,nombres])
					print(ordenes)
				
def mostrarOrdenes():
	if len(ordenes)==0:
		print("No hay ordenes todavía")
	else:
		print(f"Hay {len(ordenes)} ordenes")
		
def menu(x):
	if x<5:
		menu(x+1)
		print("1) Capturar Alumno")
		print("2) Elegir Comida")
		print("3) Realizar pedido")
		print("4) Mostrar ordenes")
		print("5) Salir")
		r=int(input("-> "))
		if r == 1:
			capturarAlumno()
		elif r==2:
			elegirComida(alimentos,bebidas)
		elif r==3:
			mostrarOrdenes()
menu(1)

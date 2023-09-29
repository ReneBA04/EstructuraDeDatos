import random
class Juego:
	def __init__(self, nombre):
		self.nombre = nombre
		self.numalt = random.randint(1,1000)
	def capturarNombre(self):
		print("Hola, ¿Cómo te llamas?")
		self.nombre=input("-> ")
		return self.nombre
		
	def jugar(self,intento=1):
		print(f"Hola de nuevo {self.nombre}, vamos a jugar un juego :)")
		print("estoy pensando en un numero del 1 al 1000,¿Cúal crees que es?")
		r=int(input("-> "))
		if r!=self.numalt:
			if intento<5:
				print(f"Intento {intento} fallado intenta de nuevo.")
				if r<self.numalt:
					print("Ups!, el numero que ingresaste es bajo\n")
				elif r>self.numalt:
					print("Ups!, el numero que ingresaste es alto\n")
				intento+=1
				juego.jugar(intento)
			else:
				print("Has perdido, se acabaron los intentos :(")
		else:
			print(f"felicidades {self.nombre} haz ganado en {intento} intento(s)")
		
juego=Juego("default")
def main():
	while True:
		print("Numeros aleatorios")
		print("Menú\n1)Introducir nombre\n2)Jugar\n3)repetir\n4)Salir")
		r=int(input("Introduzca su opción->\n"))
		if r==1: 
			juego.capturarNombre()
		elif r==2:
			juego.jugar()
		elif r==3:
			continue
		else:
			break
if __name__=="__main__":
	main()

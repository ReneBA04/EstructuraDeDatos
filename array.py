arreglo=[]
x=0
while x<=1:
	print("¿Cúal es tu nombre?")
	nombre=input("-> ")
	print("¿Cúal es tu edad?")
	edad=int(input("-> "))
	arreglo.append([nombre,edad])
	print(arreglo,"\n")
	print("¿Desea agregar más datos?\n 1)si\n 2)no")
	r=input("->")
	if r==1:
		continue
	else:
		break

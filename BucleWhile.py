x=1
i=0
while i<=x:
  nombre=str(input("Escirbe tu nombre: "))
  print(f"Hola {nombre}, ¿Cómo estas?")
  edad=int(input("¿Cúal es tu edad? "))
  print(f"{nombre} tiene {edad} años")
  print("\n")
  print("¿Deseas capturar otros datos?")
  print("1)si")
  print("2)No")
  opc=int(input("Ingrese su opcion-> "))
  if opc==1:
    continue
  else:
    break

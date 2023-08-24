factura=['pan', 'huevos', 100, 1234]
print(factura)
print(factura[0])
print(factura[3])
print(len(factura))
print(len(factura)-1)
#pueden usarse índices negativos,siendo -1 el índice del ultimo elemento
print(factura[-1])
#los indices negativos van entonces de -1(ultimo elemnto) a -len(factura)(primer elemento)
print(factura[-len(factura)])
#Mutabilidad de los elemntos de la lista
factura[1]="Carne"
print(factura)
a3=["Hola pa",2]
factura[2]=a3
print(factura)
print(len(factura))

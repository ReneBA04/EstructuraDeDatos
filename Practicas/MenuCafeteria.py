comidas=['Torta','Hamburguesa','Dobladitas','Gorditas','Chilaquiles']
bebidas=['Jugo','Coca cola','Agua','Repeticola','Squirt']
alumunos=[]

def captura():
    val=input("->")
    return val

def menu():
    op=0
    while op!=5:
        print("\n**Elegir Opcion**")
        print("1. Agregar alumnos a fila\n2. Servir Comida alumno\n3. Preparar comidad\n4. Preparar bebida\n5. Salir")
        op=int(captura())
        if op==1:
            alumc()
        elif op==2:
            servir()
        elif op==3:
            comida()
        elif op==4:
            bebida()

def alumc():
    print("Numero de alumnos a agregar a la fila")
    n=int(captura())
    for i in range(0,n):
        print("Nombre alumno",i+1,"")
        nom=captura()
        alumnos.append(nom)

def servir():
    if len(alumnos)>=1 and len(comidas)>=1 and len(bebidas)>=1:
        print("Al alumno {0} se le sirvio {1} de comida y {2} de bebida".format(alumnos[0],bebidas[0],comidas[0]))
        comidas.reverse()
        bebidas.reverse()
        falum.reverse()
        comidas.pop()
        bebidas.pop()
        falum.pop()
        comidas.reverse()
        bebidas.reverse()
        falum.reverse()
    else:
        print("***ERROR***")
        print("Hay",len(alumnos),"alumnos en fila")
        print("Hay", len(comidas), "comidas en fila")
        print("Hay", len(bebidas), "bebidas en fila")

def comida():
    print("Numero de comidas a preparar")
    n=int(captura())
    for i in range(0,n):
        print("Comida preparada",i+1,":")
        nom=captura()
        comidas.append(nom)

def bebida():
    print("Numero de bebidad a preparar")
    n=int(captura())
    for i in range(0,n):
        print("Bebida preparada",i+1,":")
        nom=captura()
        bebidas.append(nom)

menu()

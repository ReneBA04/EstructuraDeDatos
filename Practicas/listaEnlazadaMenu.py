#creacion de la clase nodo
class node:
  def __init__(self, data=None, next=None):
    self.data=data
    self.next=next

#Creacion de la clase lista enlazada
class linked_list:
  def __init__(self):
    self.head=None

#Metodo agregar elementos en el frente de la lista enlazada
  def add_at_front(self,data):
    self.head=node(data=data, next=self.head)

#Metodo para verificar si la estructura esta vacia
  def is_empty(self):
    return self.head==None

#Metodo agregar al final de la lista enlazada
  def add_at_end(self, data):
    if not self.head:
      self.head=node(data=data)
      return
    curr=self.head
    while curr.next:
      curr=curr.next
    curr.next=node(data=data)

#Metodo eliminar nodos
  def delete_nodo(self,key):
    curr=self.head
    prev=None
    while curr and curr.data!=key:
      prev=curr
      curr=curr.next
    if prev is None:
      self.head=curr.next
    elif curr:
      prev.next=curr.next
      curr.next=None

#Obtener el ultimo nodo
  def get_last_node(self):
    temp=self.head
    while (temp.next is not None):
      temp=temp.next
    return temp.data

#Imprimir nodos
  def print_list(self):
    node=self.head
    while node!=None:
      print(node.data,end=" -> ")
      node=node.next

listita=linked_list()

def menu():
    op=0
    while op!=4:
        print("\n1. Agregar Producto")
        print("2. Borrar Producto")
        print("3. Imprimir")
        print("4. Salir")
        op=int(captura())
        if op==1:
            print("Agregar a la lista")
            cosa=captura()
            listita.add_at_front(cosa)
        elif op==2:
            print("Producto a eliminar")
            cosa = captura()
            listita.delete_nodo(cosa)
        elif op==3:
            listita.print_list()
        elif op==4:
            print("Hasta luego")


def captura():
    val = input("->")
    return val

menu()

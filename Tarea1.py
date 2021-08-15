class estudiante:
  def __init__(self, carnet, nombre, edad, direccion, telefono, email, carrera, puesto):
    self.carnet = carnet
    self.nombre = nombre
    self.edad = edad
    self.direccion = direccion
    self.telefono = telefono
    self.email = email
    self.carrera = carrera
    self.puesto = puesto

class nodo:
  def __init__(self, estudiante= None, siguiente = None):
    self.estudiante = estudiante
    self.siguiente = siguiente

class lista_enlazada:
  def __init__(self):
    self.primero = None

  def insertar(self, estudiante):
    if self.primero is None:
      self.primero = nodo(estudiante=estudiante)
      return
    actual = self.primero
    while actual.siguiente:
      actual = actual.siguiente
    actual.siguiente = nodo(estudiante=estudiante)
    
  def recorrer(self):
    actual= self.primero
    while actual != None:
      print("carnet: ", actual.estudiante.carnet,"nombre: ", actual.estudiante.nombre, "email: ", actual.estudiante.email, "->")
      actual = actual.siguiente 

  def eliminar(self, carnet):
    actual = self.primero
    anterior = None

    while actual and actual.estudiante.carnet != carnet:
      anterior = actual
      actual = actual.siguiente

    if anterior is None:
      self.primero = actual.siguiente
      actual.siguiente = None
    elif actual:
      anterior.siguiente = actual.siguiente
      actual.siguiente = None

e1 = estudiante(201915060, "Gerson Ortiz", 20, "9 calle 10-02 zona 1", 24400101, "gerson.ortiz@gmail.com", "Ingenieria en Sistemas", "Programador Jr.")
e2 = estudiante(201915059, "Karen Hurtarte", 20, "7 calle 10-02 zona 1", 24400101, "karen.hurtarte@gmail.com", "Ingenieria en Sistemas", "Programador Jr.")
e3 = estudiante(201915061, "Luis Mendez", 20, "8 calle 10-02 zona 1", 24400101, "luis.mendez@gmail.com", "Ingenieria en Sistemas", "Programador Jr.")

lista_e = lista_enlazada()
lista_e.insertar(e1)
lista_e.insertar(e2)
lista_e.insertar(e3)

lista_e.recorrer()

lista_e.eliminar(201915059)
lista_e.recorrer()

lista_e.eliminar(201915060)
lista_e.recorrer()
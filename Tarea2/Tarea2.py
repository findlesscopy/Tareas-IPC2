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

class lista_circular:
  def __init__(self):
    self.primero = None

  def insertar(self, estudiante):
    if self.primero is None:
      self.primero = nodo(estudiante=estudiante)
      self.primero.siguiente = self.primero
    else:
      actual = nodo(estudiante=estudiante, siguiente=self.primero.siguiente)
      self.primero.siguiente = actual
  def recorrer(self):
    if self.primero is None:
      return
    actual = self.primero
    print("carnet: ", actual.estudiante.carnet,"nombre: ", actual.estudiante.nombre, "email: ", actual.estudiante.email, "->")
    while actual.siguiente != self.primero:
      actual = actual.siguiente
      print("carnet: ", actual.estudiante.carnet,"nombre: ", actual.estudiante.nombre, "email: ", actual.estudiante.email, "->")
  
  def eliminar(self, carnet):
    actual = self.primero
    anterior = None
    no_encontrado = False

    while actual and actual.estudiante.carnet != carnet:
      anterior = actual
      actual = actual.siguiente
      if actual == self.primero:
        no_encontrado= True
        break

    if not no_encontrado:
      if anterior is not None:
        anterior.siguiente = actual.siguiente
      else:
        while actual.siguiente != self.primero:
          actual = actual.siguiente
        actual.siguiente = self.primero.siguiente
        self.primero = self.primero.siguiente
  
  def buscar(self,carnet):
    actual = self.primero
    anterior = None
    no_encontrado = False

    while actual and actual.estudiante.carnet == carnet:
      anterior = actual
      actual = actual.siguiente
      if actual == self.primero:
        no_encontrado= True
        break

    if not no_encontrado:
      if anterior is not None:
        anterior.siguiente != actual.siguiente
      else:
        while actual.siguiente != self.primero:
          actual = actual.siguiente
        actual.siguiente = self.primero.siguiente
        self.primero = self.primero.siguiente

e1 = estudiante(201915060, "Gerson Ortiz", 20, "9 calle 10-02 zona 1", 24400101, "gerson.ortiz@gmail.com", "Ingenieria en Sistemas", "Programador Jr.")
e2 = estudiante(201915059, "Karen Hurtarte", 20, "7 calle 10-02 zona 1", 24400101, "karen.hurtarte@gmail.com", "Ingenieria en Sistemas", "Programador Jr.")
e3 = estudiante(201915061, "Luis Mendez", 20, "8 calle 10-02 zona 1", 24400101, "luis.mendez@gmail.com", "Ingenieria en Sistemas", "Programador Jr.")

lista_c = lista_circular()
lista_c.insertar(e1)
lista_c.insertar(e2)
lista_c.insertar(e3)

lista_c.recorrer()

lista_c.eliminar(201915059)
lista_c.recorrer()

lista_c.buscar(201915059)
lista_c.recorrer()
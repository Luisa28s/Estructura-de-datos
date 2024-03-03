import sys
class Nodo:
    def __init__(self, sexo, edad):
        self.sexo = sexo
        self.edad = edad
        self.li = None
        self.ld = None

class ListaLD:
    def __init__(self):
        self.primero = None  # Derecho
        self.ultimo = None  # Izquierdo
        
    def estaVacia(self):
        return self.primero is None
    
    def insertar(self, sexo, edad):
        nuevo_nodo = Nodo(sexo, edad)
        if self.estaVacia():
            self.primero = nuevo_nodo
            self.ultimo = nuevo_nodo
        else:
            self.ultimo.ld = nuevo_nodo
            nuevo_nodo.li = self.ultimo
            self.ultimo = nuevo_nodo
    
    def mostrar(self):
        actu=self.primero
        while actu is not None:
            print(f"Sexo: ", actu.sexo, "Edad: ", actu.edad, end="-->")
            actu = actu.ld

    def promedioH(self):
        sumaEdad = 0
        cantidadHombres = 0
        actu = self.primero
        while actu:
            if actu.sexo == 1: 
                sumaEdad += actu.edad
                cantidadHombres += 1
            actu = actu.ld
        if cantidadHombres == 0:
            print("No hay hombres en la lista")
            return 0
        else:
            return sumaEdad / cantidadHombres
        
    def promedioM(self):
        sumaEdadM = 0
        cantidadMujeres = 0
        actu = self.primero
        while actu:
            if actu.sexo == 2: 
                sumaEdadM += actu.edad
                cantidadMujeres += 1
            actu = actu.ld
        if cantidadMujeres == 0:
            print("No hay mujeres en la lista")
            return 0
        else:
            return sumaEdadM / cantidadMujeres
            
        
lista = ListaLD()
opc=0
while True:
    print()
    print("-------------MENÚ-------------")
    print("        1. Crear lista    ")
    print("   2. Promedio edad hombres ")
    print("   3. Promedio edad mujeres")
    print("          4. Salir")
    print("-------------------------------")
    opc=int(input("Elija una opción: "))
    
    if opc == 1:
        cantidad = int(input("Ingrese la cantidad de personas a agregar a la lista: "))
        for i in range(cantidad):
            sexo = int(input("Ingrese el sexo (1. Hombre o 2. Mujer): "))
            if sexo == 1 or sexo == 2: 
                edad = int(input("Ingrese la edad: "))
                lista.insertar(sexo, edad)
            else:
                print("Error al seleccionar opción")  #No le agregué un sys.exit() para permitir que el usuario ingrese una opción válida
        print()
    
    elif opc == 2:
        print("El promedio es de edad de los hombres es de ----> ", lista.promedioH())
    elif opc== 3:
        print("El promedio es de edad de las mujeres es de ----> ", lista.promedioM())
    elif opc==4:
        print("Salida del programa")
        sys.exit()
    else:
        print("Error al seleccionar opción") #No le agregué un sys.exit() para permitir que el usuario ingrese una opción válida
        
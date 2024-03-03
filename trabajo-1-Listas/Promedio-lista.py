import sys

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.liga = None
        
class listaSL:
    def __init__(self):
        self.pri = None
        
    def mostrar_lst(self):
        actual = self.pri
        while actual:
            print(actual.dato, end=" -> ")
            actual = actual.liga
            
    def estaVacia(self):
        return self.pri is None
            
    def insertar(self, dato):
        nodo = Nodo(dato)
        if self.estaVacia() or dato <= self.pri.dato:
            nodo.liga = self.pri
            self.pri = nodo
        else:
            actual = self.pri
            while actual.liga and actual.liga.dato < dato:
                actual = actual.liga
            nodo.liga = actual.liga
            actual.liga = nodo
            
    def suma(self ):
        acum= 0
        actual = self.pri
        while actual:
            if actual.dato%3 == 0:
                acum+=actual.dato
            actual = actual.liga
        print("la suma de los multiplos de 3 es ---> " , acum)
        
    def promedio(self ):
        acum= 0    
        contador = 0
        actual = self.pri
        while actual:
            acum += actual.dato
            contador += 1
            actual = actual.liga

        if contador > 0:
            promedio = acum / contador
            print("El promedio del total de datos guardados es ---> ", promedio)
        else:
            print("La lista está vacía.")
            
    def ins_inicio(self, dato):
        if self.pri == None:
            nodo = Nodo(dato)
            self.pri = nodo
        else:        
            nodo = Nodo(dato)
            nodo.liga = self.pri
            self.pri = nodo
            
    def ins_final(self, dato):
        if self.pri == None:
            nodo = Nodo(dato)
            self.pri = nodo
        else:
            actual = self.pri
            while actual.liga != None:
                actual = actual.liga
            nodo = Nodo(dato)
            actual.liga = nodo

lista = listaSL()
opc = 0

while True:  
    print("1. Crear lista")
    print("2. Mostrar lista")
    print("3. Sumar los multiplos de 3")
    print("4. Mostrar promedio")
    print("5. Salir")
    opc = int(input("Elija una opción: "))
    
    if opc== 1:
        cantidad = int(input("Ingrese la cantidad de datos a guardar: "))
        for i in range(cantidad):
            num = int(input("Ingrese el dato a insertar en la lista: "))
            lista.insertar(num)
            print()
    
    elif opc == 2:
        print("Los datos son ---> ")
        lista.mostrar_lst()
        print()
        
    elif opc == 3:
        lista.suma()
        print()
        
    elif opc==4:
        lista.promedio()
        print()
        
    elif opc == 5:
        print("Salida del programa")
        sys.exit()
        
    else: 
        print("Error, opción incorrecta")
        
            
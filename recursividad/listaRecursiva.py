import sys
def mostrarListaInversa(nodo):
    if nodo is None:
        return []#Retorna una lista vacía 
    else:
        return  mostrarListaInversa(nodo.liga) + [nodo.dato] 
    
def listaHaciaAdelante(nodo):
    if nodo is None:
        return []
    else:
        return [nodo.dato] + listaHaciaAdelante(nodo.liga)
    
class Nodo:
    def __init__(self,dato):
        self.dato = dato
        self.liga = None
        
class listaSL:
    def __init__(self):
        self.pri = None
        
    def insertar(self, dato):
        nodo = Nodo(dato)
        if self.estaVacia() == True or dato <= self.pri.dato:
            nodo.liga = self.pri
            self.pri = nodo
        else:
            actual = self.pri
            while actual.liga != None and actual.liga.dato < dato:
                actual = actual.liga
            nodo.liga = actual.liga
            actual.liga = nodo
        
    def estaVacia(self):
        return self.pri == None

#Colores de consola
quitarColor = '\u001B[0m'
colorRosa = '\u001B[1;35m'
colorVerde = '\u001B[36m'
colorRojo = '\u001B[31m'

lista=listaSL()
opc=0
while opc != 4:
    print(colorRosa+"----------------MENU-----------------"+quitarColor)
    print("           1. Crear lista            ")
    print("    2. Ver lista hacia adelante      ")
    print("      3. Ver lista hacia atrás       ")
    print("              4. Salir               ")
    print("-------------------------------------")
    opc = int(input(colorRosa+"Seleccione una opción: "+quitarColor))
    print()
    
    if opc == 1:
        cantidad=int(input("Ingrese la cantidad de datos a guardar en la lista: "))
        for i in range(cantidad):
            num=int(input(f"Ingrese el dato {i+1}: "))
            lista.insertar(num)
            print()
            
    elif opc == 2:
        if lista.estaVacia():
            print(colorRojo+"Error. La lista no contiene datos aún"+quitarColor)
        else:
            print(colorVerde+"Lista hacia adelante: "+quitarColor,listaHaciaAdelante(lista.pri))
        print()
        
    elif opc == 3:
        if lista.estaVacia():
            print(colorRojo+"Error. La lista no contiene datos aún"+quitarColor)
        else:
            print(colorVerde+"Lista hacia atrás: " +quitarColor,mostrarListaInversa(lista.pri))
        print()
        
    elif opc == 4:
        print("Salida del programa")
        sys.exit()
        
    else:
        print(colorRojo+"Error: Opción no válida. Por favor ingrese una opción válida "+quitarColor)
            
    
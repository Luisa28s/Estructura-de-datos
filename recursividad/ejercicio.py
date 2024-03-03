import sys
def suma(array, n):
    if n <= 0:
        return 0
    else:
        return array[n - 1] + suma(array, n - 1)
        
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
        
    def mostrarPrincipio(self):
        actual = self.pri
        while actual != None:
            print(actual.dato, end=" -> ")
            actual = actual.liga
        print()
            
    def mostrarFinal(self):
        if self.pri is None:
            print("La lista está vacía")
            return
        
        actual = self.pri #El metodo inicializa un puntero "actual" al primer nodo "self.pri " 
        while actual.liga != None: #Este bucle recorre la lista hasta llegar al ultimo nodo 
            actual = actual.liga 
        while actual != None:
             #Imprimira los datos de los nodos en orden inverso 
            actual = self.accesoNodoAnt(actual) 
            print(actual.dato, end=" -> ")
        print() #El bucle termina cuando actual se convierte en none

    def accesoNodoAnt(self, nodo): #Método para poder acceder al nodo anterior. Recibe el nodo al que quermos acceder
        actual = self.pri #Recorre la lista desde el primer nodo (self.pri), hasta que encuentra el nodo dado
        anterior = None 
        while actual != nodo:  
            anterior = actual
            actual = actual.liga
        return anterior
            
    def estaVacia(self):
        return self.pri == None

lista=listaSL()
opc=0
array=[]
print()

while True:
    print("----------------MENÚ--------------------")
    print("         1. Crear arreglo")
    print("           2. Ver la suma ")
    print("      3. Mostrar arreglo hacia adelante")
    print("       4. Mostrar arreglo hacia atrás")
    print("              5. Salir                  ")
    print("----------------------------------------")
    opc=int(input("Elija una opción --> "))
    print()
    
    if opc == 1:
        cantidad = int(input("Ingrese la cantidad de datos a guardar: "))
        for i in range(cantidad):
            dato = int(input(f"Ingrese el dato {i+1}: "))
            lista.insertar(dato)
            array.append(dato)  
            print()
            
    elif opc == 2:
        if lista.estaVacia():
            print("El arreglo está vacío.")
        else:
            long = len(array)
            print("La suma del arreglo es --> ", suma(array, long))
            print()
            
    elif opc == 3:
        print("Arreglo hacia adelante ")
        lista.mostrarPrincipio()
        print()
        
    elif opc == 4: 
        print("Arreglo hacia atrás ")
        lista.mostrarFinal()
        print()
        
    elif opc == 5:
        print("Salida del programa")
        sys.exit()
    
    else:
        print("Error al seleccionar opción")
        print()
        
    
            
            
    
            
            
            
import sys
def suma(vec, ind=0):
    if ind >= len(vec):
        return 0
    else:
        return vec[ind] + suma(vec,ind + 1)
    
#Colores de consola
quitarColor = '\u001B[0m'
colorAzul = '\u001B[36m'
colorVerde = '\u001B[1;32m'
colorRojo = '\u001B[31m'
opc=0

while opc != 3:
    print(colorAzul+"-----------MENU----------"+quitarColor)
    print("     1. Crear vector     ")
    print("   2. Suma del vector    ")
    print("        3. Salir         ")
    print("-------------------------")
    opc = int(input(colorAzul+"Ingrese una opcion: "+quitarColor))
    print()
    
    if opc==1:
        cantidad = int(input("Ingrese la cantidad de datos a guardar -> "))
        print()
        vector = [0] * cantidad #El vector será igual a la cantidad de datos que ingrese el usuario
        if cantidad <= 0:
            print(colorRojo+"Error: La cantidad de datos debe ser un número positivo mayor que cero"+quitarColor)
        else:
            for i in range(cantidad):
                dato=int(input(f"Ingrese el dato {i+1}: "))
                vector[i] = dato #Los datos se irán guardando en el vector desde la posición 0
                print()
                
    elif opc==2:
        result = suma(vector) 
        print(colorVerde+f"El resultado de la suma es {result} "+quitarColor)
        print()

    elif opc ==3:
        print("Salida del programa")
        sys.exit()
        
    else:
        print(colorRojo+"Error: Opción no válida. Por favor ingrese una opción válida "+quitarColor)
        
    
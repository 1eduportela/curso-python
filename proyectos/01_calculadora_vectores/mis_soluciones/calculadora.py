import math

def calculadora():
    i=0
    contador=0
    while True:
        i=mostrar_menu()
        
        if i=="1":
            x=float(input("Componente x del vector:..."))
            y=float(input("Componente y del vector:..."))
            print(f"La norma del vector dado es:...{norma(x,y):.2f}")
            contador+=1
        elif i=="2":
            x1=float(input("Componente x del primer vector:..."))
            y1=float(input("Componente y del priomer vector:..."))
            x2=float(input("Componente x del segundo vector:..."))
            y2=float(input("Componente y del segundo vector:..."))
            print(f"El producto escalar de los vectores dados es:...{producto_escalar(x1,y1,x2,y2):.2f}")
            contador+=1
        elif i=="3":
            x1=float(input("Componente x del primer vector:..."))
            y1=float(input("Componente y del priomer vector:..."))
            x2=float(input("Componente x del segundo vector:..."))
            y2=float(input("Componente y del segundo vector:..."))
            resultado = angulo(x1, y1, x2, y2)
            if resultado is None:
                print("Vector cero")    
            else:
                print(f"El angulo de los vectores dados es:...{resultado:.2f}")
            contador+=1
        elif i=="4":
            x1=float(input("Componente x del primer vector:..."))
            y1=float(input("Componente y del priomer vector:..."))
            x2=float(input("Componente x del segundo vector:..."))
            y2=float(input("Componente y del segundo vector:..."))
            print(posición_relativa(x1,y1,x2,y2))
            contador+=1
        elif i=="5":
            print("Gracias por usar mi cacluladora")
            if contador>=2 or contador==0:
                print(f"Has hecho {contador} operaciones")
            else:
                print(f"Has hecho {contador} operacion")
            break
        else: 
            print("Valor no valido")  

def producto_escalar(x1,y1,x2,y2):
    """Producto escalar de dos vectores"""
    return x1*x2+y1*y2

def norma(x,y):
    """Norma de un vector"""
    return math.sqrt(x**2 + y**2)

def angulo(x1,y1,x2,y2):
    """Devuelve el angulo en grados entre dos vectores"""
    if (x1==0 and y1==0) or (x2==0 and y2==0):
        return None
    else:
        arcoseno=math.acos(producto_escalar(x1,y1,x2,y2) / ((norma(x1,y1)*norma(x2,y2))))
        return math.degrees(arcoseno)

def posición_relativa(x1,y1,x2,y2):
    """Devuelve la posición relativa entre dos vectores dados"""
    if (x1==0 and y1==0) or (x2==0 and y2==0):
        return "Vector cero"
    elif producto_escalar(x1,y1,x2,y2)==0:
        return "Ortogonales"
    elif x1*y2-x2*y1==0:
        return "Paralelos"
    else:
        return "Ninguna"

def mostrar_menu():
    print("=== Calculadora de vectores ===")
    print("1. Norma de un vector")
    print("2. Producto escalar")
    print("3. Ángulo entre dos vectores")
    print("4. Posición relativa")
    print("5. Salir")
    return input("Elige una opción:...")

calculadora()
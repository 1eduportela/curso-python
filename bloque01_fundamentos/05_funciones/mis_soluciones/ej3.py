import math                 

math.acos(0)                
math.degrees(math.pi)  

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

print(producto_escalar(1, 2, 3, 4))
print(norma(3, 4))
print(angulo(1, 0, 0, 1))
print(angulo(2, 1, 1, 3))
print(angulo(3, 4, 6, 8))
print(angulo(1, 0, -1, 0))
print(angulo(0, 0, 1, 1))
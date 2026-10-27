print("Te voy a pedir los valores para construir y resolver un sistema de ecuaciones:...")

a = float(input("a?"))
b = float(input("b?"))
c = float(input("c?"))
d = float(input("d?"))
e = float(input("e?"))
f = float(input("f?"))

det = a*d - b*c

if det == 0:
    print("El sistema no tiene solución única")
else:
    x = (e*d - b*f) / det
    y = (a*f - e*c) / det

    print(f"La solcuión al sistema es ({x},{y})")
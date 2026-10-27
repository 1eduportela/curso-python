# | Sistema | a, b, c, d, e, f | Salida esperada |
# |---|---|---|
# | 2x + y = 5; x − y = 1 | 2, 1, 1, -1, 5, 1 | x = 2.00, y = 1.00 |
# | 3x = 6; 2y = 3 | 3, 0, 0, 2, 6, 3 | x = 2.00, y = 1.50 |
# | x + 2y = 4; 2x + 4y = 8 | 1, 2, 2, 4, 4, 8 | El sistema no tiene solución única |

print("Te voy a pedir los valores de a, b, c, d, e y f para construir un sistema de ecuaciones (a·x + b·y = e, c·x + d·y = f) y encontrar la solución:...")

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
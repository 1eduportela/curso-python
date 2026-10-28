# El producto de dos matrices 2×2 es:

# ```text
# | p  q |   | a  b |   | p·a + q·c   p·b + q·d |
# | r  s | · | c  d | = | r·a + s·c   r·b + s·d |
# ```

# Muestra el resultado en dos líneas, una por fila, con los números separados por un espacio.

# | a, b, c, d | n | Salida esperada |
# |---|---|---|
# | 1, 2, 3, 4 | 1 | `1 2` / `3 4` |
# | 1, 2, 3, 4 | 2 | `7 10` / `15 22` |
# | 2, 0, 0, 3 | 3 | `8 0` / `0 27` |
# | 1, 1, 1, 0 | 5 | `8 5` / `5 3` |

print("Escribe los valores de p, q, r y s para una matriz y Aⁿ = A · A · … · A:...")

p = int(input("p:..."))
q = int(input("q:..."))
r = int(input("r:..."))
s = int(input("s:..."))
n = int(input("n:..."))

a = p
b = q
c = r
d = s


for i in range(1,n,1):
    x = p*a + q*c
    y = p*b + q*d
    z = r*a + s*c
    w = r*b + s*d
    a = x
    b = y
    c = z
    d = w

print(f"| {p},{q},{r},{s} | {n} | `{a} {b}` / `{c} {d}` |")

# Lección 04 · Bucles
# Ejecútalo DESPUÉS de hacer la predicción de leccion.md.

# --- while ---
cuenta = 3
while cuenta > 0:
    print(cuenta)          # 3, 2, 1
    cuenta -= 1
print("¡Despegue!")

# --- for con range ---
for i in range(4):
    print(i, end=" ")      # 0 1 2 3
print()

for i in range(2, 11, 2):
    print(i, end=" ")      # 2 4 6 8 10
print()

for i in range(5, 0, -1):
    print(i, end=" ")      # 5 4 3 2 1
print()

# --- Recorrer un texto ---
vocales = 0
for letra in "murciélago":
    if letra in "aeiouáéíóú":   # "in" comprueba si está dentro del texto
        vocales += 1
print(f"Vocales: {vocales}")     # Vocales: 5

# --- break: salir al encontrar lo que buscas ---
for n in range(1, 100):
    if n * n > 50:
        print(f"El primer número cuyo cuadrado supera 50 es {n}")   # 8
        break

# --- continue: saltar vueltas ---
for n in range(1, 11):
    if n % 3 != 0:
        continue
    print(n, end=" ")      # 3 6 9
print()

# --- Acumulador ---
suma = 0
for i in range(1, 101):
    suma += i
print(suma)                # 5050

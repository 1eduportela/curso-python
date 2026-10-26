# Lección 02 · Operadores
# Ejecútalo DESPUÉS de hacer la predicción de leccion.md.

# --- Aritméticos ---
a = 9
b = 4
print(a + b)       # 13
print(a - b)       # 5
print(a * b)       # 36
print(a / b)       # 2.25 (siempre float)
print(a // b)      # 2 (división entera)
print(a % b)       # 1 (resto)
print(a ** 2)      # 81 (potencia)
print(16 ** 0.5)   # 4.0 (raíz cuadrada)

# --- Asignación compuesta (no existe ++) ---
contador = 0
contador += 1
contador *= 5
print(contador)    # 5

# --- Comparación ---
nota = 7.5
print(nota >= 5)            # True
print(0 <= nota <= 10)      # True (comparación encadenada)
print("hola" == "hola")     # True (compara el contenido)

# --- Lógicos ---
edad = 20
tiene_carnet = True
print(edad >= 18 and tiene_carnet)      # True
print(edad < 18 or not tiene_carnet)    # False

# --- Mostrar decimales ---
total = 19.99 * 7
print(total)                  # 139.92999999999998
print(f"{total:.2f} euros")   # 139.93 euros

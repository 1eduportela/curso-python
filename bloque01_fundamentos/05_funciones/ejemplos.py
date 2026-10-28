# Lección 05 · Funciones
# Ejecútalo DESPUÉS de hacer la predicción de leccion.md.


# --- Función básica con docstring y anotaciones ---
def area_rectangulo(base: float, altura: float) -> float:
    """Devuelve el área de un rectángulo."""
    return base * altura


print(area_rectangulo(3, 4))        # 12
print(area_rectangulo(2.5, 2))      # 5.0


# --- return frente a print ---
def suma_print(a, b):
    print(a + b)


def suma_return(a, b):
    return a + b


x = suma_print(2, 3)     # muestra 5
print(x)                 # None
y = suma_return(2, 3)    # no muestra nada
print(y * 10)            # 50: el valor devuelto se puede seguir usando


# --- return dentro de un bucle: sale al momento ---
def primer_multiplo(n, desde):
    """Devuelve el primer múltiplo de n que sea mayor o igual que desde."""
    numero = desde
    while True:                  # bucle "infinito"...
        if numero % n == 0:
            return numero        # ...del que se sale con return
        numero += 1


print(primer_multiplo(7, 50))    # 56


# --- Parámetros con valor por defecto ---
def saludar(nombre, saludo="Hola"):
    return f"{saludo}, {nombre}"


print(saludar("Edu"))                       # Hola, Edu
print(saludar("Edu", "Buenas"))             # Buenas, Edu
print(saludar(saludo="Ey", nombre="Edu"))   # Ey, Edu


# --- Funciones que usan otras funciones ---
def es_par(n):
    return n % 2 == 0


def contar_pares(hasta):
    """Cuenta los números pares entre 1 y hasta, ambos incluidos."""
    cuenta = 0
    for i in range(1, hasta + 1):
        if es_par(i):
            cuenta += 1
    return cuenta


print(contar_pares(10))   # 5

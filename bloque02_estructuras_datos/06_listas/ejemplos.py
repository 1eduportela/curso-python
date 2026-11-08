# Lección 06 · Listas
# Ejecútalo DESPUÉS de hacer la predicción de leccion.md.

# --- Crear e indexar ---
dias = ["lunes", "martes", "miércoles", "jueves", "viernes"]
print(len(dias))      # 5
print(dias[0])        # lunes
print(dias[-1])       # viernes

# --- Rebanadas ---
print(dias[1:4])      # ['martes', 'miércoles', 'jueves']
print(dias[:2])       # ['lunes', 'martes']
print(dias[::-1])     # al revés

# --- Modificar ---
dias.append("sábado")
dias.remove("miércoles")
print(dias)           # ['lunes', 'martes', 'jueves', 'viernes', 'sábado']

# --- Construir una lista nueva con un bucle (patrón muy habitual) ---
temperaturas = [18, 25, 31, 22, 35, 28]
calurosos = []
for t in temperaturas:
    if t >= 30:
        calurosos.append(t)
print(calurosos)      # [31, 35]

# --- Funciones integradas ---
print(sum(temperaturas) / len(temperaturas))   # 26.5 (la media)
print(max(temperaturas), min(temperaturas))    # 35 18
print(sorted(temperaturas))                    # [18, 22, 25, 28, 31, 35]

# --- Asignar no es copiar ---
original = [1, 2, 3]
alias = original
copia = original.copy()
alias.append(99)
print(original)       # [1, 2, 3, 99]: alias y original son la misma lista
print(copia)          # [1, 2, 3]: la copia no se entera

# --- Una función que recibe y devuelve listas ---
def dobles(lista):
    """Devuelve una lista nueva con cada elemento multiplicado por 2."""
    resultado = []
    for x in lista:
        resultado.append(2 * x)
    return resultado

print(dobles([1, 2, 3]))   # [2, 4, 6]

# --- Listas de listas: una matriz ---
A = [[1, 2, 3],
     [4, 5, 6]]
print(len(A), len(A[0]))   # 2 3 (filas y columnas)
print(A[1][2])             # 6
for fila in A:
    print(fila)            # [1, 2, 3] y luego [4, 5, 6]

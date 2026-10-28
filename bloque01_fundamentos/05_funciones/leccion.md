# Lección 05 · Funciones

## 🔁 Repaso de la 04

Apúntalo en `mis_soluciones/prediccion.md` sin ejecutarlo. Fíjate bien en la sangría.

```python
for i in range(2, 9, 3):
    print(i)

k = 10
while k > 3:
    k = k // 2
    print(k)
```

## Definir una función

```python
def area_rectangulo(base, altura):
    return base * altura

print(area_rectangulo(3, 4))   # 12
```

Diferencias con Java:

- Se define con `def`, sin tipo de retorno ni tipos en los parámetros.
- No hace falta ninguna clase ni `static`: la función vive suelta en el archivo.
- Tiene que estar definida **antes** de llamarla, porque Python ejecuta el archivo de arriba abajo.

## `return` frente a `print`

La diferencia más importante de la lección:

- `print` **muestra** algo en pantalla.
- `return` **devuelve** un valor a quien llamó a la función, que puede guardarlo o usarlo.

Una función sin `return` devuelve `None`: es el equivalente al `void` de Java.

```python
def suma_print(a, b):
    print(a + b)

def suma_return(a, b):
    return a + b

x = suma_print(2, 3)    # muestra 5, pero x vale None
y = suma_return(2, 3)   # no muestra nada, y vale 5
```

Regla de oro: **las funciones calculan y devuelven; los `input` y los `print` van fuera.**
Así puedes reutilizar la función en cualquier sitio.

`return` termina la función al instante, aunque esté dentro de un bucle.

## Parámetros con valor por defecto

```python
def saludar(nombre, saludo="Hola"):
    return f"{saludo}, {nombre}"

print(saludar("Edu"))                     # Hola, Edu
print(saludar("Edu", "Buenas"))           # Buenas, Edu
print(saludar(saludo="Ey", nombre="Edu")) # Ey, Edu (por nombre, el orden da igual)
```

En Java harías sobrecarga de métodos; en Python se usan valores por defecto.
Los parámetros con valor por defecto van siempre al final.

## Variables locales

Lo que se crea dentro de una función solo existe dentro de ella:

```python
def calcular():
    resultado = 42

calcular()
print(resultado)   # NameError: name 'resultado' is not defined
```

## Docstrings y anotaciones de tipo

```python
def area_rectangulo(base: float, altura: float) -> float:
    """Devuelve el área de un rectángulo."""
    return base * altura
```

- El **docstring** es un texto entre triples comillas en la primera línea de la función.
  Explica qué hace, y VS Code lo muestra al pasar el ratón por encima de la llamada.
- Las **anotaciones** `: float` y `-> float` son opcionales y Python **no las comprueba** al ejecutar:
  son documentación, aunque VS Code las usa para avisarte. Viniendo de Java, te resultarán naturales.

## 🔮 Predicción

Añádela a `mis_soluciones/prediccion.md` antes de ejecutar nada. ¿Qué imprime?

```python
def doble(x):
    return x * 2

def saludo(nombre):
    print(f"Hola, {nombre}")

print(doble(4))
print(doble("ab"))
r = saludo("Edu")
print(r)

def potencia(base, exponente=2):
    return base ** exponente

print(potencia(3))
print(potencia(2, 5))
print(potencia(exponente=3, base=2))

def primero_par(n):
    for i in range(1, n):
        if i % 2 == 0:
            return i
    return -1

print(primero_par(10))
print(primero_par(2))
```

Escribe **una línea por cada línea que se imprime**.

## Ejemplos

Después de la predicción, ejecuta [`ejemplos.py`](ejemplos.py).

## Siguiente paso

Los ejercicios están en [`ejercicios.md`](ejercicios.md).

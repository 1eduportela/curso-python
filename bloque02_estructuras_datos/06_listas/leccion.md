# Lección 06 · Listas

## 🔁 Repaso del bloque 1

Apúntalo en `mis_soluciones/prediccion.md` sin ejecutarlo:

```python
def f(n):
    total = 0
    for i in range(n):
        total += i
    return total

print(f(4))
print(f(1))
```

## Qué es una lista

Una secuencia **ordenada** y **modificable** de valores. Es lo más parecido al `ArrayList` de Java,
pero viene integrada en el lenguaje, con su propia sintaxis:

```python
notas = [7.5, 4.0, 9.2]
vacia = []
mezcla = [1, "hola", True]   # se puede, aunque lo normal es que todos sean del mismo tipo
```

- No tiene tamaño fijo: crece y encoge sola.
- `len(notas)` te da cuántos elementos tiene (en Java, `.size()`).

## Índices

Empiezan en 0, como en Java. La novedad son los **índices negativos**, que cuentan desde el final:

```python
letras = ["a", "b", "c", "d"]
print(letras[0])    # a
print(letras[-1])   # d (el último)
print(letras[-2])   # c
letras[1] = "B"     # se pueden modificar
print(letras[10])   # IndexError: list index out of range
```

## Rebanadas (slicing)

`lista[inicio:fin]` te da una **nueva lista** con un trozo. El `fin` **no se incluye**,
igual que en `range`:

```python
letras = ["a", "b", "c", "d", "e"]
print(letras[1:3])    # ['b', 'c']
print(letras[:2])     # ['a', 'b']       (desde el principio)
print(letras[2:])     # ['c', 'd', 'e']  (hasta el final)
print(letras[::-1])   # ['e', 'd', 'c', 'b', 'a'] (paso -1: al revés)
```

## Añadir, quitar y buscar

```python
frutas = ["pera", "uva"]
frutas.append("kiwi")        # al final: ['pera', 'uva', 'kiwi']
frutas.insert(0, "higo")     # en una posición: ['higo', 'pera', 'uva', 'kiwi']
frutas.remove("uva")         # por valor: ['higo', 'pera', 'kiwi']
ultima = frutas.pop()        # quita y devuelve el último: 'kiwi'
print("pera" in frutas)      # True (¿está dentro?)
```

## Recorrer una lista

```python
for fruta in frutas:          # el for de Python brilla aquí
    print(fruta)

for i in range(len(frutas)):  # si además necesitas la posición
    print(i, frutas[i])
```

## Funciones útiles

```python
numeros = [4, 1, 7, 3]
print(sum(numeros), min(numeros), max(numeros))   # 15 1 7
print(sorted(numeros))   # [1, 3, 4, 7]: devuelve una lista NUEVA ordenada
numeros.sort()           # ordena la propia lista (y devuelve None)
```

¿Ves ahora por qué no debías llamar `sum` o `min` a tus variables? 😉

## ⚠️ Asignar no es copiar

Una variable guarda una **referencia** a la lista, como pasa con los objetos en Java:

```python
a = [1, 2, 3]
b = a          # b y a son LA MISMA lista
b.append(4)
print(a)       # [1, 2, 3, 4]

c = a.copy()   # una copia independiente
```

## Listas de listas

Una lista puede contener otras listas. Así se representa una matriz, fila a fila:

```python
A = [[1, 2],
     [3, 4]]
print(A[0])      # [1, 2]  (la primera fila)
print(A[1][0])   # 3       (fila 1, columna 0)
```

En el bloque 6 NumPy lo hará mucho mejor, pero entender esto primero te ayudará.

## 🔮 Predicción

Añádela a `mis_soluciones/prediccion.md` antes de ejecutar nada. **Una línea por cada `print`.**

```python
numeros = [10, 20, 30, 40, 50]
print(numeros[1])
print(numeros[-1])
print(numeros[1:3])
print(numeros[:2])
print(len(numeros))

numeros.append(60)
print(numeros[-2:])

a = [1, 2, 3]
b = a
b.append(4)
print(a)

c = a.copy()
c.append(5)
print(a)
print(sum(a), max(a))
print(3 in a, 7 in a)
```

## Ejemplos

Después de la predicción, ejecuta [`ejemplos.py`](ejemplos.py).

## Siguiente paso

Los ejercicios están en [`ejercicios.md`](ejercicios.md).

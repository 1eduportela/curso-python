# Lección 04 · Bucles

## 🔁 Repaso de la 03

Apúntalo en `mis_soluciones/prediccion.md` sin ejecutarlo:

```python
x = 15
if x > 10:
    print("A")
if x > 12:
    print("B")
elif x > 14:
    print("C")
else:
    print("D")
```

## `while`

Igual que en Java, pero con la sintaxis de los `if`: sin paréntesis, con `:` y sangría.

```python
cuenta = 3
while cuenta > 0:
    print(cuenta)
    cuenta -= 1      # recuerda: no existe cuenta--
print("¡Despegue!")
```

No existe `do-while`. Si te sale un bucle infinito, en la terminal se para con `Ctrl+C`.

## `for` y `range()`

Aquí está el gran cambio. El `for` de Python no tiene inicialización, condición e incremento:
**recorre los elementos de algo**, como el `for (int x : array)` de Java. Para contar se usa `range()`:

| Java | Python | Valores |
|---|---|---|
| `for (int i = 0; i < 5; i++)` | `for i in range(5):` | 0, 1, 2, 3, 4 |
| `for (int i = 2; i < 8; i++)` | `for i in range(2, 8):` | 2, 3, 4, 5, 6, 7 |
| `for (int i = 0; i < 10; i += 3)` | `for i in range(0, 10, 3):` | 0, 3, 6, 9 |
| `for (int i = 5; i > 0; i--)` | `for i in range(5, 0, -1):` | 5, 4, 3, 2, 1 |

Regla de oro: `range(inicio, fin, paso)` **nunca incluye el `fin`**.

Un texto también se puede recorrer, carácter a carácter:

```python
for letra in "hola":
    print(letra)     # h, o, l, a (una por línea)
```

¿Cuál usar? `for` cuando sabes cuántas vueltas das o qué recorres; `while` cuando depende de algo
que no sabes de antemano (por ejemplo, hasta que el usuario escriba algo válido).

## `break` y `continue`

Funcionan igual que en Java: `break` sale del bucle y `continue` salta a la siguiente vuelta.

## El patrón acumulador

Muy habitual: una variable que se inicializa **antes** del bucle y se actualiza dentro.

```python
suma = 0
for i in range(1, 101):
    suma += i
print(suma)   # 5050
```

## Imprimir en la misma línea

`print` añade un salto de línea al final. Con `end` lo cambias:

```python
for i in range(3):
    print(i, end=" ")   # 0 1 2
print()                 # salto de línea para terminar
```

## 🔮 Predicción

Añádela a `mis_soluciones/prediccion.md` antes de ejecutar nada. ¿Qué imprime?

```python
for i in range(3):
    print(i)

for i in range(10, 0, -3):
    print(i)

n = 5
while n > 0:
    n -= 2
print(n)

for letra in "Python":
    if letra == "h":
        break
    print(letra)

total = 0
for i in range(1, 5):
    if i % 2 == 0:
        continue
    total += i
print(total)
```

## Ejemplos

Después de la predicción, ejecuta [`ejemplos.py`](ejemplos.py).

## Siguiente paso

Los ejercicios están en [`ejercicios.md`](ejercicios.md).

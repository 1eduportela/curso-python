# Lección 02 · Operadores

## 🔁 Repaso de la 01

Antes de empezar, ¿qué imprime esto? Apúntalo en `mis_soluciones/prediccion.md` sin ejecutarlo.

```python
x = "3"
print(x * 2 + "1")
print(int(x) * 2 + 1)
```

## Aritméticos

| Operador | Significado | Ejemplo | Resultado |
|---|---|---|---|
| `+` | suma | `9 + 4` | `13` |
| `-` | resta | `9 - 4` | `5` |
| `*` | multiplicación | `9 * 4` | `36` |
| `/` | división | `9 / 4` | `2.25` |
| `//` | división entera (redondea hacia abajo) | `9 // 4` | `2` |
| `%` | resto | `9 % 4` | `1` |
| `**` | potencia | `9 ** 2` | `81` |

Diferencias con Java:

- `/` **siempre** devuelve `float`, aunque dividas dos `int`. En Java `9 / 4` da `2`; en Python, `2.25`.
  Si quieres la división entera, usa `//`.
- `**` es la potencia (en Java, `Math.pow`) y se evalúa antes que casi todo lo demás.
  Truco: `x ** 0.5` es la raíz cuadrada.
- No existen `++` ni `--`. Se usa la asignación compuesta:

```python
contador = 0
contador += 1   # contador = contador + 1
contador *= 5   # también existen -=, /=, //=, %=, **=
```

## Comparación

`==`, `!=`, `<`, `>`, `<=`, `>=` devuelven un `bool`.

- Con textos, `==` compara el **contenido**. En Java tendrías que usar `.equals()`.
- Se pueden encadenar: `0 <= nota <= 10` equivale a `0 <= nota and nota <= 10`.

## Lógicos

| Java | Python |
|---|---|
| `&&` | `and` |
| `\|\|` | `or` |
| `!` | `not` |

```python
edad = 20
tiene_carnet = True
print(edad >= 18 and tiene_carnet)   # True
print(not tiene_carnet)              # False
```

Prioridad: primero `not`, luego `and` y por último `or`. Ante la duda, paréntesis.

## Mostrar decimales con `:.2f`

¿Recuerdas el `139.92999999999998` del ejercicio 3 de la lección anterior? Los `float` no son exactos
(con `double` en Java pasa exactamente lo mismo). Para **mostrar** un número con 2 decimales:

```python
total = 19.99 * 7
print(f"Total: {total:.2f} euros")   # Total: 139.93 euros
```

Solo cambia cómo se muestra: la variable `total` sigue valiendo lo mismo.

## 🔮 Predicción

**Esto** es lo que tienes que predecir (no `ejemplos.py`). Añádelo a `mis_soluciones/prediccion.md`
antes de ejecutarlo. Hay alguna trampa.

```python
print(7 / 2)
print(7 // 2)
print(-7 // 2)
print(7 % 3)
print(10 / 5)
print(-2 ** 2)
print(1 < 5 < 3)
print(not 3 > 2 or 2 > 1)
```

## Ejemplos

Después de la predicción, ejecuta [`ejemplos.py`](ejemplos.py).

## Siguiente paso

Los ejercicios están en [`ejercicios.md`](ejercicios.md).

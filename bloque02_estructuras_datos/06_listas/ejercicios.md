# Ejercicios · Lección 06

Guarda cada ejercicio en `mis_soluciones/` con el nombre indicado.

Las normas de la Lección 05 siguen en pie:

- Funciones con docstring que **no usan `input()` ni `print()`**: reciben y devuelven.
- Pruebas al final del archivo, con el resultado esperado en un comentario.
- **Las funciones no modifican las listas que reciben**: si tienen que devolver una lista, crean una nueva.

Antes de subirlo, compara cada salida con la tabla.

## Ejercicio 1 · Estadísticas de notas (fácil)

Archivo: `mis_soluciones/ej1.py`

Con la lista `notas = [7.5, 4.0, 9.2, 6.8, 5.5, 3.9]`, escribe:

1. `media(lista)`: la media. Si la lista está vacía, devuelve `None`.
2. `aprobados(lista)`: una lista **nueva** con las notas mayores o iguales que 5.
3. `contar_suspensos(lista)`: cuántas notas son menores que 5. Puedes usar `aprobados`.

| Llamada | Resultado esperado |
|---|---|
| `f"{media(notas):.2f}"` | `6.15` |
| `media([])` | `None` |
| `aprobados(notas)` | `[7.5, 9.2, 6.8, 5.5]` |
| `contar_suspensos(notas)` | `2` |
| `notas` (después de todo) | `[7.5, 4.0, 9.2, 6.8, 5.5, 3.9]` (sin cambios) |

## Ejercicio 2 · Vectores de cualquier dimensión (media)

Archivo: `mis_soluciones/ej2.py`

Ahora un vector es una lista: (1, 2, 3) es `[1, 2, 3]`. Capítulos 1 y 6 del Lay.

1. `suma_vectores(u, v)`: devuelve u + v, componente a componente.
2. `escalar_por_vector(k, v)`: devuelve k·v.
3. `producto_escalar(u, v)`: devuelve u · v.
4. `norma(v)`: devuelve ‖v‖. Pista: ‖v‖ = √(v · v).

Si dos vectores no tienen la misma dimensión, `suma_vectores` y `producto_escalar` devuelven `None`.

| Llamada | Resultado esperado |
|---|---|
| `suma_vectores([1, 2, 3], [4, 5, 6])` | `[5, 7, 9]` |
| `escalar_por_vector(2, [1, -1, 0])` | `[2, -2, 0]` |
| `producto_escalar([1, 2, 3], [4, 5, 6])` | `32` |
| `producto_escalar([1, 0, 0, 1], [0, 1, 1, 0])` | `0` |
| `norma([1, 2, 2])` | `3.0` |
| `producto_escalar([1, 2], [1, 2, 3])` | `None` |

Compara con tu calculadora del mini proyecto: ¿cuántas variables `x1, y1, x2, y2` te ahorras?
Y ahora funciona igual en 2, 3 o 100 dimensiones.

## Ejercicio 3 · Matriz por vector (más difícil)

Archivo: `mis_soluciones/ej3.py`

Sección 1.4 del Lay. Una matriz es una lista de filas, y el producto **A·x** es el vector cuyos
elementos son el producto escalar de cada fila de A con x:

```text
| 1  2 |   | 1 |   | 1·1 + 2·1 |   | 3 |
| 3  4 | · | 1 | = | 3·1 + 4·1 | = | 7 |
```

Escribe `matriz_por_vector(A, x)`, reutilizando tu `producto_escalar` del ejercicio 2
(cópialo al archivo; en el bloque 5 veremos cómo importarlo). Si las dimensiones no encajan, devuelve `None`.

| Llamada | Resultado esperado |
|---|---|
| `matriz_por_vector([[1, 2], [3, 4]], [1, 1])` | `[3, 7]` |
| `matriz_por_vector([[1, 0, -1], [2, 1, 0]], [1, 2, 3])` | `[-2, 4]` |
| `matriz_por_vector([[1, 0], [0, 1]], [5, -3])` | `[5, -3]` |
| `matriz_por_vector([[1, 2], [3, 4]], [1, 2, 3])` | `None` |

¿Por qué la tercera fila devuelve el mismo vector? ¿Cómo se llama esa matriz en el Lay?

**Extra (opcional):** el Lay explica que A·x también es una **combinación lineal de las columnas**
de A, con los elementos de x como pesos. Compruébalo con la segunda fila de la tabla usando
`suma_vectores` y `escalar_por_vector`: 1·(1, 2) + 2·(0, 1) + 3·(−1, 0) debería dar `[-2, 4]`.

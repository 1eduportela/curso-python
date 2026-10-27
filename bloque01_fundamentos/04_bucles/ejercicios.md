# Ejercicios · Lección 04

Guarda cada ejercicio en `mis_soluciones/` con el nombre indicado.
Antes de subirlo, **ejecútalo con todas las filas** y comprueba que la salida es **exactamente** la de la tabla.

## Ejercicio 1 · Tabla de multiplicar (fácil)

Archivo: `mis_soluciones/ej1.py`

Pide un número entero y muestra su tabla del 1 al 10.

Entrada `7`, salida esperada:

```text
7 x 1 = 7
7 x 2 = 14
...
7 x 10 = 70
```

## Ejercicio 2 · Suma de dígitos (media)

Archivo: `mis_soluciones/ej2.py`

Pide un número entero positivo y muestra la suma de sus dígitos.
**Sin convertirlo a texto**: solo con `while`, `//` y `%`.

| Entrada | Salida esperada |
|---|---|
| 1234 | 10 |
| 9 | 9 |
| 1000 | 1 |

Pista de partida: ¿qué te da `1234 % 10`? ¿Y `1234 // 10`?

## Ejercicio 3 · Potencia de una matriz 2×2 (más difícil)

Archivo: `mis_soluciones/ej3.py`

Conecta con la sección 2.1 del Lay (multiplicación de matrices). Pide los cuatro números
de una matriz A y un entero n ≥ 1, y muestra Aⁿ = A · A · … · A (n veces).

```text
A = | a  b |
    | c  d |
```

El producto de dos matrices 2×2 es:

```text
| p  q |   | a  b |   | p·a + q·c   p·b + q·d |
| r  s | · | c  d | = | r·a + s·c   r·b + s·d |
```

Muestra el resultado en dos líneas, una por fila, con los números separados por un espacio.

| a, b, c, d | n | Salida esperada |
|---|---|---|
| 1, 2, 3, 4 | 1 | `1 2` / `3 4` |
| 1, 2, 3, 4 | 2 | `7 10` / `15 22` |
| 2, 0, 0, 3 | 3 | `8 0` / `0 27` |
| 1, 1, 1, 0 | 5 | `8 5` / `5 3` |

⚠️ Hay una trampa al actualizar las variables dentro del bucle. Si la fila de n = 2 te sale mal,
piensa en qué valor tiene cada variable en el momento en que la usas.

**Curiosidad:** con la última matriz, prueba n = 6, 7, 8... y mira los números. ¿Te suenan?

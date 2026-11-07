# Mini proyecto 1 · Calculadora de vectores del plano

Cierre del bloque 1. Junta todo lo visto: variables, operadores, condicionales, bucles y funciones.
Además, reutiliza tus funciones del ejercicio 3 de la Lección 05 y conecta con los capítulos 3 y 6 del Lay.

Guarda tu programa en `mis_soluciones/calculadora.py`.

## Qué tiene que hacer

Un programa con menú que se repite hasta que el usuario elige salir:

```text
=== Calculadora de vectores ===
1. Norma de un vector
2. Producto escalar
3. Ángulo entre dos vectores
4. Posición relativa
5. Salir
Elige una opción:
```

| Opción | Pide | Muestra |
|---|---|---|
| 1 | x, y | `Norma: 5.00` |
| 2 | x1, y1, x2, y2 | `Producto escalar: 11.00` |
| 3 | x1, y1, x2, y2 | `Ángulo: 45.00°`, o `El ángulo no está definido (vector cero)` |
| 4 | x1, y1, x2, y2 | `Posición relativa: ortogonales` (o `paralelos`, `ninguna`, `vector cero`) |
| 5 | — | `Has hecho 3 operaciones. ¡Hasta luego!` y termina |
| otra cosa | — | `Opción no válida` y vuelve al menú |

Las coordenadas pueden tener decimales.

## La posición relativa (nuevo)

Para dos vectores **u** = (x1, y1) y **v** = (x2, y2), comprobando en este orden:

1. Si alguno es el vector cero → `vector cero`.
2. Si **u · v = 0** → `ortogonales` (capítulo 6 del Lay).
3. Si **x1·y2 − x2·y1 = 0** → `paralelos`. ¿Te suena? Es el determinante de la matriz que tiene
   **u** y **v** como columnas: vale 0 cuando una columna es múltiplo de la otra (capítulo 3).
4. Si no → `ninguna`.

## Requisitos

- [ ] Funciones de cálculo con docstring que **solo devuelven** (sin `input` ni `print`):
      `norma`, `producto_escalar`, `angulo` y una nueva, `posicion_relativa`, que devuelve el texto.
- [ ] Una función `mostrar_menu()` que imprime el menú. Las funciones de interfaz sí pueden imprimir.
- [ ] El menú se repite con un bucle hasta elegir la opción 5.
- [ ] Una opción no válida (`7`, `hola`, vacío...) **no hace que el programa se rompa**.
      Pista: ¿hace falta convertir la opción a número para compararla?
- [ ] Al salir, muestra cuántas operaciones válidas se han hecho, con el singular correcto:
      `Has hecho 1 operación` frente a `Has hecho 3 operaciones`.
- [ ] Todos los resultados numéricos con 2 decimales.

## Casos de prueba

Pruébalos **todos** antes de subir.

| Opción | Datos | Salida esperada |
|---|---|---|
| 1 | 3, 4 | `Norma: 5.00` |
| 2 | 1, 2, 3, 4 | `Producto escalar: 11.00` |
| 3 | 2, 1, 1, 3 | `Ángulo: 45.00°` |
| 3 | 0, 0, 1, 1 | `El ángulo no está definido (vector cero)` |
| 4 | 1, 2, -2, 1 | `Posición relativa: ortogonales` |
| 4 | 1, 2, 2, 4 | `Posición relativa: paralelos` |
| 4 | 3, -1, -6, 2 | `Posición relativa: paralelos` |
| 4 | 1, 0, 1, 1 | `Posición relativa: ninguna` |
| 4 | 0, 0, 1, 1 | `Posición relativa: vector cero` |
| 7 | — | `Opción no válida` |

## Ejemplo de sesión

```text
=== Calculadora de vectores ===
1. Norma de un vector
2. Producto escalar
3. Ángulo entre dos vectores
4. Posición relativa
5. Salir
Elige una opción: 1
x: 3
y: 4
Norma: 5.00

=== Calculadora de vectores ===
...
Elige una opción: 7
Opción no válida

=== Calculadora de vectores ===
...
Elige una opción: 5
Has hecho 1 operación. ¡Hasta luego!
```

## Notas

- **Comparar decimales con `== 0`:** con números como `0.1` o `0.2`, los `float` no son exactos y
  `== 0` puede fallar por muy poco. Para este proyecto no te preocupes: lo resolveremos bien en NumPy.
- **Sin listas:** todavía no las hemos visto, así que pedirás cada coordenada en su propia variable.
  Cuando lleguen las listas en el bloque 2, verás lo mucho que se simplifica.

## Extra (opcional)

Añade la opción **Proyección escalar de u sobre v**: comp = (u · v) / ‖v‖.
Con u = (2, 1) y v = (1, 3), la salida es `Proyección escalar: 1.58`.

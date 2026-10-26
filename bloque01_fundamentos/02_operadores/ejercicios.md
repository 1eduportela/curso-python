# Ejercicios · Lección 02

Guarda cada ejercicio en `mis_soluciones/` con el nombre indicado.
Antes de subirlo, **ejecútalo** con los valores de prueba y comprueba que sale lo esperado.

## Ejercicio 1 · Norma de un vector (fácil)

Archivo: `mis_soluciones/ej1.py`

La norma (longitud) de un vector **v** = (x, y) del plano es √(x² + y²).
La verás en el capítulo 6 del Lay.

Pide al usuario las dos componentes y muestra la norma con 2 decimales.
No importes nada: hazlo solo con operadores.

| Entrada | Salida esperada |
|---|---|
| (3, 4) | 5.00 |
| (1, 1) | 1.41 |
| (-2, 5.5) | 5.85 |

## Ejercicio 2 · Conversor de segundos (media)

Archivo: `mis_soluciones/ej2.py`

Pide un número entero de segundos y muéstralo en horas, minutos y segundos.

| Entrada | Salida esperada |
|---|---|
| 3725 | 1 h 2 min 5 s |
| 59 | 0 h 0 min 59 s |
| 86399 | 23 h 59 min 59 s |

## Ejercicio 3 · ¿Año bisiesto? (más difícil)

Archivo: `mis_soluciones/ej3.py`

Pide un año y muestra `True` o `False` según sea bisiesto.
Todavía no hemos visto `if`: hazlo con **una sola expresión** de operadores de comparación y lógicos.

La regla: un año es bisiesto si es divisible entre 4, excepto los divisibles entre 100,
salvo que también lo sean entre 400.

| Entrada | Salida esperada |
|---|---|
| 2024 | True |
| 2023 | False |
| 1900 | False |
| 2000 | True |

Añade un comentario explicando por qué tu expresión acierta tanto con 1900 como con 2000.

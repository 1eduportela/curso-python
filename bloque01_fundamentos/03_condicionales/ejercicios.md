# Ejercicios · Lección 03

Guarda cada ejercicio en `mis_soluciones/` con el nombre indicado.
Antes de subirlo, **ejecútalo con todas las filas de la tabla** y comprueba que sale lo esperado.

## Ejercicio 1 · Calificación (fácil)

Archivo: `mis_soluciones/ej1.py`

Pide una nota (puede tener decimales) y muestra su calificación:

- menos de 5: Suspenso
- de 5 a menos de 7: Aprobado
- de 7 a menos de 9: Notable
- de 9 a 10: Sobresaliente
- fuera del rango 0-10: Nota no válida

| Entrada | Salida esperada |
|---|---|
| 4.9 | Suspenso |
| 5 | Aprobado |
| 8.5 | Notable |
| 10 | Sobresaliente |
| 11 | Nota no válida |
| -1 | Nota no válida |

## Ejercicio 2 · Conversor de segundos, versión 2 (media)

Archivo: `mis_soluciones/ej2.py`

Mejora tu conversor de la Lección 02:

- Singular y plural correctos: "1 hora", "2 horas", "1 minuto"...
- Si el número es negativo, muestra `No puede ser negativo` en lugar de convertirlo.

| Entrada | Salida esperada |
|---|---|
| 3725 | 1 hora, 2 minutos y 5 segundos |
| 3661 | 1 hora, 1 minuto y 1 segundo |
| 7322 | 2 horas, 2 minutos y 2 segundos |
| 0 | 0 horas, 0 minutos y 0 segundos |
| -5 | No puede ser negativo |

## Ejercicio 3 · Sistema de ecuaciones 2×2 (más difícil)

Archivo: `mis_soluciones/ej3.py`

Este conecta con los capítulos 1 y 3 del Lay. Un sistema

```text
a·x + b·y = e
c·x + d·y = f
```

tiene solución única si y solo si el determinante de su matriz de coeficientes no es cero:

```text
det = a·d − b·c
```

En ese caso, por la regla de Cramer:

```text
x = (e·d − b·f) / det
y = (a·f − e·c) / det
```

Pide los seis números (pueden tener decimales). Si `det` no es cero, muestra la solución con
2 decimales; si es cero, muestra `El sistema no tiene solución única`.

| Sistema | a, b, c, d, e, f | Salida esperada |
|---|---|---|
| 2x + y = 5; x − y = 1 | 2, 1, 1, -1, 5, 1 | x = 2.00, y = 1.00 |
| 3x = 6; 2y = 3 | 3, 0, 0, 2, 6, 3 | x = 2.00, y = 1.50 |
| x + 2y = 4; 2x + 4y = 8 | 1, 2, 2, 4, 4, 8 | El sistema no tiene solución única |

Comprueba a mano la primera fila sustituyendo x e y en las dos ecuaciones.

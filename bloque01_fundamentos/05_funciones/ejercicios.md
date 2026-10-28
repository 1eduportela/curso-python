# Ejercicios · Lección 05

Guarda cada ejercicio en `mis_soluciones/` con el nombre indicado.

Normas para esta lección:

- Las funciones **no usan `input()` ni `print()`**: reciben parámetros y devuelven con `return`.
- Cada función lleva su **docstring**.
- Al final del archivo, pruébalas con `print` y anota en un comentario el resultado esperado:

```python
# Pruebas
print(es_bisiesto(2024))   # esperado: True
```

Antes de subirlo, **relee el enunciado** y comprueba que cumples cada requisito.

## Ejercicio 1 · Años bisiestos, versión función (fácil)

Archivo: `mis_soluciones/ej1.py`

1. `es_bisiesto(anio)`: devuelve `True` o `False`. Reutiliza tu expresión de la Lección 02.
2. `dias_del_anio(anio)`: devuelve 365 o 366. **Tiene que usar** `es_bisiesto`.

| Llamada | Resultado esperado |
|---|---|
| `es_bisiesto(2024)` | `True` |
| `es_bisiesto(1900)` | `False` |
| `es_bisiesto(2000)` | `True` |
| `dias_del_anio(2023)` | `365` |
| `dias_del_anio(2024)` | `366` |

## Ejercicio 2 · Suma de dígitos y divisibilidad (media)

Archivo: `mis_soluciones/ej2.py`

1. `suma_digitos(n)`: devuelve la suma de los dígitos de un entero no negativo.
   **Sin convertir a texto**: solo con `while`, `//` y `%` (lo que quedó pendiente de la Lección 04).
2. `divisible_por_3(n)`: devuelve `True` si n es divisible entre 3. **Sin usar `n % 3`**: usa la regla
   de que un número es divisible entre 3 si y solo si la suma de sus dígitos lo es.

| Llamada | Resultado esperado |
|---|---|
| `suma_digitos(1234)` | `10` |
| `suma_digitos(1000)` | `1` |
| `suma_digitos(0)` | `0` |
| `divisible_por_3(123)` | `True` |
| `divisible_por_3(124)` | `False` |
| `divisible_por_3(999999)` | `True` |

Pista: `1234 % 10` da el último dígito y `1234 // 10` lo quita.

## Ejercicio 3 · Ángulo entre dos vectores (más difícil)

Archivo: `mis_soluciones/ej3.py`

Conecta con el capítulo 6 del Lay. Para dos vectores del plano **u** = (x1, y1) y **v** = (x2, y2):

```text
producto escalar:   u · v = x1·x2 + y1·y2
norma:              ‖u‖ = √(x1² + y1²)
ángulo:             cos θ = (u · v) / (‖u‖ · ‖v‖)
```

Escribe tres funciones:

1. `producto_escalar(x1, y1, x2, y2)`
2. `norma(x, y)`
3. `angulo(x1, y1, x2, y2)`: devuelve el ángulo en **grados**. Tiene que usar las otras dos.
   Si alguno de los vectores es el vector cero, el ángulo no está definido: devuelve `None`.

Para el arco coseno necesitas el módulo `math` de la biblioteca estándar:

```python
import math                 # va al principio del archivo

math.acos(0)                # arco coseno, en radianes: 1.5707963267948966
math.degrees(math.pi)       # de radianes a grados: 180.0
```

En las pruebas, muestra los ángulos con 2 decimales.

| Llamada | Resultado esperado |
|---|---|
| `producto_escalar(1, 2, 3, 4)` | `11` |
| `norma(3, 4)` | `5.0` |
| `angulo(1, 0, 0, 1)` | `90.00` |
| `angulo(2, 1, 1, 3)` | `45.00` |
| `angulo(3, 4, 6, 8)` | `0.00` |
| `angulo(1, 0, -1, 0)` | `180.00` |
| `angulo(0, 0, 1, 1)` | `None` |

⚠️ Cuidado al mostrar el caso `None` con `:.2f`. Pruébalo y mira qué pasa.

**Para qué sirve:** el coseno del ángulo entre dos vectores (la "similitud coseno") es una de las
herramientas más usadas en IA, por ejemplo para medir lo parecidos que son dos textos.

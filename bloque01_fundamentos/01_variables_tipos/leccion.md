# Lección 01 · Variables y tipos

## La idea clave

En Java la **variable** tiene tipo: `int edad = 21;`.
En Python el tipo lo tiene el **valor**, no la variable. No se declara nada: se asigna y listo.
Tampoco hay punto y coma, ni llaves, ni método `main`.

```python
edad = 21          # Python deduce que el valor es un int
edad = "veintiuno" # la misma variable ahora apunta a un str (en Java no compilaría)
```

## Tipos básicos (comparados con Java)

| Java | Python | Notas |
|---|---|---|
| `int`, `long` | `int` | Sin límite de tamaño: no hay overflow |
| `double`, `float` | `float` | Equivale al `double` de Java |
| `String` | `str` | Comillas simples o dobles, da igual |
| `char` | — | No existe: un carácter es un `str` de longitud 1 |
| `boolean` (`true`/`false`) | `bool` (`True`/`False`) | ¡Con mayúscula! |
| `null` | `None` | |

Con `type(valor)` puedes ver el tipo de cualquier cosa.

## Dinámico, pero fuerte

Python es de tipado **dinámico** (el tipo se decide al ejecutar) pero **fuerte**:
no convierte tipos por su cuenta. Si quieres convertir, lo haces tú:

```python
int("42")     # str -> int: 42
float("3.5")  # str -> float: 3.5
str(10)       # int -> str: "10"
int(3.9)      # float -> int: 3 (trunca, no redondea)
```

## f-strings

La forma moderna de meter variables dentro de un texto: una `f` delante de las comillas
y las variables entre llaves.

```python
nombre = "Lucía"
edad = 21
print(f"{nombre} tiene {edad} años")  # Lucía tiene 21 años
```

## Nombres de variables

En Java se usa `camelCase`; en Python, la guía de estilo oficial (PEP 8) pide `snake_case`:

```python
nota_media = 7.5   # bien
notaMedia = 7.5    # funciona, pero no es estilo Python
```

## Ejemplo completo

Ejecuta [`ejemplos.py`](ejemplos.py) y comprueba que la salida coincide con los comentarios.

## 🔮 Predicción

Antes de ejecutarlo, escribe en `mis_soluciones/prediccion.md` qué imprime cada línea.
Cuidado: alguna puede dar error.

```python
a = 7
b = "7"
print(a * 2)
print(b * 2)
print(int(b) + a)
print(a + b)
```

Después ejecútalo y compara. Si fallaste alguna, intenta explicar por qué.

## Siguiente paso

Los ejercicios están en [`ejercicios.md`](ejercicios.md).

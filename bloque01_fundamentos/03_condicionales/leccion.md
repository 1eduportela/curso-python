# Lección 03 · Condicionales

## 🔁 Repaso de la 02

Apúntalo en `mis_soluciones/prediccion.md` sin ejecutarlo:

```python
print(17 // 5, 17 % 5)
print(-17 // 5)
print(not 0 == 0 or 5 > 7)
```

## `if`, `elif`, `else`

```python
nota = 6.5

if nota >= 9:
    print("Sobresaliente")
elif nota >= 5:
    print("Aprobado")
else:
    print("Suspenso")
```

Diferencias con Java:

- No hacen falta paréntesis alrededor de la condición.
- Al final de la línea van **dos puntos** `:`.
- No hay llaves: el bloque se marca con la **sangría** (4 espacios). VS Code la pone solo al pulsar Enter
  después de los `:`.
- `else if` se escribe `elif`.

La sangría no es estética: es la sintaxis. Si te la saltas, Python da `IndentationError`.

```python
if nota >= 5:
print("Aprobado")   # IndentationError: expected an indented block
```

Igual que en Java, solo se ejecuta **la primera** rama cuya condición se cumple. El orden importa.

## Valores "verdaderos" y "falsos"

En Java, la condición de un `if` tiene que ser un `boolean`. En Python vale **cualquier valor**,
y estos cuentan como falsos:

| Falsos | Ejemplos |
|---|---|
| `False` | |
| `None` | |
| el cero | `0`, `0.0` |
| lo vacío | `""` (texto vacío), y más adelante listas vacías, etc. |

Todo lo demás cuenta como verdadero. Es muy útil para comprobar si el usuario escribió algo:

```python
nombre = input("Nombre: ")
if nombre:
    print(f"Hola, {nombre}")
else:
    print("No has escrito nada")
```

## Expresión condicional (el "ternario")

Para elegir entre dos valores en una sola línea. En Java es `cond ? a : b`; en Python se lee casi
como una frase:

```python
horas = 1
palabra = "hora" if horas == 1 else "horas"
print(f"{horas} {palabra}")   # 1 hora
```

Úsala solo para casos sencillos. Si la lógica crece, mejor un `if` normal.

## 🔮 Predicción

Añádela a `mis_soluciones/prediccion.md` antes de ejecutar nada. ¿Qué imprime?

```python
nota = 8
if nota >= 5:
    print("aprobado")
elif nota >= 7:
    print("notable")
else:
    print("suspenso")

texto = ""
if texto:
    print("hay texto")
else:
    print("vacío")

n = 0
if n:
    print("A")
if not n:
    print("B")
if "0":
    print("C")

x = -7
print("par" if x % 2 == 0 else "impar")
```

## Ejemplos

Después de la predicción, ejecuta [`ejemplos.py`](ejemplos.py).

## Siguiente paso

Los ejercicios están en [`ejercicios.md`](ejercicios.md).

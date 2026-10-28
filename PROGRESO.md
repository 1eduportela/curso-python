# Progreso

Resúmenes de sesión, del más reciente al más antiguo.
Cada resumen recoge: temas vistos, ejercicios hechos, puntos débiles y siguiente paso.

## Sesión 2 · 27 oct 2026

**Temas vistos**
- Lección 02: operadores aritméticos (`/` siempre `float`, `//` redondea hacia abajo, `%`, `**`), comparación encadenada, `and`/`or`/`not`, formato `:.2f`.
- Lección 03: `if`/`elif`/`else`, la sangría como sintaxis, valores verdaderos y falsos, expresión condicional.
- Dudas resueltas: cadena `if`/`elif` frente a `if` sueltos, comentarios de varias líneas, determinante y regla de Cramer para el sistema 2×2.

**Ejercicios hechos**
- Predicción 02: 8/10, corregida. Predicción 03: casi perfecta (faltó la `C` de `if "0":`).
- L02: norma de un vector ✅ (tras cambiar `int` por `float`), conversor de segundos ✅, año bisiesto ✅ (segunda versión, con explicación correcta).
- L03: calificación ✅, conversor de segundos v2 ✅ (de 8 ramas a 3 decisiones independientes), sistema 2×2: lógica ✅, falta mostrar la solución con 2 decimales.

**Puntos débiles**
- Intuiciones de Java: `-7 // 2` y `10 / 5`. Superado en el repaso de la 03 (`-17 // 5` a la primera).
- Textos que contienen dígitos: `"7" * 2`, `if "0":`.
- Usar nombres de funciones integradas como variables (`sum`, `min`).
- La salida no coincide exactamente con la pedida (mensajes, decimales).

**Siguiente paso**
- Lección 04: bucles. Antes, terminar el formato del ej. 3 de la 03.

## Sesión 1 · 26 oct 2026

**Temas vistos**
- Entorno: Git para Windows, VS Code con la cuenta de GitHub y el flujo del curso (`pull`, trabajar en `mis_soluciones/`, `push`).
- Lección 01: tipos básicos (`int`, `float`, `str`, `bool`, `None`), tipado dinámico pero fuerte, conversiones (`int()`, `float()`, `str()`), f-strings, `snake_case`.

**Ejercicios hechos**
- Predicción 01: en dos intentos (el primero se hizo sobre `ejemplos.py` por error).
- Ej. 1, ficha personal: ✅
- Ej. 2, suma con `input()`: ✅ tras corregir el uso de `sum` como variable.
- Ej. 3, caza de errores: ✅ en la segunda versión, con explicaciones precisas.

**Puntos débiles**
- Predecir "error" en operaciones válidas que no existen en Java (`type(None)`, `"7" * 2`).
- Explicar con precisión la causa de un error (mejoró en la segunda versión).
- Subir código sin ejecutarlo antes.

**Siguiente paso**
- Lección 02: operadores.

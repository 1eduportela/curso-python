# Curso de Python: de cero a NumPy y Qiskit

Curso personal de Python, guiado por un tutor (Claude), con una meta a largo plazo:
usar Python en **inteligencia artificial** y **computación cuántica**.
En paralelo estudio álgebra lineal con *Linear Algebra and Its Applications* (David C. Lay),
y a partir del bloque 6 los dos caminos se juntan.

Punto de partida: 3º de Ingeniería Informática, con experiencia en Java y SQL.
Por eso las lecciones comparan Python con Java cuando ayuda.

## Cómo funciona este repo

Cada lección vive en su propia carpeta:

```text
01_variables_tipos/
├── leccion.md         # teoría breve + ejemplo + predicción
├── ejemplos.py        # el código de la lección, listo para ejecutar
├── ejercicios.md      # enunciados (sin soluciones)
└── mis_soluciones/    # mi código
```

1. Leo `leccion.md` y ejecuto `ejemplos.py`.
2. Antes de ejecutar nada nuevo, apunto mi predicción en `mis_soluciones/prediccion.md`.
3. Resuelvo los ejercicios en `mis_soluciones/` y hago `push`.
4. El tutor corrige leyendo el repo.

Las soluciones "oficiales" no se suben: primero se intenta, luego pistas, y solo al final la solución.

## Ruta

### Bloque 1 · Fundamentos
- [x] [01 · Variables y tipos](bloque01_fundamentos/01_variables_tipos/leccion.md)
- [ ] [02 · Operadores](bloque01_fundamentos/02_operadores/leccion.md)
- [ ] 03 · Condicionales
- [ ] 04 · Bucles
- [ ] 05 · Funciones
- [ ] Mini proyecto 1

### Próximos bloques
- [ ] **Bloque 2 · Estructuras de datos**: listas, tuplas, diccionarios, conjuntos
- [ ] **Bloque 3 · Texto, archivos y errores**: cadenas, lectura/escritura de archivos, excepciones
- [ ] **Bloque 4 · Programación orientada a objetos**: clases y objetos
- [ ] **Bloque 5 · Buenas prácticas**: código legible, módulos, pruebas sencillas
- [ ] **Bloque 6 · NumPy**: vectores y matrices, conectado con álgebra lineal
- [ ] **Bloque 7 · Matplotlib**: visualización
- [ ] **Bloque 8 · Qiskit**: introducción a la computación cuántica

No se avanza de bloque hasta dominar el anterior. Cada pocos temas hay un mini proyecto integrador.

## Requisitos

- Python 3.10 o superior
- VS Code con la extensión de Python

Para ejecutar un archivo desde la terminal (en Windows puede ser `py` en lugar de `python`):

```bash
python bloque01_fundamentos/01_variables_tipos/ejemplos.py
```

## Progreso

Los resúmenes de cada sesión están en [PROGRESO.md](PROGRESO.md).

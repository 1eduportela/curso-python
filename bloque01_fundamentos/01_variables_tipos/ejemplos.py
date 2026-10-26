# Lección 01 · Variables y tipos
# Ejecuta este archivo y comprueba que la salida coincide con los comentarios.

# --- Tipos básicos ---
edad = 21           # int (sin límite de tamaño)
altura = 1.78       # float (como el double de Java)
nombre = "Lucía"    # str
aprobado = True     # bool (True/False con mayúscula)
nada = None         # el "null" de Python

print(type(edad))      # <class 'int'>
print(type(altura))    # <class 'float'>
print(type(nombre))    # <class 'str'>
print(type(aprobado))  # <class 'bool'>
print(type(nada))      # <class 'NoneType'>

# --- f-strings ---
print(f"{nombre} tiene {edad} años y mide {altura} m")  # Lucía tiene 21 años y mide 1.78 m

# --- Una variable puede cambiar de tipo ---
edad = "veintiuno"
print(type(edad))      # <class 'str'>

# --- Los int no tienen overflow ---
grande = 2147483647    # el máximo de un int en Java
print(grande + 1)      # 2147483648 (en Java daría -2147483648)

# --- Conversiones explícitas ---
print(int("42") + 1)   # 43
print(float("3.5"))    # 3.5
print(str(10) + "0")   # 100 (es texto: "10" + "0")
print(int(3.9))        # 3 (trunca, no redondea)

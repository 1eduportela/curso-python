# Lección 03 · Condicionales
# Ejecútalo DESPUÉS de hacer la predicción de leccion.md.

# --- if / elif / else ---
temperatura = 28

if temperatura >= 30:
    print("Hace calor")
elif temperatura >= 20:
    print("Se está bien")      # se ejecuta esta
else:
    print("Hace frío")

# --- Condiciones compuestas ---
edad = 20
tiene_carnet = False

if edad >= 18 and tiene_carnet:
    print("Puede conducir")
elif edad >= 18:
    print("Edad suficiente, pero falta el carnet")   # se ejecuta esta
else:
    print("Es menor de edad")

# --- Valores verdaderos y falsos ---
mensaje = ""
if mensaje:
    print("Hay mensaje")
else:
    print("Mensaje vacío")     # "" cuenta como falso

saldo = 0.0
if not saldo:
    print("Saldo a cero")      # 0.0 cuenta como falso

# --- Expresión condicional ---
numero = 3
tipo = "par" if numero % 2 == 0 else "impar"
print(f"{numero} es {tipo}")   # 3 es impar

minutos = 1
print(f"{minutos} {'minuto' if minutos == 1 else 'minutos'}")   # 1 minuto

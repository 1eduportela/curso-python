print("Necesito que me des los dos componentes de un vector")

x = input("Primer componente (x)...")
y = input("Segundo componente (y)...")

norma = (float(x)**2 + float(y)**2)**0.5

print(f"La longitud del vector ({x},{y}) es {norma:.2f}")
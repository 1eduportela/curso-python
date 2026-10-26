#precio = 19.99
#cantidad = input("¿Cuántas unidades? ")
#total = precio * cantidad
#print("Total: " + total + " euros")

#El primer error es que el input va a recibir un str y precio es un número
#El segundo error es que el segundo print suma un str con un float

precio = 19.99
cantidad = input("¿Cuántas unidades? ")
total = precio * float(cantidad)
print(f"Total: {total} euros")
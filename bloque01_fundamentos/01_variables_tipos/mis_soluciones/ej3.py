precio = 19.99
cantidad = input("¿Cuántas unidades? ")
total = precio * cantidad
print("Total: " + total + " euros")

#El primer error es que el input va a recibir un str y precio es un número
#El segundo error es que el segundo print deberia cumplir con la nomenclatura de f""
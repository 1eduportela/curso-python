x = str(input("Escribe un número entero y te doy la suma de sus digitos:..."))

total = 0
for i in x:
    total = total + int(i)
print (total)
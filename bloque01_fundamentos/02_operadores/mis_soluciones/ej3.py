x = int(input("Escribeme un año y te digo si es bisiesto:..."))

res = ((x%4)==0) and ((x%100)!=0) and ((x%400)!=0)

print(res)

#Mi programa funciona con 1900 y con 2000 porque el resto de la division entre 4 de ambos es 0
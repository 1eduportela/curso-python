x = int(input("Escribeme un año y te digo si es bisiesto:..."))

res = (((x%4)==0) and ((x%100)!=0)) or (((x%100)==0) and (x%400)==0)

print(res)

#Mi programa funciona con 1900 y con 2000 porque tiene en cuenta que si es divisible entre 100, tambien tiene que serlo entre 400
#1900%4=0, 1900%100=0 y 1900%400!=0 -> False
#2000%4=0, 2000%100=0 y 2000%400==0 -> True
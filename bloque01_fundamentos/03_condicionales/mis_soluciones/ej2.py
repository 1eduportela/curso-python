x = int(input("Dime un número de segundos para cambair el formato:..."))

h = x // 3600
m = (x % 3600) // 60
s = (x % 60)

if x < 0:
    print("Número no valido")
else:
    if h == 1:
        hor = "hora"
    else:
        hor ="horas"

    if m == 1:
        min = "minuto"
    else:
        min ="minutos"

    if s == 1:
        seg = "segundo"
    else:
        seg ="segundos"
    
    print(f"{x} segundos son {h} {hor}, {m} {min} y {s} {seg}")

x = int(input("Dime un número de segundos para cambair el formato:..."))

h = x // 3600
m = (x % 3600) // 60
s = (x % 60)

if x < 0:
    print("Número no valido")
else:
    if h == 1 and m ==1 and s == 1:
        print(f"{x} segundos son {h} hora, {m} minuto y {s} segundo")
    elif h == 1 and m == 1:
        print(f"{x} segundos son {h} hora, {m} minuto y {s} segundos")
    elif m == 1 and s == 1:
        print(f"{x} segundos son {h} horas, {m} minuto y {s} segundo")
    elif h == 1 and s == 1:
        print(f"{x} segundos son {h} hora, {m} minutos y {s} segundo")
    elif h == 1 :
        print(f"{x} segundos son {h} hora, {m} minutos y {s} segundos")
    elif m == 1:
        print(f"{x} segundos son {h} horas, {m} minuto y {s} segundos")
    elif s == 1:
        print(f"{x} segundos son {h} horas, {m} minutos y {s} segundo")

    if h != 1 and m != 1 and s != 1:
        print(f"{x} segundos son {h} horas, {m} minutos y {s} segundos")

x = int(input("Dime un número de segundos para cambair el formato:..."))

h = x // 3600
m = (x % 3600) // 60
s = (x % 60)

print(f"{x} segundos son {h} horas, {m} minutos y {s} segundos")
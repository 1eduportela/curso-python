def suma_digitos(n):
    """Suma de los digitos de un número"""
    suma=0
    separar=0
    while(n!=0):
        separar=n%10
        suma=suma+separar
        n=n//10
    return suma

def divisible_por_tres(n):
    """Devuelve si n es un número divisible entre tres"""
    if suma_digitos(n)%3:
        return True
    else:
        return False

print(suma_digitos(1234))
print(suma_digitos(1000))
print(suma_digitos(0))
print(divisible_por_tres(123))
print(divisible_por_tres(124))
print(divisible_por_tres(999999))
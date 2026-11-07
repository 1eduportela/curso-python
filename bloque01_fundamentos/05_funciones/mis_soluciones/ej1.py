def es_bisiesto(anio):
    """Cálculo año bisiesto"""
    return (((anio%4)==0) and ((anio%100)!=0)) or (((anio%100)==0) and (anio%400)==0)

def dias_del_anio(anio):
    """Cálculo número días del año"""
    if es_bisiesto(anio):
        return 366
    else:
        return 365

print(es_bisiesto(2024))
print(es_bisiesto(1900))
print(es_bisiesto(2000))
print(dias_del_anio(2023))
print(dias_del_anio(2024))
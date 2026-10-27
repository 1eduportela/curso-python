nota = float(input("Dime la nota del alumno que queremos calificar:..."))

if nota < 0:
    print("No valido")
elif nota > 10:
    print("No valido")
elif nota >= 9:
    print("Sobresaliente")
elif nota >= 7:
    print("Notable")
elif nota >= 5:
    print("Aprovado")
elif nota < 5:
    print("Suspenso")
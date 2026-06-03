# 24. Clasificar una nota (Suspenso, Aprobado, Notable, Sobresaliente).

try:
    nota = float(input("Introduce tu nota: "))

    if nota < 5:
        print("Estás suspenso")
    elif nota < 7:
        print("Estás aprobado")
    elif nota < 9:
        print("Tienes un notable")
    else:
        print("Tienes un sobresaliente")

except ValueError:
    print("Valor no válido.")
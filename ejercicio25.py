# 25. Comprobar si un año es bisiesto.

try:
    anio = int(input("Introduce un año: "))

    if (anio % 400 == 0):
        print(f"{anio} es bisiesto")
    elif (anio % 100 == 0):
        print(f"{anio} no es bisiesto")
    elif (anio % 4 == 0):
        print(f"{anio} es bisiesto")
    elif (anio % 4 != 0):
        print(f"{anio} no es bisiesto")

except ValueError:
    print("Valor no válido.")
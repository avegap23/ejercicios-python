# 54. Una empresa tiene dos turnos (mañana y tarde) en los que trabajan 8 empleados
# (4 por la mañana y 4 por la tarde) Confeccionar un programa que permita almacenar
# los sueldos de los empleados agrupados en dos listas. Imprimir las dos listas de sueldos.

sueldos_maniana = []
sueldos_tarde = []

def generar_lista_sueldos(turno):
    if turno == "mañana":
        print("\nSueldos turno de mañana:")
        for i in range(1, 5):
            sueldo = float(input(f"Introduce el sueldo del {i}º empleado: "))
            sueldos_maniana.append(sueldo)

    elif turno == "tarde":
        print("\nSueldos turno de tarde:")
        for i in range(1, 5):
            sueldo = float(input(f"Introduce el sueldo del {i}º empleado: "))
            sueldos_tarde.append(sueldo)

def imprimir_lista_sueldos(turno):
    if turno == "mañana":
        print("\nLista de sueldos del turno de mañana")
        for i in range(len(sueldos_maniana)):
            print(f"{sueldos_maniana[i]}€")
    
    elif turno == "tarde":
        print("\nLista de sueldos del turno de tarde")
        for i in range(len(sueldos_tarde)):
            print(f"{sueldos_tarde[i]}€")

generar_lista_sueldos("mañana")
generar_lista_sueldos("tarde")

imprimir_lista_sueldos("mañana")
imprimir_lista_sueldos("tarde")
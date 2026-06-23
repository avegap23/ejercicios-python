# 52. Almacenar en una lista los sueldos (valores float) de 5 operarios. Imprimir la lista y el promedio de sueldos.

lista_sueldos = []
for i in range(1, 6):
    sueldo = float(input(f"Introduce el {i}º sueldo: "))
    lista_sueldos.append(sueldo)

print("\nLista de sueldos: ")
for i in range(len(lista_sueldos)):
    print(f"{lista_sueldos[i]}€")

sum_sueldos = 0
for i in range(len(lista_sueldos)):
    sum_sueldos += lista_sueldos[i]
promedio_sueldos = sum_sueldos / len(lista_sueldos)
print(f"\nPromedio de los sueldos: {promedio_sueldos}€")
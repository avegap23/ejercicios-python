# 53. Cargar por teclado y almacenar en una lista las alturas de 5 personas (valores float).
# Obtener el promedio de las mismas. Contar cuántas personas son más altas que el promedio
# y cuántas más bajas.

lista_alturas = []
for i in range(1, 6):
    altura = float(input(f"Introduce la altura de la {i}ª persona: "))
    lista_alturas.append(altura)

sum_alturas = 0
for i in range(len(lista_alturas)):
    sum_alturas += lista_alturas[i]
promedio_alturas = sum_alturas / len(lista_alturas)
print(f"\nAltura promedio: {promedio_alturas}m")

mas_altas = 0
mas_bajas = 0
for i in range(len(lista_alturas)):
    if lista_alturas[i] >= promedio_alturas:
        mas_altas += 1
    else:
        mas_bajas += 1
print(f"\nHay {mas_altas} personas más altas que la media")
print(f"Hay {mas_bajas} personas más bajas que la media")
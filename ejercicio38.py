# 38. Contar cuántas veces aparece un número.

numeros = [1, 5, 6, 65, 7, 2, 7, 8, 10, 0, 89]

for i in range(len(numeros)):
    print(f"{numeros[i]}: {numeros.count(numeros[i])}")
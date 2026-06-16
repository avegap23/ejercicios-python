# 36. Calcular la suma de los elementos de una lista.

numeros = [1, 5, 6, 65, 7, 2, 7, 8, 10, 0, 89]

cont = 0
for i in range(len(numeros)):
    cont += numeros[i]

print(cont)
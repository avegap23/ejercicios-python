# 39. Eliminar elementos duplicados.

numeros = [1, 5, 6, 65, 7, 2, 7, 8, 10, 0, 89]
print(f"Original: {numeros}")

rango = len(numeros)
for i in range(rango):
    if numeros.count(numeros[i]) > 1:
        del numeros[i]
        rango -= 1
        break

print(f"Nuevo: {numeros}")
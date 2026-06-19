# 49. Contar la frecuencia de palabras usando un diccionario.

palabras = {}

frase = input("Escribe: ")

for palabra in frase.split():
    if palabra not in palabras:
        palabras[palabra] = 1
    else:
        palabras[palabra] += 1

print(palabras)
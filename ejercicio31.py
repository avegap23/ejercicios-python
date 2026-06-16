# 31. Contar cuántas vocales tiene una palabra.

palabra = str(input("Introduce una palabra, cualquiera: "))

palabra_lower = palabra.lower()

cont_vocales = 0
for letra in palabra_lower:
    if letra in ['a', 'e', 'i', 'o', 'u']:
        cont_vocales += 1

print(f"'{palabra}' tiene {cont_vocales} vocales")
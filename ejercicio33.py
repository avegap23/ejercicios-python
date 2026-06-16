# 33. Adivinar un número usando while.

import random

min = 1
max = 50
num_secreto = random.randint(min, max)

cont = 0
num_usuario = int(input(f"Adivina en qué numero estoy del {min} al {max} estoy pensando: "))

while num_usuario != num_secreto:
    if num_usuario > num_secreto:
        print("\nEl número es más pequeño.")
    elif num_usuario < num_secreto:
        print("\nEl número es más grande.")
    num_usuario = int(input("Prueba otra vez: "))
    cont += 1

if num_usuario == num_secreto:
    cont += 1
    print(f"\nFelicidades, mi número era {num_secreto}. Has acertado en {cont} intento(s).")
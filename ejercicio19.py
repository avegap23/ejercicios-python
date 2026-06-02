# 19. Clasificar un número como positivo, negativo o cero.

n = float(input("Introduce un número: "))

if n < 0:
    print(str(n) + " es negativo")
elif n > 0:
    print(str(n) + " es positivo")
else:
    print(str(n) + " es literalmente 0")
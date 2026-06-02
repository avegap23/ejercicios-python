# 17. Determinar si un número es par o impar.

n = int(input("Introduce un número entero: "))

if (n % 2 == 0):
    print(str(n) + " es par")
else:
    print(str(n) + " es impar")
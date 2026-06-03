# 21. Encontrar el mayor de dos números.

n1 = float(input("Introduce un número: "))
n2 = float(input("Introduce otro número: "))

if n1 > n2:
    print(f"{n1} es mayor que {n2}")
elif n1 < n2:
    print(f"{n2} es mayor que {n1}")
else:
    print("Ambos números son iguales")
# 22. Encontrar el mayor de tres números.

n1 = float(input("Introduce un número: "))
n2 = float(input("Introduce otro número: "))
n3 = float(input("Otro más: "))

if n1 != n2 != n3:
    if n1 > n2 and n1 > n3:
        print(f"{n1} es el mayor")
    elif n2 > n3:
        print(f"{n2} es el mayor")
    else:
        print(f"{n3} es el mayor")
else:
    print("Todos los números son iguales")
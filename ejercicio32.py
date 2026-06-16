# 32. Calcular el factorial de un número.

while True:
    # Estructura de control
    try:
        n = int(input("Introduce un número positivo entero mayor que cero: "))
        if n <= 0:
            print("\nTienes que introducir un NÚMERO MAYOR QUE CERO.")
            continue
    except ValueError:
        print("\nTienes que introducir un NÚMERO ENTERO.")
        continue
    
    # La chicha
    factorial = 1
    for i in range(1, n+1):
        factorial *= i
    
    print(f"El factorial de {n} es {factorial}")
    break
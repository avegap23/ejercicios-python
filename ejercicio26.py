# 26. Simular una calculadora usando if/elif.

while True:
    print('''
    [+] Suma
    [-] Resta
    [*] Multiplicación
    [/] División
    ''')

    op = str(input("Elige una operación (sólo símbolos):"))

    if op not in ['+', '-', '*', '/']:
        print("\nHas introducido una opción desconocida")
        break

    num1 = float(input("Primer número: "))
    num2 = float(input("Segundo número: "))

    if op == '+':
        print(f"Resultado: {num1 + num2}")
        break
    elif op == '-':
        print(f"Resultado: {num1 - num2}")
        break
    elif op == '*':
        print(f"Resultado: {num1 * num2}")
        break
    elif op == '/':
        if num2 == 0:
            print("\nEstás dividiendo entre 0 y eso no se puede hacer")
            break
        else:
            print(f"Resultado: {num1 / num2}")
            break
# 30. Mostrar la tabla de multiplicar de un número.

num = int(input("Introduce un número: "))

print(f"\nTABLA DEL {num}:")
for i in range(11):
    print(f"{num} x {i} = {num*i}")
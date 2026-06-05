# 29. Sumar los primeros N números, sabiendo que N es un número que introducimos por teclado

num = int(input("¿Hasta donde sumar?: "))

suma = 0

for i in range(1, num+1):
    print(f"{suma} + {i} = {suma + i}")
    suma += i
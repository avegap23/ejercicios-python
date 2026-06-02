# 20. Determinar si una persona es mayor de edad.

edad = int(input("Introduce tu edad: "))

if edad >= 18:
    print("Eres mayor de edad")
elif 0 <= edad < 18:
    print("Eres menor de edad")
else:
    print("No existes")
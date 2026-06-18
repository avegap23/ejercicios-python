# 45. Crear un diccionario con nombre, edad y ciudad.

alguien = {}

nombre = input("¿Cómo te llamas?: ")
edad = int(input("Tu edad: "))
ciudad = input("Tu ciudad: ")

alguien["Nombre"] = nombre
alguien["Edad"] = edad
alguien["Ciudad"] = ciudad

print(alguien)
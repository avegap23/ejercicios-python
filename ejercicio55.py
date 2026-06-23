# 55. Cargar una oración por teclado. Mostrar luego cuántos espacios en blanco
# se ingresaron. Tener en cuenta que un espacio en blanco es igual a " ",
# en cambio una cadena vacía es ""

oracion = input("Escribe. Algo: ")

if oracion == "":
    print("Has introducido una cadena vacía")

else:
    blancos = 0
    for i in oracion:
        if i == " ":
            blancos += 1
    
    print(f"La oración tiene {blancos} espacios en blanco")
# 42. Buscar un elemento dentro de una lista.

lista = [1, 5, 6, 65, 7, 2, 7, 8, 10, 0, 89]

busqueda = int(input("Introduce el elemento a buscar: "))

if busqueda in lista:
    print(f"Lo he encontrado. Está en la posición {lista.index(busqueda)}")
else:
    print(f"No he encontrado el elemento {busqueda}")
# 41. Crea una lista con varios productos. Además, incluye una sublista
# por cada lista (precio, por ejemplo). Debemos ordenar los productos por precio.

productos = {
    "Manzanas": 1.00,
    "Peras": 2.10,
    "Plátanos": 1.80
}

precios = []
for p in productos:
    precios.append(productos.get(p))

precios.sort(reverse=True)
print(precios)
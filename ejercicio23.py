# 23. Calcular descuento según importe de compra.

try:
    importe = float(input("Precio de la compra: "))
    descuento = float(input("Un descuento: "))

    precio_final = importe - ((importe * descuento) / 100)

    print(f"\n{importe}€ con un -{descuento}% de descuento aplicado es {precio_final}€")

except ValueError:
    print("\nValor(es) no válidos.")
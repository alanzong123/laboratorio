print("El checkout no distingue el precio de contado del precio a meses.")
precio = 1200
comision_12 = 0.15
recibe = precio - precio * comision_12
print("A 12 MSI la tienda recibe", recibe)
precio_msi = precio / (1 - comision_12)
print("Precio a meses:", precio_msi, "| Mensualidad:", precio_msi / 12)
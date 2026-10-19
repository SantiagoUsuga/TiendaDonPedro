
from pathlib import Path

archivo = Path("datos/productos.txt")

lineas = archivo.read_text(encoding="utf-8").splitlines()

print("=== Inventario Tienda Don Pedro ===")

productos = lineas[2:]

for linea in productos:
    print("-", linea)

total_productos = len(productos)

valor_inventario = 0

for linea in productos:
    precio = linea.split("$")[-1].replace(".", "").replace(",", "").strip()
    valor_inventario += int(precio)

print(f"\nTotal de productos: {total_productos}")
print(f"Valor del inventario: ${valor_inventario:,}".replace(",", "."))

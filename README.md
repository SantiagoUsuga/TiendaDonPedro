# 🛒 Tienda Don Pedro


## 📌 Descripción del proyecto

**Tienda Don Pedro** es un proyecto desarrollado en Python para administrar información básica de una tienda de barrio. Permite consultar los productos registrados en un archivo de texto, mostrar el inventario y calcular la cantidad de productos y su valor total.

El proyecto también contiene información sobre los clientes frecuentes de la tienda y utiliza buenas prácticas para proteger los datos privados.

## 🎯 Objetivos

- Registrar y consultar los productos de la tienda.
- Mostrar los precios de los productos disponibles.
- Calcular la cantidad total de productos registrados.
- Calcular el valor del inventario.
- Identificar a los clientes frecuentes.
- Proteger la información privada mediante archivos de configuración y `.gitignore`.

## 🛍️ Productos de la tienda

| Producto | Precio |
|---|---:|
| Leche 1L | $4.200 |
| Pan tajado | $6.500 |
| Huevos x12 | $14.000 |
| Café 500g | $18.000 |
| Panela | $3.500 |
| Gaseosa | $1.000 |

## 👥 Clientes frecuentes

| Cliente | Dirección de referencia |
|---|---|
| Doña Rosa | Calle 50 |
| Julián | Carrera 48 |
| La señora Gloria | Calle 52 |
| Don Carlos | Calle 49 |

## 🧾 Ejemplo de una compra

El siguiente registro representa una compra realizada por un cliente:

- **Cliente:** Doña Rosa
- **Producto:** Leche 1L
- **Precio registrado en la compra:** $4.500

Este valor corresponde al registro de la compra y es diferente del precio de $4.200 definido en la lista general de productos.

## ⚙️ Funcionamiento del programa

El programa utiliza la biblioteca `pathlib` de Python para leer el archivo de productos y realizar los cálculos del inventario.

Sus funciones principales son:

1. Leer los datos almacenados en `datos/productos.txt`.
2. Mostrar los productos registrados.
3. Contar las líneas correspondientes a los productos.
4. Extraer los precios y convertirlos en números enteros.
5. Sumar los precios para calcular el valor del inventario.
6. Mostrar los resultados en la terminal.

### Ejemplo de código

```python
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
```

> **Nota:** el código anterior supone que las dos primeras líneas del archivo son encabezados. Además, cada producto debe tener un precio que el programa pueda convertir a número. La cantidad contada corresponde a los registros de productos, no necesariamente a las unidades físicas disponibles.

## 📂 Estructura del proyecto

```text
tienda-don-pedro/
├── datos/
│   └── productos.txt
|    └── cliente.txt
|    └── ventas.txt
├── main.py
├── .gitignore
└── README.md
```

Esta estructura es una referencia inicial. Los nombres y las ubicaciones deben coincidir con los archivos reales de tu repositorio.

## 🚀 Cómo ejecutar el proyecto

### Requisitos

- Python 3 instalado.
- Git, si deseas clonar o administrar el repositorio.
- Una terminal de Linux, Windows o macOS.

### Pasos

1. Abre una terminal en la carpeta principal del proyecto.
2. Verifica que Python esté instalado:

```bash
python --version
```

En Linux también puedes utilizar:

```bash
python3 --version
```

3. Ejecuta el archivo principal:

```bash
python main.py
```

Si utilizas Linux y el comando anterior no funciona, prueba:

```bash
python3 main.py
```

## 🔐 Seguridad de la información

El proyecto utiliza un archivo `.gitignore` para evitar que determinados archivos privados o innecesarios se suban al repositorio.

Ejemplo:

```gitignore
# Claves y datos privados: nunca se suben
.env

# Archivos que crea Python automáticamente
__pycache__/
.venv/
```

**Importante:** no publiques contraseñas, claves bancarias ni datos sensibles en el código o en GitHub. Si una clave real ya fue publicada, cámbiala. El archivo `.gitignore` evita nuevas inclusiones accidentales, pero no elimina información que ya se haya subido al historial de Git.

## 🧰 Tecnologías utilizadas

- **Python 3:** lenguaje de programación.
- **pathlib:** manejo de rutas y archivos.
- **Markdown:** documentación del proyecto.
- **Git:** control de versiones.
- **GitHub:** alojamiento del repositorio, si se utiliza.

## 📌 Mejoras futuras

- Incorporar un menú interactivo para administrar el inventario.
- Permitir agregar, editar y eliminar productos.
- Registrar las cantidades disponibles de cada producto.
- Calcular el valor del inventario según las cantidades y los precios.
- Registrar las compras de los clientes.
- Guardar los datos en una base de datos.
- Validar los precios y manejar errores cuando falten archivos o existan datos incorrectos.

## 👨‍💻 Autor

**Daniel Esteban Narváez Ara**

Proyecto académico: Tienda Don Pedro.

---

*Desarrollado con Python para practicar la lectura de archivos, el manejo de datos, los ciclos, las operaciones matemáticas y el control de versiones con Git.*

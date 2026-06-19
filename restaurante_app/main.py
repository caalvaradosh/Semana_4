# Importación de clases

from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante

# Crear restaurante
restaurante = Restaurante("Restaurante El Buen Sabor")

# Crear productos
producto1 = Producto("Maito de Tilapia", 5.50)
producto2 = Producto("Maito de Pollo", 8.00)
producto3 = Producto("Asado de Chonta Curo", 2.50)

# Crear clientes
cliente1 = Cliente("Clide Alvarado", "0912345678")
cliente2 = Cliente("María López", "1712345678")

# Agregar productos
restaurante.agregar_producto(producto1)
restaurante.agregar_producto(producto2)
restaurante.agregar_producto(producto3)

# Agregar clientes
restaurante.agregar_cliente(cliente1)
restaurante.agregar_cliente(cliente2)

# Mostrar información
print(f"\n=== {restaurante.nombre} ===")

restaurante.mostrar_productos()
restaurante.mostrar_clientes()

import sys
import os

# Agregar la ruta del directorio Models al sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from Models.products import Products


producto_vendido = Products('Televisor', 100)
print(producto_vendido.discount_day(producto_vendido.product_price, discount_day='thursday'))


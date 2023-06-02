from ..models.products import Products

producto_vendido = Products('Televisor', 100)


print(producto_vendido.discount_day(producto_vendido.product_price, discount_day='thursday'))

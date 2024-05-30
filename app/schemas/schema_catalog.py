from app import ma

class ProductoSchema(ma.Schema):
    class Meta:
        fields = ( 'id_producto', 'nombre_producto', 'marca_producto', 'modelo_producto', 'precio_producto', 'disponibilidad', 'stock_producto')

producto_schema = ProductoSchema()
productos_schema = ProductoSchema(many=True)
from app import db

class Producto(db.Model):
    id_producto = db.Column(db.Integer, primary_key=True)
    nombre_producto = db.Column(db.String(100), nullable=False)
    marca_producto = db.Column(db.String(100), nullable=False)
    modelo_producto = db.Column(db.String(100), nullable=False)
    precio_producto = db.Column(db.Integer, nullable=False)
    disponibilidad = db.Column(db.Boolean, default=True)
    stock_producto = db.Column(db.Integer, nullable=False)
    

    def __init__(self, nombre_producto, marca_producto, modelo_producto, precio_producto, disponibilidad, stock_producto):
        self.nombre_producto = nombre_producto
        self.marca_producto = marca_producto
        self.modelo_producto = modelo_producto
        self.precio_producto = precio_producto
        self.disponibilidad = disponibilidad
        self.stock_producto = stock_producto


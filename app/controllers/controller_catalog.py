from flask import request, jsonify
from app.models.model_catalog import Producto
from app.schemas.schema_catalog import producto_schema, productos_schema
from app import db

def create_productos():
    data = request.get_json()
    if not isinstance(data, list):
        return jsonify({'message': 'Los datos deben ser una lista de productos.'}), 400

    new_productos = []
    for item in data:
        nombre_producto = item.get('nombre_prod')
        marca_producto = item.get('marca_prod')
        modelo_producto = item.get('modelo_prod')
        precio_producto = item.get('precio_prod')
        disponibilidad = item.get('disponibilidad')
        stock_producto = item.get('stock_prod')

        if not nombre_producto:
            return jsonify({'message': 'Nombre de producto es requerido.'}), 400

        if not marca_producto:
            return jsonify({'message': 'Marca de producto es requerido.'}), 400

        if not modelo_producto:
            return jsonify({'message': 'Modelo de producto es requerido.'}), 400

        if not precio_producto:
            return jsonify({'message': 'Precio de producto es requerido.'}), 400

        if not disponibilidad:
            return jsonify({'message': 'Disponibilidad de producto es requerido.'}), 400

        if not stock_producto:
            return jsonify({'message': 'Stock de producto es requerido.'}), 400

        new_producto = Producto(nombre_producto, marca_producto, modelo_producto, precio_producto, disponibilidad, stock_producto)
        db.session.add(new_producto) 
        new_productos.append(new_producto)

    db.session.commit()
    return productos_schema.jsonify(new_productos), 201

def get_productos():
    all_productos = Producto.query.all()
    result = productos_schema.dump(all_productos)
    return jsonify(result)

def get_producto(id):
    producto = Producto.query.get_or_404(id)
    return producto_schema.jsonify(producto)

def update_producto(id):
    producto = Producto.query.get_or_404(id)
    data = request.get_json()

    nombre_producto = data.get('nombre_prod')
    marca_producto = data.get('marca_prod')
    modelo_producto = data.get('modelo_prod')
    precio_producto = data.get('precio_prod')
    disponibilidad = data.get('disponibilidad')
    stock_producto = data.get('stock_prod')

    if nombre_producto:
        producto.nombre_prod = nombre_producto

    if marca_producto:
        producto.marca_prod = marca_producto

    if modelo_producto:
        producto.modelo_prod = modelo_producto

    if precio_producto:
        producto.precio_prod = precio_producto

    if disponibilidad:
        producto.disponibilidad = disponibilidad

    if stock_producto:
        producto.stock_prod = stock_producto

    db.session.commit()
    return producto_schema.jsonify(producto)

def delete_producto(id):
    producto = Producto.query.get_or_404(id)
    db.session.delete(producto)
    db.session.commit()
    return '', 204



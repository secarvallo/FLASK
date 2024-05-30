from flask import Blueprint
from flask import jsonify
from app.controllers.controller_catalog import create_productos, get_productos, get_producto, update_producto, delete_producto


catalog_bp= Blueprint('catalog_bp', __name__)

@catalog_bp.route('/productos', methods=['POST'])
def create_productos_route():
    return create_productos()

@catalog_bp.route('/productos', methods=['GET'])
def productos_route():
    return get_productos()

@catalog_bp.route('/productos/<int:id>', methods=['GET'])
def producto_id_route(id):
    return get_producto(id)

@catalog_bp.route('/productos/<int:id>', methods=['PUT'])
def update_producto_route(id):
    return update_producto(id)

@catalog_bp.route('/productos/<int:id>', methods=['DELETE'])
def delete_producto_route(id):
    return delete_producto(id)

@catalog_bp.route('/', methods=['GET'])
def index():
    return jsonify({'message': 'Welcome to my API'})





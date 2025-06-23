from flask import Blueprint, jsonify
from models.product_model import get_all_products
from schemas.product_schema import serialize_product

products_bp = Blueprint('products', __name__)

@products_bp.route('/products', methods=['GET'])
def get_products():
    rows = get_all_products()
    products = [serialize_product(row) for row in rows]
    return jsonify(products)

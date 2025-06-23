

from flask import Blueprint, jsonify
from models.category_model import get_all_category
from schemas.categories_schema import serialize_category

category_bp = Blueprint('category', __name__)

@category_bp.route('/category', methods=['GET'])
def get_categories():
    rows = get_all_category()
    category = [serialize_category(row) for row in rows]
    return jsonify(category)

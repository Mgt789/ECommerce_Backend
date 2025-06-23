from flask import Blueprint, jsonify
from models.user_model import get_all_users
from schemas.user_schema import serialize_user

users_bp = Blueprint('users', __name__)

@users_bp.route('/users', methods=['GET'])
def get_users():
    rows = get_all_users()
    users = [serialize_user(row) for row in rows]
    return jsonify(users)

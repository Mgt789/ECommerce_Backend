from flask import Flask
from flask_cors import CORS
from routes.users import users_bp
from routes.products import products_bp
from routes.category import category_bp

app = Flask(__name__)
CORS(app)

# Register Blueprints
app.register_blueprint(users_bp)
app.register_blueprint(products_bp)
app.register_blueprint(category_bp)


if __name__ == '__main__':
    app.run(debug=True)

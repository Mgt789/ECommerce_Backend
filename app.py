from flask import Flask
from flask_cors import CORS
from routes.users import users_bp
from routes.products import products_bp

app = Flask(__name__)
CORS(app)

# Register Blueprints
app.register_blueprint(users_bp)
app.register_blueprint(products_bp)


if __name__ == '__main__':
    app.run(debug=True)

print(f"🔍 __name__ is: {__name__}")

from flask import Flask, request, jsonify
from models import db
from schemas import ma
from datetime import datetime
import urllib.parse

# Import models
try:
    print("📦 Importing models...")
    from models.user import User
    from models.product import Product
    from models.order import Order, order_product
    print("✅ Models imported successfully.")
except Exception as e:
    print(f"❌ Error importing models: {e}")

# Import schemas
try:
    print("📦 Importing schemas...")
    from schemas.user_schema import UserSchema
    from schemas.product_schema import ProductSchema
    from schemas.order_schema import OrderSchema
    print("✅ Schemas imported successfully.")
except Exception as e:
    print(f"❌ Error importing schemas: {e}")

# Initialize Flask
try:
    print("🚧 Initializing Flask app...")
    app = Flask(__name__)
    print("✅ Flask app initialized.")
except Exception as e:
    print(f"❌ Failed to initialize Flask app: {e}")

# Setup DB URI
try:
    raw_password = "YOUR_MYSQL_PASSWORD"
    encoded_password = urllib.parse.quote_plus(raw_password)
    app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+mysqlconnector://root:{encoded_password}@localhost/ecommerce_api'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    print("🔧 App config set.")
except Exception as e:
    print(f"❌ Failed to set app config: {e}")

# Initialize DB + Marshmallow
try:
    db.init_app(app)
    ma.init_app(app)
    print("✅ DB and Marshmallow initialized.")
except Exception as e:
    print(f"❌ Failed to initialize DB or Marshmallow: {e}")

# Create tables
try:
    print("🧪 Entering app context for db.create_all()")
    with app.app_context():
        print("📋 Tables SQLAlchemy is trying to create:")
        for table_name in db.metadata.tables:
            print(f" - {table_name}")
        print("👀 Calling db.create_all()...")
        # db.create_all()
        print("✅ Tables created.")
except Exception as e:
    import traceback
    print(f"❌ Error during db.create_all(): {e}")
    traceback.print_exc()

# Health check route
@app.route('/ping-db')
def ping_db():
    try:
        db.session.execute('SELECT 1')
        return jsonify({"message": "✅ Database connection successful!"}), 200
    except Exception as e:
        return jsonify({"error": f"❌ Database connection failed: {str(e)}"}), 500

# ===== USER ENDPOINTS =====
user_schema = UserSchema()
users_schema = UserSchema(many=True)

@app.route('/users', methods=['GET'])
def get_users():
    return users_schema.jsonify(User.query.all())

@app.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    return user_schema.jsonify(User.query.get_or_404(id))

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    user = user_schema.load(data)
    db.session.add(user)
    db.session.commit()
    return user_schema.jsonify(user), 201

@app.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    user = User.query.get_or_404(id)
    data = request.get_json()
    user.name = data.get('name', user.name)
    user.address = data.get('address', user.address)
    user.email = data.get('email', user.email)
    db.session.commit()
    return user_schema.jsonify(user)

@app.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": "User deleted"}), 200

# ===== PRODUCT ENDPOINTS =====
product_schema = ProductSchema()
products_schema = ProductSchema(many=True)

@app.route('/products', methods=['GET'])
def get_products():
    return products_schema.jsonify(Product.query.all())

@app.route('/products/<int:id>', methods=['GET'])
def get_product(id):
    return product_schema.jsonify(Product.query.get_or_404(id))

@app.route('/products', methods=['POST'])
def create_product():
    product = product_schema.load(request.get_json())
    db.session.add(product)
    db.session.commit()
    return product_schema.jsonify(product), 201

@app.route('/products/<int:id>', methods=['PUT'])
def update_product(id):
    product = Product.query.get_or_404(id)
    data = request.get_json()
    product.product_name = data.get('product_name', product.product_name)
    product.price = data.get('price', product.price)
    db.session.commit()
    return product_schema.jsonify(product)

@app.route('/products/<int:id>', methods=['DELETE'])
def delete_product(id):
    product = Product.query.get_or_404(id)
    db.session.delete(product)
    db.session.commit()
    return jsonify({"message": "Product deleted"}), 200

# ===== ORDER ENDPOINTS =====
order_schema = OrderSchema()
orders_schema = OrderSchema(many=True)

@app.route('/orders', methods=['POST'])
def create_order():
    data = request.get_json()
    order = Order(
        order_date=datetime.fromisoformat(data['order_date']),
        user_id=data['user_id']
    )
    db.session.add(order)
    db.session.commit()
    return order_schema.jsonify(order), 201

@app.route('/orders/<int:order_id>/add_product/<int:product_id>', methods=['PUT'])
def add_product_to_order(order_id, product_id):
    order = Order.query.get_or_404(order_id)
    product = Product.query.get_or_404(product_id)
    if product in order.products:
        return jsonify({"message": "Product already in order"}), 400
    order.products.append(product)
    db.session.commit()
    return jsonify({"message": "Product added to order"}), 200

@app.route('/orders/<int:order_id>/remove_product/<int:product_id>', methods=['DELETE'])
def remove_product_from_order(order_id, product_id):
    order = Order.query.get_or_404(order_id)
    product = Product.query.get_or_404(product_id)
    if product not in order.products:
        return jsonify({"message": "Product not in order"}), 400
    order.products.remove(product)
    db.session.commit()
    return jsonify({"message": "Product removed from order"}), 200

@app.route('/orders/user/<int:user_id>', methods=['GET'])
def get_orders_by_user(user_id):
    orders = Order.query.filter_by(user_id=user_id).all()
    return orders_schema.jsonify(orders)

@app.route('/orders/<int:order_id>/products', methods=['GET'])
def get_products_in_order(order_id):
    order = Order.query.get_or_404(order_id)
    return products_schema.jsonify(order.products)

# ===== RUN APP =====
print("👋 End of file reached. Preparing to run app...")

if __name__ == '__main__':
    try:
        print("🚀 Starting server...")
        app.run(debug=True, use_reloader=False)
    except Exception as e:
        print(f"❌ Server failed to start: {e}")
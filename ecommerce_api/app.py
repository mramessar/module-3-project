from flask import Flask, request, jsonify
from models import db
from models.user import User
from models.order import Order
from models.product import Product
from models.order_product import order_product
from schemas import UserSchema, ProductSchema, OrderSchema

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:password@localhost/ecommerce_api'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()

# Users
@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    user_schema = UserSchema(many=True)
    return jsonify(user_schema.dump(users))

@app.route('/users/<id>', methods=['GET'])
def get_user(id):
    user = User.query.get_or_404(id)
    user_schema = UserSchema()
    return jsonify(user_schema.dump(user))

@app.route('/users', methods=['POST'])
def create_user():
    user_schema = UserSchema()
    user = user_schema.load(request.get_json())
    db.session.add(user)
    db.session.commit()
    return jsonify(user_schema.dump(user)), 201

@app.route('/users/<id>', methods=['PUT'])
def update_user(id):
    user = User.query.get_or_404(id)
    user_schema = UserSchema()
    updated_user = user_schema.load(request.get_json(), instance=user)
    db.session.commit()
    return jsonify(user_schema.dump(updated_user))

@app.route('/users/<id>', methods=['DELETE'])
def delete_user(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    return '', 204

# Products
@app.route('/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    product_schema = ProductSchema(many=True)
    return jsonify(product_schema.dump(products))

@app.route('/products/<id>', methods=['GET'])
def get_product(id):
    product = Product.query.get_or_404(id)
    product_schema = ProductSchema()
    return jsonify(product_schema.dump(product))

@app.route('/products', methods=['POST'])
def create_product():
    product_schema = ProductSchema()
    product = product_schema.load(request.get_json())
    db.session.add(product)
    db.session.commit()
    return jsonify(product_schema.dump(product)), 201

@app.route('/products/<id>', methods=['PUT'])
def update_product(id):
    product = Product.query.get_or_404(id)
    product_schema = ProductSchema()
    updated_product = product_schema.load(request.get_json(), instance=product)
    db.session.commit()
    return jsonify(product_schema.dump(updated_product))

@app.route('/products/<id>', methods=['DELETE'])
def delete_product(id):
    product = Product.query.get_or_404(id)
    db.session.delete(product)
    db.session.commit()
    return '', 204

# Orders
@app.route('/orders', methods=['POST'])
def create_order():
    order_schema = OrderSchema()
    order = order_schema.load(request.get_json())
    db.session.add(order)
    db.session.commit()
    return jsonify(order_schema.dump(order)), 201

@app.route('/orders/<order_id>/add_product/<product_id>', methods=['GET'])
def add_product_to_order(order_id, product_id):
    order = Order.query.get_or_404(order_id)
    product = Product.query.get_or_404(product_id)
    
    if product not in order.products:
        order.products.append(product)
        db.session.commit()
    return jsonify(OrderSchema().dump(order))

@app.route('/orders/<order_id>/remove_product/<product_id>', methods=['DELETE'])
def remove_product_from_order(order_id, product_id):
    order = Order.query.get_or_404(order_id)
    product = Product.query.get_or_404(product_id)
    if product in order.products:
        order.products.remove(product)
        db.session.commit()
    return '', 204

@app.route('/orders/user/<user_id>', methods=['GET'])
def get_orders_by_user(user_id):
    orders = Order.query.filter_by(user_id=user_id).all()
    return jsonify(OrderSchema(many=True).dump(orders))

@app.route('/orders/<order_id>/products', methods=['GET'])
def get_products_in_order(order_id):
    order = Order.query.get_or_404(order_id)
    return jsonify(ProductSchema(many=True).dump(order.products))

if __name__ == '__main__':
    app.run(debug=True)

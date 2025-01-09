from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy()

from .user import User
from .order import Order
from .product import Product
from .order_product import order_product

from sqlalchemy import Table, Column, Integer, ForeignKey
from models import db

order_product = Table('order_product', db.Model.metadata,
    Column('order_id', Integer, ForeignKey('orders.id', ondelete='CASCADE'), primary_key=True),
    Column('product_id', Integer, ForeignKey('products.id', ondelete='CASCADE'), primary_key=True)
)

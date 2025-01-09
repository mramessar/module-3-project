from datetime import datetime
from sqlalchemy import Column, Integer, DateTime, ForeignKey
from models import db

class Order(db.Model):
    __tablename__ = 'orders'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    order_date = Column(DateTime, default=datetime.utcnow)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    
    # Relationship with Products through Order_Product
    products = db.relationship('Product', secondary='order_product', backref='orders')
    
    def __repr__(self):
        return f'<Order {self.id} by User {self.user_id}>'

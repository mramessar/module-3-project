from datetime import datetime
from sqlalchemy import Column, Integer, String
from models import db

class User(db.Model):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    address = Column(String(200))
    email = Column(String(100), unique=True, nullable=False)
    
    # Relationship with Orders
    orders = db.relationship('Order', backref='user', lazy=True)
    
    def __repr__(self):
        return f'<User {self.name}>'
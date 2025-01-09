from sqlalchemy import Column, Integer, String, Float
from models import db

class Product(db.Model):
    __tablename__ = 'products'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    product_name = Column(String(100), nullable=False)
    price = Column(Float, nullable=False)
    
    def __repr__(self):
        return f'<Product {self.product_name}>'

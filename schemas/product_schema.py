from . import ma
from models.product import Product

class ProductSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Product

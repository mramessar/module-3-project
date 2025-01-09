from marshmallow import Schema, fields, validate

# User Schema
class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    address = fields.Str(required=True)
    email = fields.Email(required=True, validate=validate.Email(error="Invalid email"))
    
# Order Schema
class OrderSchema(Schema):
    id = fields.Int(dump_only=True)
    order_date = fields.DateTime(required=True)
    user_id = fields.Int(required=True)

# Product Schema
class ProductSchema(Schema):
    id = fields.Int(dump_only=True)
    product_name = fields.Str(required=True)
    price = fields.Float(required=True)
    
# Order-Product Association Schema
class OrderProductSchema(Schema):
    order_id = fields.Int(required=True)
    product_id = fields.Int(required=True)

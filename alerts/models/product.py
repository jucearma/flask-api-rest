from alerts.config import db
from marshmallow import fields
from marshmallow_sqlalchemy import ModelSchema


class Product(db.Model):
    __tablename__ = "products"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20))
    productDescription = db.Column(db.String(100))
    productBrand = db.Column(db.String(20))
    price = db.Column(db.Integer)

        
    def __init__(self, title, productDescription, productBrand, price):
        self.title = title
        self.productDescription = productDescription
        self.productBrand = productBrand
        self.price = price
        
    def __repr__(self):
        return '' % self.id
    
    def create(self):
        db.session.add(self)
        db.session.commit()
        return self


class ProductSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = Product
        sqla_session = db.session

    id = fields.Number(dump_only=True)
    title = fields.String(required=True)
    productDescription = fields.String(required=True)
    productBrand = fields.String(required=True)
    price = fields.Number(required=True)

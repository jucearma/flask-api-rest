from alerts.models.product import Product,ProductSchema
from alerts.config import db

product_schema = ProductSchema()
products_schema = ProductSchema(many=True)

class Product_Services:
    
    def add_product(self, product:Product):
        db.session.add(product)
        db.session.commit()


    def find_all_products(self):
        get_products = Product.query.all()
        return products_schema.dump(get_products)

    
    def get_product_by_id(self,id: int):
        get_product = Product.query.get_or_404(id)
        return product_schema.dump(get_product)

    
    def update_product_by_id(self, id:int, data):
        get_product = Product.query.get_or_404(id)
        if data.get('title'):
            get_product.title = data['title']
        if data.get('productDescription'):
            get_product.productDescription = data['productDescription']
        if data.get('productBrand'):
            get_product.productBrand = data['productBrand']
        if data.get('price'):
            get_product.price= data['price']    
        self.add_product(get_product)
        product_schema = ProductSchema(only=['id', 'title', 'productDescription','productBrand','price'])
        
        return product_schema.dump(get_product)

    
    def create_product(self,data):
        product = product_schema.load(data)
        return product_schema.dump(product.create())
    
    
    def delete_product_by_id(self, id):
        get_product = Product.query.get_or_404(id)
        db.session.delete(get_product)
        db.session.commit()
        return str("Product {} removed successfully".format(id))
        


from helper import helper
from apps.models.product import Product as ProductModel

class Product():
    def __init__(self, name=None, price=None, quantity=None):
        self.name = name
        self.price = price
        self.quantity = quantity

    #Agrega producto
    def add_product(self, pro, app):
        try:
            product = ProductModel
            product.insert({
                'name': pro.name,
                'price': pro.price,
                'quantity': pro.quantity
            })
            message = f'''Se agrego: {pro.name}, {pro.state}'''
            print(message)
            return helper.handler_response(app, 201, message)
        except Exception as e:
            return helper.handler_response(app, 500, f'{str(e)}')

    #Muestra las cantidades del producto
    def viewAll_product(self, app):
        try:
            product = ProductModel.get()
            result = {}
            if product:
                result = product.serialize()
            return helper.handler_response(app, 201, 'Lista de productos', result)
        except Exception as e:
            return helper.handler_response(app, 500, f'{str(e)}')
    
    #Busca 1 producto en especial
    def find_product(self, pro_id, app):
        try:
            product = ProductModel.where('product_id', pro_id).first()
            result = {}
            if product:
                result = product.serialize()
            return helper.handler_response(app, 201, f'Buscar product_id: {pro_id}', result)
        except Exception as e:
            return helper.handler_response(app, 500, f'{str(e)}')

    #Selecciona y Acrtualiza un producto:
    def update_product(self, pro, pro_id, app):
        try:
            product = ProductModel.where('product_id', pro_id)\
                .update({
                    'name': pro.name,
                    'price': pro.price,
                    'quantity': pro.quantity
                })
            message = f''' No se encontro el producto: {pro_id}'''
            
            if product > 0:
                message = f''' Se actualizo el producto: {pro_id}'''
            return helper.handler_response(app, 201, message)
        except Exception as e:
            return helper.handler_response(app, 500, f'{str(e)}')
    
    #Elimina un producto
    def delete_product(self, pro_id, app):
        try:
            product = ProductModel.where('product_id', pro_id).delete()
            message = f''' No se encontro el producto: {pro_id}'''
            if product > 0:
                message = f''' Se elimino el producto: {pro_id}'''
            print(message)
            return helper.handler_response(app, 201, message)
        except Exception as e:
            return helper.handler_response(app, 500, f'{str(e)}')
    
    #Busqueda por CUALQUIER CARACTERISTICA
    def select_product(self, pro_id, app):
        try:
            product = ProductModel\
                .where('product_id', pro_id)\
                .or_where('name', pro_id)\
                .or_where('price', pro_id)\
                .or_where('quantity', pro_id)\
                .get()
            result = {}
            if product:
                result = product.serialize()
            return helper.handler_response(app, 201, f'Buscar por: {pro_id}', result)
        except Exception as e:
            return helper.handler_response(app, 500, f'{str(e)}')

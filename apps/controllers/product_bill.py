from helper import helper
from apps.models.product_bill import Product_bill as ProductBillModel
from apps.models.product import Product as ProductModel
from apps.models.bill import Bill as BillModel

class Product_bill():
    def __init__(self, product_id=None, bill_id=None):
        self.product_id = product_id
        self.bill_id= bill_id

     #Agrega al LA TABLA MAESTRA PRODUCT_BILL
    def add_pb(self, probill, app):
        try:
            product = ProductModel.find(probill.product_id)
            bill = BillModel.find(probill.bill_id)
            if product and bill:
                ProductBillModel.insert({
                    'product_id': probill.product_id,
                    'bill_id': probill.bill_id
                })
                message = f'''Se agrego al registro: {probill.product_id}, {probill.bill_id}'''
                print(message)
                return helper.handler_response(app, 201, message)
            message = f''' NO SE PUDO REGISTRAR'''
            print(message)
            return helper.handler_response(app, 401, message)
        except Exception as e:
            return helper.handler_response(app, 500, f'{str(e)}')
    
     #Muestra las cantidades totales de la tb maestra
    def viewAll_pb(self, app):
        pb_dic = {}
        try:
            pb = ProductBillModel.get()
            pb.load('product_id', 'bill_id')
            pb_dic = pb.serialize()
            message = f''' Lista total del Pivote: RO_CO_US'''
            return helper.handler_response(app, 201, message, pb_dic)
        except Exception as e:
            return helper.handler_response(app, 500, f'{str(e)}')
    
    #Busca 1 registro
    def find_pb(self, pb_id, app):
        try:
            pb = ProductBillModel\
            .where('Product_bill_id', pb_id).first()
            result = {}
            if pb:
                result = pb.serialize()
            return helper.handler_response(app, 201, f'Buscar piv_id: {pb_id}', result)
        except Exception as e:
            return helper.handler_response(app, 500, f'{str(e)}')
    
    #Selecciona y Acrtualiza un Rol:
    def update_pb(self, pb, pb_id, app):
        try:
            product = ProductModel.find(pb.product_id)
            bill = BillModel.find(pb.bill_id)
            if product and bill:
                ProductBillModel\
                    .where('Product_bill_id', pb_id)\
                    .update({
                        'product_id': pb.product_id,
                        'bill_id': pb.bill_id
                })
                message = f''' Se actualizo el registro: {pb_id}'''
                print(message)
                return helper.handler_response(app, 201, message)
            message = '''No existe el registro: Empresa, Usuario, Rol'''
            print(message)
            return helper.handler_response(app, 401, message)
        except Exception as e:
            return helper.handler_response(app, 500, f'{str(e)}')
    
    #Elimina un registro
    def delete_pb(self, pb_id, app):
        try:
            pb = ProductBillModel.where('Product_bill_id', pb_id).delete()
            message = f''' No se encontro el registro: {pb_id}'''
            if pb > 0:
                message = f''' Se elimino al registro: {pb_id}'''
            print(message)
            return helper.handler_response(app, 201, message)
        except Exception as e:
            return helper.handler_response(app, 500, f'{str(e)}')
    
    #Busqueda por CUALQUIER CARACTERISTICA
    def select_pb(self, pb_id, app):
        try:
            pb = ProductBillModel\
                .where('Product_bill_id', pb_id)\
                .or_where('product_id', pb_id)\
                .or_where('bill_id', pb_id)\
                .get()
            result = {}
            if pb:
                result = pb.serialize()
            return helper.handler_response(app, 201, f'Buscar por: {pb_id}', result)
        except Exception as e:
            return helper.handler_response(app, 500, f'{str(e)}')
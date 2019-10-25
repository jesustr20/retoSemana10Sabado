from helper import helper
from apps.models.bill import Bill as BillModel

class Bill():
    def __init__(self, invIdenti=None, unitePrice=None, igv=None, totalPrice=None):
        self.invIdenti = invIdenti
        self.unitePrice = unitePrice
        self.igv = igv
        self.totalPrice = totalPrice

    #Agrega a la factura
    def add_factu(self, fact, app):
        try:
            factura = BillModel
            factura.insert({
                'invIdenti': fact.invIdenti,
                'unitePrice': fact.unitePrice,
                'igv': fact.igv,
                'totalPrice': fact.totalPrice
            })
            message = f'''Se agrego la factura: {fact.invIdenti}, {fact.unitePrice}, {fact.igv}, {fact.totalPrice}'''
            print(message)
            return helper.handler_response(app, 201, message)
        except Exception as e:
            return helper.handler_response(app, 500, f'{str(e)}')
    
    #Muestra las cantidades de factura
    def viewAll_factu(self, app):
        try:
            factura = BillModel.get()
            result = {}
            if factura:
                result = factura.serialize()
            return helper.handler_response(app, 201, 'Lista de factura', result)
        except Exception as e:
            return helper.handler_response(app, 500, f'{str(e)}')
    
    #Busca 1 factura en especial
    def find_factu(self, fact_id, app):
        try:
            factura = BillModel.where('bill_id', fact_id).first()
            result = {}
            if factura:
                result = factura.serialize()
            return helper.handler_response(app, 201, f'Buscar factura_id: {fact_id}', result)
        except Exception as e:
            return helper.handler_response(app, 500, f'{str(e)}')

    #Selecciona y Actualiza una factura:
    def update_factu(self, fact, fact_id, app):
        try:
            factura = BillModel.where.where('bill_id', fact_id)\
                .update({
                    'invIdenti': fact.invIdenti,
                    'unitePrice': fact.unitePrice,
                    'igv': fact.igv,
                    'totalPrice': fact.totalPrice
                })
            message = f''' No se encontro la factura: {fact_id}'''
            
            if factura > 0:
                message = f''' Se actualizo la factura: {fact_id}'''
            return helper.handler_response(app, 201, message)
        except Exception as e:
            return helper.handler_response(app, 500, f'{str(e)}')
    
    #Elimina una factura
    def delete_factu(self, fact_id, app):
        try:
            factura = BillModel.where('bill_id', fact_id).delete()
            message = f''' No se encontro la factura: {fact_id}'''
            if factura > 0:
                message = f''' Se elimino la factura: {fact_id}'''
            print(message)
            return helper.handler_response(app, 201, message)
        except Exception as e:
            return helper.handler_response(app, 500, f'{str(e)}')
    
    #Busqueda por CUALQUIER CARACTERISTICA
    def select_factu(self, fact_id, app):
        try:
            factura = BillModel\
                .where('bill_id', fact_id)\
                .or_where('invIdenti', fact_id)\
                .or_where('unitePrice', fact_id)\
                .or_where('igv', fact_id)\
                .or_where('totalPrice', fact_id)\
                .get()
            result = {}
            if factura:
                result = factura.serialize()
            return helper.handler_response(app, 201, f'Buscar por: {fact_id}', result)
        except Exception as e:
            return helper.handler_response(app, 500, f'{str(e)}')
#BODEGA
import jwt
from helper import helper
from apps.models.company import Company as CompanyModel

class Company():
    def __init__(self, ruc=None, name=None, address=None):
        self.ruc = ruc
        self.name = name
        self.address = address
    
    #Agrega companias
    def add_company(self, comp, app):
        try:
            compay = CompanyModel
            compay.insert({
                'ruc': comp.ruc,
                'name': comp.name,
                'address': comp.address
            })
            message = f'''Se agrego: {comp.ruc}, {comp.name}, {comp.address}'''
            print(message)
            return helper.handler_response(app, 201, message)
        except Exception as e:
            return helper.handler_response(app, 500, f'{str(e)}')
    
    #Muestra las companias
    def viewAll_company(self, app):
        try:
            company = CompanyModel.get()
            result = {}
            if company:
                result = company.serialize()
            return helper.handler_response(app, 201, 'Lista de Companias', result)
        except Exception as e:
            return helper.handler_response(app, 500, f'{str(e)}')
    
    #Busca 1 compania
    def find_company(self, comp_id, app):
        try:
            company = CompanyModel.where('company_id', comp_id).first()
            result = {}
            if company:
                result = company.serialize()
            return helper.handler_response(app, 201, f'Buscar company_id: {comp_id}', result)
        except Exception as e:
            return helper.handler_response(app, 500, f'{str(e)}')
        
    #Selecciona y Acrtualiza una compania:
    def update_company(self, comp, comp_id, app):
        try:
            company = CompanyModel.where('company_id', comp_id)\
                .update({
                    'ruc': comp.ruc,
                    'name': comp.name,
                    'address': comp.address
                })
            message = f''' No se encontro el usuario: {comp_id}'''
            
            if company > 0:
                message = f''' Se actualizo el usuario: {comp_id}'''
            return helper.handler_response(app, 201, message)
        except Exception as e:
            return helper.handler_response(app, 500, f'{str(e)}')
    
    #Elimina una compania
    def delete_company(self, comp_id, app):
        try:
            company = CompanyModel.where('company_id', comp_id).delete()
            message = f''' No se encontro la Compania: {comp_id}'''
            if company > 0:
                message = f''' Se elimino la compania: {comp_id}'''
            print(message)
            return helper.handler_response(app, 201, message)
        except Exception as e:
            return helper.handler_response(app, 500, f'{str(e)}')
    
    #Busqueda por CUALQUIER CARACTERISTICA
    def select_company(self, comp_id, app):
        try:
            company = CompanyModel\
                .where('company_id', comp_id)\
                .or_where('ruc', comp_id)\
                .or_where('name', comp_id)\
                .or_where('address', comp_id)\
                .get()
            result = {}
            if company:
                result = company.serialize()
            return helper.handler_response(app, 201, f'Buscar por: {comp_id}', result)
        except Exception as e:
            return helper.handler_response(app, 500, f'{str(e)}')
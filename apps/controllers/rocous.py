#Pivote
from helper import helper
from apps.models.rocous import Rocous as PivoteModel
from apps.models.rocous import CompanyModel
from apps.models.rocous import RoleModel
from apps.models.rocous import UsersModel

class Pivote():
    def __init__(self, company_id=None, users_id=None, role_id=None):
        self.company_id = company_id
        self.users_id= users_id
        self.role_id = role_id

    #Agrega al LA TABLA MAESTRA
    def add_pivote(self, pivote, app):
        try:
            company = CompanyModel.find(pivote.company_id)
            user = UsersModel.find(pivote.users_id)
            role = RoleModel.find(pivote.role_id)
            if company and user and role:
                PivoteModel.insert({
                    'company_id': pivote.company_id,
                    'users_id': pivote.users_id,
                    'role_id': pivote.role_id
                })
                message = f'''Se agrego al registro: {pivote.company_id}, {pivote.users_id}, {pivote.role_id}'''
                print(message)
                return helper.handler_response(app, 201, message)
            message = f''' NO SE PUDO REGISTRAR'''
            print(message)
            return helper.handler_response(app, 401, message)
        except Exception as e:
            return helper.handler_response(app, 500, f'{str(e)}')
    
    #Muestra las cantidades totales de la tb maestra
    def viewAll_pivote(self, app):
        piv_dic = {}
        try:
            piv = PivoteModel.get()
            piv.load('company', 'role', 'users')
            piv_dic = piv.serialize()
            message = f''' Lista total del Pivote: RO_CO_US'''
            return helper.handler_response(app, 201, message, piv_dic)
        except Exception as e:
            return helper.handler_response(app, 500, f'{str(e)}')

    #Busca 1 registro
    def find_pivote(self, piv_id, app):
        try:
            piv = PivoteModel\
            .where('ro_co_us_id', piv_id).first()
            result = {}
            if piv:
                result = piv.serialize()
            return helper.handler_response(app, 201, f'Buscar piv_id: {piv_id}', result)
        except Exception as e:
            return helper.handler_response(app, 500, f'{str(e)}')
    
    #Selecciona y Acrtualiza un Rol:
    def update_pivote(self, pivote, piv_id, app):
        try:
            company = CompanyModel.find(pivote.company_id)
            user = UsersModel.find(pivote.users_id)
            role = RoleModel.find(pivote.role_id)
            if company and user and role:
                PivoteModel\
                    .where('ro_co_us_id', piv_id)\
                    .update({
                        'company_id': pivote.company_id,
                        'users_id': pivote.users_id,
                        'role_id': pivote.role_id
                })
                message = f''' Se actualizo el registro: {piv_id}'''
                print(message)
                return helper.handler_response(app, 201, message)
            message = '''No existe el registro: Empresa, Usuario, Rol'''
            print(message)
            return helper.handler_response(app, 401, message)
        except Exception as e:
            return helper.handler_response(app, 500, f'{str(e)}')
    
    #Elimina un registro
    def delete_pivote(self, piv_id, app):
        try:
            pivote = PivoteModel.where('ro_co_us_id', piv_id).delete()
            message = f''' No se encontro el registro: {piv_id}'''
            if pivote > 0:
                message = f''' Se elimino al registro: {piv_id}'''
            print(message)
            return helper.handler_response(app, 201, message)
        except Exception as e:
            return helper.handler_response(app, 500, f'{str(e)}')
    
    #Busqueda por CUALQUIER CARACTERISTICA
    def select_pivote(self, piv_id, app):
        try:
            pivote = PivoteModel\
                .where('ro_co_us_id', piv_id)\
                .or_where('company_id', piv_id)\
                .or_where('users_id', piv_id)\
                .or_where('role_id', piv_id)\
                .get()
            result = {}
            if pivote:
                result = pivote.serialize()
            return helper.handler_response(app, 201, f'Buscar por: {piv_id}', result)
        except Exception as e:
            return helper.handler_response(app, 500, f'{str(e)}')
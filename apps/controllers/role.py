#ROL
from helper import helper
from apps.models.role import Role as RoleModel

class Role():
    def __init__(self, name=None, state=None):
        self.name = name
        self.state = state
    
    #Agrega el rol
    def add_role(self, rol, app):
        try:
            role = RoleModel
            role.insert({
                'name': rol.name,
                'state': rol.state
            })
            message = f'''Se agrego: {rol.name}, {rol.state}'''
            print(message)
            return helper.handler_response(app, 201, message)
        except Exception as e:
            return helper.handler_response(app, 500, f'{str(e)}')
    
    #Muestra las cantidades de rol
    def viewAll_role(self, app):
        try:
            role = RoleModel.get()
            result = {}
            if role:
                result = role.serialize()
            return helper.handler_response(app, 201, 'Lista de Roles', result)
        except Exception as e:
            return helper.handler_response(app, 500, f'{str(e)}')
    
    #Busca 1 Rol en especial
    def find_role(self, rol_id, app):
        try:
            role = RoleModel.where('role_id', rol_id).first()
            result = {}
            if role:
                result = role.serialize()
            return helper.handler_response(app, 201, f'Buscar rol_id: {rol_id}', result)
        except Exception as e:
            return helper.handler_response(app, 500, f'{str(e)}')
    
    #Selecciona y Acrtualiza un Rol:
    def update_role(self, rol, rol_id, app):
        try:
            role = RoleModel.where('role_id', rol_id)\
                .update({
                    'name': rol.name,
                    'state': rol.state
                })
            message = f''' No se encontro el rol: {rol_id}'''
            
            if role > 0:
                message = f''' Se actualizo el rol: {rol_id}'''
            return helper.handler_response(app, 201, message)
        except Exception as e:
            return helper.handler_response(app, 500, f'{str(e)}')

    #Elimina un Rol
    def delete_role(self, rol_id, app):
        try:
            role = RoleModel.where('role_id', rol_id).delete()
            message = f''' No se encontro el rol: {rol_id}'''
            if role > 0:
                message = f''' Se elimino el rol: {rol_id}'''
            print(message)
            return helper.handler_response(app, 201, message)
        except Exception as e:
            return helper.handler_response(app, 500, f'{str(e)}')
    
    #Busqueda por CUALQUIER CARACTERISTICA
    def select_role(self, rol_id, app):
        try:
            role = RoleModel\
                .where('role_id', rol_id)\
                .or_where('name', rol_id)\
                .or_where('state', rol_id)\
                .get()
            result = {}
            if role:
                result = role.serialize()
            return helper.handler_response(app, 201, f'Buscar por: {rol_id}', result)
        except Exception as e:
            return helper.handler_response(app, 500, f'{str(e)}')
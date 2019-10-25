#Usuario
import jwt
import bcrypt
from helper import helper
from apps.models.users import Users as UsersModel

class Users():
    def __init__(self, name=None, last_name=None, user=None, password=None, state=None):
        self.name = name
        self.last_name= last_name
        self.user = user
        self.password = password
        self.state = state
    
    #LOGIN
    def login(self, app, username, password):
        try:
            user_found = UsersModel.where_user(username).first()
            if user_found and user_found.password_valid(password):
                return helper.handler_response(app, 201, 'Logeado con exito')           
            message = f'El usuario y/o contraseña son incorrectas: {username}'
            return helper.handler_response(app, 401, message)
        except Exception as e:
            return helper.handler_response(app, 500, f'{str(e)}')


    #Agrega al usuario
    def add_user(self, users, app):
        try:
            #Ingresando para la encriptacion
            hash_pw = bcrypt.hashpw(users.password.encode('utf-8'), bcrypt.gensalt())
            user = UsersModel
            user.insert({
                'name': users.name,
                'last_name': users.last_name,
                'user': users.user,
                'password': hash_pw,
                'state': users.state
            })
            message = f'''Se agrego al usuario: {users.name}, {users.last_name}, {users.user}'''
            print(message)
            return helper.handler_response(app, 201, message)
        except Exception as e:
            return helper.handler_response(app, 500, f'{str(e)}')
    
    #Muestra las cantidades de usuarios
    def viewAll_user(self, app):
        try:
            user = UsersModel.get()
            result = {}
            if user:
                result = user.serialize()
            return helper.handler_response(app, 201, 'Lista de Usuarios', result)
        except Exception as e:
            return helper.handler_response(app, 500, f'{str(e)}')
    
    #Busca 1 Usuario en especial
    def find_user(self, users_id, app):
        try:
            user = UsersModel.where('users_id', users_id).first()
            result = {}
            if user:
                result = user.serialize()
            return helper.handler_response(app, 201, f'Buscar user_id: {users_id}', result)
        except Exception as e:
            return helper.handler_response(app, 500, f'{str(e)}')
    
    #Selecciona y Acrtualiza un Rol:
    def update_users(self, user, user_id, app):
        try:
            hash_pw = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt())
            users = UsersModel.where('users_id', user_id)\
                .update({
                    'name': user.name,
                    'last_name': user.last_name,
                    'user': user.user,
                    'password': hash_pw,
                    'state': user.state
                })
            message = f''' No se encontro al usuario: {user_id}'''
            
            if users > 0:
                message = f''' Se actualizo al usuario: {user_id}'''
            return helper.handler_response(app, 201, message)
        except Exception as e:
            return helper.handler_response(app, 500, f'{str(e)}')
    
    #Elimina un Rol
    def delete_users(self, user_id, app):
        try:
            user = UsersModel.where('users_id', user_id).delete()
            message = f''' No se encontro el usuario: {user_id}'''
            if user > 0:
                message = f''' Se elimino al usuario: {user_id}'''
            print(message)
            return helper.handler_response(app, 201, message)
        except Exception as e:
            return helper.handler_response(app, 500, f'{str(e)}')
    
    #Busqueda por CUALQUIER CARACTERISTICA
    def select_users(self, user_id, app):
        try:
            user = UsersModel\
                .where('users_id', user_id)\
                .or_where('name', user_id)\
                .or_where('last_name', user_id)\
                .or_where('user', user_id)\
                .or_where('state', user_id)\
                .get()
            result = {}
            if user:
                result = user.serialize()
            return helper.handler_response(app, 201, f'Buscar por: {user_id}', result)
        except Exception as e:
            return helper.handler_response(app, 500, f'{str(e)}')
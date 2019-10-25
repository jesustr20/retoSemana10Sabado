from flask import request
from helper import helper
from apps.controllers.users import Users
from routes.auth import route as route_auth

user = Users()

def route(app):
    @app.route('/user')
    def user_lista():
        return '<h1>Lista de Usuarios...</h1>'

    #Login
    route_auth.auth(app, user)

    #Agregar un usuario
    @app.route('/user/add', methods=['POST'])
    def user_add():
        values = request.values
        user.name = values.get('nombre')
        user.last_name = values.get('apellido')
        user.user = values.get('usuario')
        user.password = values.get('password')
        user.state = values.get('estado')
        return user.add_user(user, app)
    
    #Mostrar Usuarios
    @app.route('/user/view', methods=['GET'])
    def user_viewAll():
        return user.viewAll_user(app)
    
    #Busca solo 1 usuario especifico
    @app.route('/user/find', methods=['GET'])
    def user_find():
        values = request.values
        user_id = values.get('id')
        return user.find_user(user_id, app)
    
    #Buscar Rol por ID y Edita
    @app.route('/user/update', methods=['PUT'])
    def user_update():
        values = request.values
        user_id = values.get('id')
        user.name = values.get('nombre')
        user.last_name = values.get('apellido')
        user.user = values.get('usuario')
        user.password = values.get('password')
        user.state = values.get('estado')
        return user.update_users(user, user_id, app)
    
    #Elimina un usuario
    @app.route('/user/delete', methods=['DELETE'])
    def user_delete():
        values = request.values
        user_id = values.get('id')
        return user.delete_users(user_id, app)
    
    #Buscar Rol por Cualquier tipo
    @app.route('/user/select', methods=['GET'])
    def user_select():
        values = request.values
        user_id = values.get('id')
        return user.select_users(user_id, app)
from flask import request
from helper import helper
from apps.controllers.role import Role

rol = Role()

def route(app):
    @app.route('/rols')
    def role_lista():
        return '<h1>Lista de Roles...</h1>'

    #Agregar Rol
    @app.route('/role/add', methods=['POST'])
    def role_add():
        values = request.values
        rol.name = values.get('nombre')
        rol.state = values.get('estado')
        return rol.add_role(rol, app)

    #Mostrar Roles
    @app.route('/role/view', methods=['GET'])
    def role_viewAll():
        return rol.viewAll_role(app)
    
    #Busca solo 1 rol
    @app.route('/role/find', methods=['GET'])
    def role_find():
        values = request.values
        rol_id = values.get('id')
        return rol.find_role(rol_id, app)
    
    #Buscar Rol por ID y Editar
    @app.route('/role/update', methods=['PUT'])
    def role_update():
        values = request.values
        rol_id = values.get('id')
        rol.name = values.get('nombre')
        rol.state = values.get('estado')
        return rol.update_role(rol, rol_id, app)
    
    #Elimina un rol
    @app.route('/role/delete', methods=['DELETE'])
    def role_delete():
        values = request.values
        rol_id = values.get('id')
        return rol.delete_role(rol_id, app)

    #Buscar Rol por Cualquier tipo
    @app.route('/role/select', methods=['GET'])
    def role_select():
        values = request.values
        rol_id = values.get('id')
        return rol.select_role(rol_id, app)
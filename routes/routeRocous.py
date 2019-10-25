from flask import request
from helper import helper
from apps.controllers.rocous import Pivote

piv = Pivote()

def route(app):
    @app.route('/pivote')
    def pivote_lista():
        return '<h1>Lista de registros agregados...</h1>'

    #Agregar Rol
    @app.route('/pivote/add', methods=['POST'])
    def pivote_add():
        values = request.values
        piv.company_id = values.get('empresa_id')
        piv.users_id = values.get('usuario_id')
        piv.role_id = values.get('rol_id')
        return piv.add_pivote(piv, app)

    #Mostrar Roles
    @app.route('/pivote/view', methods=['GET'])
    def pivote_viewAll():
        return piv.viewAll_pivote(app)
    
    #Busca solo 1 rol
    @app.route('/pivote/find', methods=['GET'])
    def pivote_find():
        values = request.values
        piv_id = values.get('id')
        return piv.find_pivote(piv_id, app)
    
    #Buscar Rol por ID y Editar
    @app.route('/pivote/update', methods=['PUT'])
    def pivote_update():
        values = request.values
        piv_id = values.get('id')
        piv.company_id = values.get('empresa_id')
        piv.users_id = values.get('usuario_id')
        piv.role_id = values.get('rol_id')
        return piv.update_pivote(piv, piv_id, app)
    
    #Elimina un rol
    @app.route('/pivote/delete', methods=['DELETE'])
    def pivote_delete():
        values = request.values
        piv_id = values.get('id')
        return piv.delete_pivote(piv_id, app)

    #Buscar Rol por Cualquier tipo
    @app.route('/pivote/select', methods=['GET'])
    def pivote_select():
        values = request.values
        piv_id = values.get('id')
        return piv.select_pivote(piv_id, app)
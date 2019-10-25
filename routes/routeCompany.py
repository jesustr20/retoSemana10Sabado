from flask import request
from helper import helper
from apps.controllers.company import Company

comp = Company()

def route(app):
    @app.route('/')
    def company_listay():
        return '<h1>Lista de Empresas...</h1>'
    
    #Agregar Compania
    @app.route('/company/add', methods=['POST'])
    def company_add():
        values = request.values
        comp.ruc = values.get('ruc')
        comp.name = values.get('nombre')
        comp.address = values.get('direccion')
        return comp.add_company(comp, app)

    #Mostrar Companias
    @app.route('/company/view', methods=['GET'])
    def company_viewAll():
        return comp.viewAll_company(app)
    
    #Busca solo 1 compania
    @app.route('/company/find', methods=['GET'])
    def company_find():
        values = request.values
        comp_id = values.get('id')
        return comp.find_company(comp_id, app)
    
    #Buscar compania por ID y Editar
    @app.route('/company/update', methods=['PUT'])
    def company_update():
        values = request.values
        comp_id = values.get('id')
        comp.ruc = values.get('ruc')
        comp.name = values.get('nombre')
        comp.address = values.get('direccion')
        return comp.update_company(comp, comp_id, app)
    
    #Elimina una compania
    @app.route('/company/delete', methods=['DELETE'])
    def company_delete():
        values = request.values
        comp_id = values.get('id')
        return comp.delete_company(comp_id, app)
    
    #Buscar COMPANia por Cualquier tipo
    @app.route('/company/select', methods=['GET'])
    def company_select():
        values = request.values
        comp_id = values.get('id')
        return comp.select_company(comp_id, app)

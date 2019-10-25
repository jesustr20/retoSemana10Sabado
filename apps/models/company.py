from database.config import Conexion

conn = Conexion()
Model = conn.model()

class Company(Model):
    __table__ = 'company'
    __primary_key__ = 'company_id'
    __timestamps__ = True
    __connection__ = 'mysql'

    __fillable__ = ['ruc', 'name', 'address']

    __casts__ = {
        'ruc': 'str',
        'name': 'str',
        'address': 'str'
    }

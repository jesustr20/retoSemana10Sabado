from database.config import Conexion

conn = Conexion()
Model = conn.model()

class Role(Model):
    __table__ = 'role'
    __primary_key__ = 'role_id'
    __timestamps__ = True
    __connection__ = 'mysql'

    __fillable__ = ['name', 'state']

    __casts__ = {
        'name': 'str',
        'state': 'str'
    }
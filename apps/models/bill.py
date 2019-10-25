from database.config import Conexion

conn = Conexion()
Model = conn.model()

class Bill(Model):
    __table__ = 'bill'
    __primary_key__ = 'bill_id'
    __timestamps__ = True
    __connection__ = 'mysql'

    __fillable__ = ['invIdenti', 'unitePrice', 'igv', 'totalPrice']

    __casts__ = {
        'invIdenti': 'int',
        'unitePrice': 'float',
        'igv': 'float',
        'totalPrice': 'float'
    }
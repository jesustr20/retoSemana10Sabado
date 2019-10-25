from database.config import Conexion
from orator.orm import belongs_to
from apps.models.product import Product as ProductModel
from apps.models.bill import Bill as BillModel


conn = Conexion()
Model = conn.model()

class Product_bill(Model):
    __table__ = 'rocous'
    __primary_key__ = 'Product_bill_id'
    __timestamps__ = True
    __connection__ = 'mysql'

    __fillable__ = ['product_id', 'bill_id']

    __casts__ = {
        'product_id': 'int',
        'bill_id': 'int'
    }

    @belongs_to
    def product(self):
        return ProductModel

    @belongs_to
    def bill(self):
        return BillModel
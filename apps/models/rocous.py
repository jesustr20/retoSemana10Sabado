from database.config import Conexion
from orator.orm import belongs_to
from apps.models.company import Company as CompanyModel
from apps.models.role import Role as RoleModel
from apps.models.users import Users as UsersModel

conn = Conexion()
Model = conn.model()

class Rocous(Model):
    __table__ = 'rocous'
    __primary_key__ = 'ro_co_us_id'
    __timestamps__ = True
    __connection__ = 'mysql'

    __fillable__ = ['company_id', 'users_id', 'role_id']

    __casts__ = {
        'company_id': 'int',
        'users_id': 'int',
        'role_id': 'int'
    }

    @belongs_to
    def company(self):
        return CompanyModel

    @belongs_to
    def role(self):
        return RoleModel

    @belongs_to
    def users(self):
        return UsersModel

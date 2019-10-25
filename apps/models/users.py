from database.config import Conexion
import bcrypt

conn = Conexion()
Model = conn.model()

class Users(Model):
    __table__ = 'users'
    __primary_key__ = 'users_id'
    __timestamps__ = True
    __connection__ = 'mysql'

    __hidden__ = ['password']
    __fillable__ = ['name', 'last_name', 'user', 'password', 'state']

    __casts__ = {
        'name': 'str',
        'last_name': 'str',
        'user': 'str',
        'password': 'str',
        'state': 'str'
    }

    def password_valid(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.password.encode('utf-8'))
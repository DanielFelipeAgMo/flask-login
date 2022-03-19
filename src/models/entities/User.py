from werkzeug.security import check_password_hash #, generate_password_hash
from flask_login import UserMixin


class User(UserMixin):
   #Clase constructora con init
    def __init__(self, id, username, password, fullname="") -> None:
        self.id = id
        self.username = username
        self.password = password
        self.fullname = fullname

    @classmethod #@el decorador nos evita intanciar la clase            #password desde BD  y password en texto plano
    def check_password(self, hashed_password, password):
        return check_password_hash(hashed_password, password)

#print(generate_password_hash("soytdea"))
# Para generar una nueva clave de tipo hash  python .\src\models\entities\User.py
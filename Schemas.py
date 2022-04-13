#Schema utiliza un "Meta" que mapea los campos de la base de datos
# a un objeto python serializado.

from Models import User
from config import ma 
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

#class UserSchema(ma.Schema):
#    class Meta:
#        fields = ('id','name','lastname')

#Schema que genera automaticamente a partir de un modelo o tabla de SQLAlchemy
# el modelo se asigna mediante la opción model en la clase Meta
class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = User

user_schema = UserSchema()
users_schema = UserSchema(many=True)
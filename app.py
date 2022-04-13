from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from config import app,db
from Models import User
from Schemas import user_schema, users_schema

@app.route('/')
def hello():
    return 'Hello World!'
    
@app.route('/a/', methods=['GET'])
def add():
    name = request.args['name']
    lastname = request.args['lastname']
    user = User(name=name, lastname=lastname)
    db.session.add(user)
    db.session.commit()
    if user.id is None:
        return 'Usuario no agregado'
    return f'Usuario con id { user.id } agregado con exito'

@app.route('/user/<int:id>', methods=["GET"])
def search(id):
    results = User.query.get(id)
    return user_schema.dumps(results)

@app.route('/d/<string:nom>', methods=['GET','DELETE'])
def delete(nom):
    result = User.query.filter_by(name=nom).first()
    if result is not None:
        db.session.delete(result)
        db.session.commit()
        return f'Usuario {nom} eliminado'
    else:
        return f'Usuario no encontrado'

if __name__ == '__main__':
    app.run(debug=True)

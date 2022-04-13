from config import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), nullable= False, default="XD")
    lastname = db.Column(db.String(100), unique= False, nullable = False)

    def __repr__(self):
        return '<User %r> ' % self.name

    def __init__(self,name,lastname):
        self.name = name
        self.lastname = lastname
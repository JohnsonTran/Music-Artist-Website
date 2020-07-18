from ..app import db

# database model to represent merch information
class Merch(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(500))
    name = db.Column(db.String(500))
    price = db.Column(db.Float)
    filename = db.Column(db.String(500))
    quantity = db.Column(db.Integer)

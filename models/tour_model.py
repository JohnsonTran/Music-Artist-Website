from ..app import db

# database model to represent tour information
class Tour(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(500))
    venue = db.Column(db.String(500))
    tickets = db.Column(db.Integer)
    date = db.Column(db.DateTime)
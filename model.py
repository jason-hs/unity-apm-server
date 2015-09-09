from sqlalchemy.dialects.postgresql import JSON

from core import db

class Package(db.Model):
    id = db.Column(db.Integer, primary_key = True)

    name = db.Column(db.Text)


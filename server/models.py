from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin

metadata = MetaData()

db = SQLAlchemy()

# Add models here
class Production(db.Model, SerializerMixin):
    __tablename__ = "productions"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    genre = db.Column(db.String)
    budget = db.Column(db.Integer)
    director = db.Column(db.Integer)
    description = db.Column(db.String)
    ongoing = db.Column(db.Boolean)

    def __repr__(self):
        return f"<Production {self.id}, {self.title}, {self.genre}, {self.budget}, {self.director}, {self.description}, {self.ongoing}>"
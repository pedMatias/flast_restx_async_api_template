from datetime import datetime

from template_api.ws import db


class ExampleModel(db.Model):
    """ Learn more about SQLAlchemy models at
        https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/"""
    __tablename__ = 'example_model'
    __table_args__ = {'extend_existing': True}
    
    id = db.Column(db.Integer, primary_key=True)
    field1 = db.Column(db.Float, nullable=False)
    field2 = db.Column(db.Boolean, nullable=False)
    field3 = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    field4 = db.Column(db.Integer, nullable=False, default=-1)


db.create_all()

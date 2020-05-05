from datetime import datetime
from template_api.ws import db


class AppModel(db.Model):
    md5sum = db.Column(db.String(32), primary_key=True)
    package = db.Column(db.String(120), nullable=False)
    name = db.Column(db.String(20), nullable=False)
    age_rating = db.Column(db.String(10), nullable=False)
    url = db.Column(db.String(120), nullable=False)
    images = db.relationship('ImageModel', cascade="all,delete", backref="image")
    result = db.relationship('FinalResultModel', backref='app_result', cascade="all,delete")

    def __repr__(self):
        return f"App('{self.md5sum}', '{self.name}', '{self.age_rating}', '{self.url}')"


class ImageModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    path = db.Column(db.String(120), nullable=False)
    is_icon = db.Column(db.Boolean, nullable=False)
    app_md5sum = db.Column(db.Integer, db.ForeignKey('app_model.md5sum'), nullable=False)
    result = db.relationship('ImageResultModel', backref='image_result', cascade="all,delete", lazy=True)

    def __repr__(self):
        return f"Image('{self.path}', {'icon' if self.is_icon else 'screenshot'})"


class ImageResultModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    result = db.Column(db.Float, nullable=False)
    individual_nsfw = db.Column(db.String(100), nullable=False)
    result_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    external_validator = db.Column(db.Integer, nullable=False, default=-1)
    image_id = db.Column(db.Integer, db.ForeignKey('image_model.id'), nullable=False)

    def __repr__(self):
        return f"ImageResult('{self.result}', '{self.result_date}', '{self.individual_nsfw}')"


class FinalResultModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    result = db.Column(db.Float, nullable=False)
    is_mature = db.Column(db.Boolean, nullable=False)
    result_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    external_validator = db.Column(db.Integer, nullable=False, default=-1)
    app_md5sum = db.Column(db.Integer, db.ForeignKey('app_model.md5sum'), nullable=False)

    def __repr__(self):
        return f"FinalResult('{self.result}', '{self.is_mature}', '{self.result_date}')"


db.create_all()
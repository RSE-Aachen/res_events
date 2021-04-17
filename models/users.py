from .shared import db
from sqlalchemy_utils import EmailType


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(EmailType)
    password_hashed = db.Column(db.String)
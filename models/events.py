from .shared import db


class Event(db.Model):
    __abstract__ = True
    title = db.Column(db.String(100))
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    remark = db.Column(db.String(100))
    url = db.Column(db.String)
    fee = db.Column(db.Float)


class OnlineEvent(Event):
    __tablename__ = "OnlineEvents"
    id = db.Column(db.Integer, primary_key=True)


class LiveEvent(Event):
    __tablename__ = "LiveEvents"
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(40))
    country = db.Column(db.String(30))
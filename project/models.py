from sqlalchemy import ForeignKey
from . import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    age = db.Column(db.Integer)
    
class Donations(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    amount = db.Column(db.Integer)
    campaign_id = db.Column(db.Integer, ForeignKey('campaigns.id'))

class Campaigns(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(1000), unique=True)
    start_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)
    campaign_type = db.Column(db.String(1000)) # type of campaign e.g. fundraiser, donation drive, etc., rmb to validate in the backend
    description = db.Column(db.String(1000))
    progress = db.Column(db.Integer)
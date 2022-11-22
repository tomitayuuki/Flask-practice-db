from datetime import datetime
from apps.app import db

class User(db.Model):
    __tablename__="users"
    id=db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String, index=True)
    email=db.Column(db.String, index=True)
    created_at=db.Column(db.DateTime, default=datetime.now)
    updated_at=db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

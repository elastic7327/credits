"""
File: users.py
Author: Me
Email: yourname@email.com
Github: https://github.com/yourname
Description:
"""

from datetime import datetime

from src.flaskr import db


class User(db.Model):
    __tablename__ = 'usdart_admin'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    nickname = db.Column(db.String(1024), nullable=True)

    created_at = db.Column(
            db.DateTime,
            nullable=False, default=datetime.utcnow)

    updated_at = db.Column(
            db.DateTime,
            nullable=True, onupdate=datetime.utcnow)

    deleted_at = db.Column(db.DateTime, nullable=True)

    def __repr__(self):
        return '<User %r>' % self.username

    def __str__(self):
        return "User(id='%s')" % self.id

    def to_json(self):
        return {
            "id": self.id,
            "username": self.username,
        }

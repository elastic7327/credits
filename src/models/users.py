"""
File: users.py
Author: Me
Email: yourname@email.com
Github: https://github.com/yourname
Description:
"""

from src.flaskr import db


class User(db.Model):
    __tablename__ = 'usdart_admin'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    nickname = db.Column(db.String(1024), nullable=True)
    password = db.Column(db.String(1024), nullable=False)
    email = db.Column(db.String(1024), nullable=False)
    is_staff = db.Column(db.Boolean, default=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    def __str__(self):
        return "User(id='%s')" % self.id

    def to_json(self):
        return {
            "id": self.id,
            "username": self.username,
            "nickname": self.nickname,
            "email": self.email,
            "is_staff": self.is_staff
        }

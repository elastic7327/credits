"""
File: users.py
Author: Me
Email: yourname@email.com
Github: https://github.com/yourname
Description:
"""

from datetime import datetime

from sqlalchemy.orm import validates

from src.modules.luhn import luhn
from src.flaskr import db


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)

    card_holder_name = db.Column(db.String(50), nullable=False)

    #  TODO:  <08-07-18, Daniel> #
    #  내부적으로, Ashper을 구현해서, 저장하는 방법도.. SecretKey필요

    card_no = db.Column(db.String(500), unique=True, nullable=False)

    limitation = db.Column(db.Integer, nullable=False)

    created_at = db.Column(
            db.DateTime,
            nullable=False, default=datetime.utcnow)

    updated_at = db.Column(
            db.DateTime,
            nullable=True, onupdate=datetime.utcnow)

    deleted_at = db.Column(db.DateTime, nullable=True)

    def __repr__(self):
        return '<User %r>' % self.card_holder_name

    def __str__(self):
        return "User(id='%s')" % self.id

    @validates('card_no')
    def validate_card_no(self, key, card_no):
        assert len(card_no) <= 19, "CardLengthError!"
        assert luhn(card_no) is True, "CardNumberError!"
        return card_no

    def to_json(self):
        return {
            "id": self.id,
            "username": self.username,
        }

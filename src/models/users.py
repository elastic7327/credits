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

    username = db.Column(db.String(50), nullable=False)

    limitation = db.Column(db.Integer, nullable=False, default=0)

    balance = db.Column(db.Integer, nullable=False, default=0)

    card_no = db.Column(db.String(500), unique=True, nullable=False)

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

    @validates('balance')
    def validate_balance_with_limitation(self, key, balance):
        assert abs(balance) <= self.limitation, "OverCharged!!"
        return balance

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

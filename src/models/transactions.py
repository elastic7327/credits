"""
File: transactions.py
Author: Me
Email: yourname@email.com
Github: https://github.com/yourname
Description:
"""

from datetime import datetime
from src.flaskr import db


class Transaction(db.Model):
    __tablename__ = 'transaction'

    id = db.Column(db.Integer, primary_key=True)

    tram = db.Column(db.Integer, nullable=False)  # 트렌젝션 어마운트

    type = db.Column(db.Integer, nullable=False)  # 0 Charge, Credit

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    label = db.Column(db.String(20), nullable=False)  # Charge, Credit

    is_valid = db.Column(db.Integer, default=0, nullable=False)  # 모든 트렌젝션의 default 값들은 0 으로, 유효하지 않습니다.

    created_at = db.Column(
            db.DateTime,
            nullable=False, default=datetime.utcnow)

    updated_at = db.Column(
            db.DateTime,
            nullable=True, onupdate=datetime.utcnow)

    deleted_at = db.Column(db.DateTime, nullable=True)

    def __repr__(self):
        return '<Transaction %r>' % self.label

    def __str__(self):
        return "Transaction(id='%s')" % self.id

    def to_json(self):
        return {
            "id": self.id,
            "username": self.username,
        }

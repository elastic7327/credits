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
            "user_id": self.user_id,
            "type": self.type,
            "label": self.label,
            "created_at": self.created_at,
            "tram": self.tram,
        }

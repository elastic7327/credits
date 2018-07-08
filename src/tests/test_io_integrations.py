"""
File: test_io_integrations.py
Author: dan
Email: elastic7327@email.com
Github: https://github.com/elastic7327
Description:
"""

from src.tests.common.base import TestBaseClass
from src.models.users import User
from src.models.transactions import Transaction
from src.flaskr import db

# import pytest


def Add(values):

    username = values[0]
    card_no = values[1]
    limitation = int(values[2][1:])

    try:
        o = User(
                username=username,
                card_no=card_no,
                limitation=limitation)

        db.session.add(o)
        db.session.commit()

    except Exception as e:
        print(f"{username}: error")


def Charge(values):

    try:
        username = values[0]
        amount = values[1][1:]

        uo = User.query.filter_by(
                username=username).one()

        tr = Transaction(
                user_id=uo.id,
                tram=amount,
                type=1,
                label=f'{username} Charge {amount}')

        uo.balance += int(amount)

        db.session.add(tr)
        db.session.commit()

        print(f"{username}: ${amount}")

    except Exception as e:
        print(f"{username}: error")


def Credit(values):

    try:
        username = values[0]
        amount = values[1][1:]

        uo = User.query.filter_by(
                username=username).one()

        tr = Transaction(
                user_id=uo.id,
                tram=amount,
                type=0,
                label=f'{username} Credit {amount} at the Sumgo Shop')

        uo.balance -= int(amount)

        db.session.add(tr)
        db.session.commit()

        print(f"{username}: $-{amount}")

    except Exception as e:
        print(f"{username}: error")


class TestIOClass(TestBaseClass):

    def test_read_input_sample(self):
        filename = 'src/tests/input_sample.txt'
        with open(filename, 'r') as f:
            for k, line in enumerate(f):

                try:

                    ip = line.split()

                    if ip[0] == "Add":
                        Add(ip[1:])
                    elif ip[0] == "Charge":
                        Charge(ip[1:])
                    elif ip[0] == "Credit":
                        Credit(ip[1:])

                except IndexError as e:
                    pass

        assert User.query.count() == 3, "Should be 3"
        assert Transaction.query.count() > 6

        for x in Transaction.query.all():
            print(x.to_json())

        for x in User.query.all():
            print(x.to_json())

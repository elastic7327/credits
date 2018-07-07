"""
File: flaskr.py
Author: Daniel
Email: elastic7327@email.com
Github: https://github.com/elastic7327
Description: . . . .
"""


import sys
import select
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask('__name__')  # pylint: disable=invalid-name
db = SQLAlchemy(app)  # pylint: disable=invalid-name


# @click.option('<', prompt=True)
# @click.argument('filename')
# def hello(filename):
# click.echo(filename)


def credit():

    if select.select([sys.stdin, ], [], [], 0.0)[0]:
        print("Have data! stdin")

    else:

        print("No data! file data")
        filename = sys.argv[-1]
        with open(filename, 'r') as f:
            for line in f:
                print(line)


if __name__ == '__main__':
    credit()

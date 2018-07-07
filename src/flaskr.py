"""
File: flaskr.py
Author: Daniel
Email: elastic7327@email.com
Github: https://github.com/elastic7327
Description: . . . .
"""

from flask import Flask
app = Flask(__name__)  # pylint: disable=invalid-name


@app.route('/')
def hello_world():
    """
    doc
    """
    return 'Hello, World!'

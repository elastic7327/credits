"""
File: base.py
Author: Me
Email: yourname@email.com
Github: https://github.com/yourname
Description:
"""

import unittest

from mixer.backend.flask import mixer

from src.flaskr import app, db


class TestBaseClass(unittest.TestCase):

    """Test case docstring."""

    def setUp(self):
        app.config.from_object('src.configs.settings.DevelopmentConfig')
        mixer.init_app(app)
        db.create_all()
        self.client = app.test_client()

        self.test_username1 = 'Daniel'
        self.test_username2 = 'Chris'
        self.test_username3 = 'Trump'

        self.valid_card_no1 = "4028571169702107"
        self.valid_card_no2 = "9440038135573607"
        self.valid_card_no3 = "5272892672067154"

    def tearDown(self):
        db.session.remove()

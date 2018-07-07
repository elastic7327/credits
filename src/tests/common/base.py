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

    def tearDown(self):
        db.session.remove()

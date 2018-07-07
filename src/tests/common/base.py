"""
File: base.py
Author: Me
Email: yourname@email.com
Github: https://github.com/yourname
Description:
"""

import unittest

from src.flaskr import app, db
from mixer.backend.flask import mixer


class TestBaseClass(unittest.TestCase):

    """Test case docstring."""

    def setUp(self):
        """
        doc
        """
        # get test-config
        # app.config.from_object('src.configs.settings.TestingConfigReadOnly')
        app.config.from_object('src.configs.settings.TestingConfigLocalMysql')
        mixer.init_app(app)
        self.client = app.test_client()

    def tearDown(self):
        """
        doc
        """
        db.session.remove()

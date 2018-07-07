"""
File: test_models.py
Author: Me
Email: yourname@email.com
Github: https://github.com/yourname
Description:
"""

from mixer.backend.flask import mixer

from src.tests.common.base import TestBaseClass
from src.models.users import User


class TestModelsClass(TestBaseClass):

    """Test case docstring."""

    def test_smoke_test(self):

        assert 1 is 1, "Should be equal"

    def test_create_fake_users(self):

        for x in range(5):
            mixer.blend(User)

        assert User.query.count() == 5, "Suppose to be five"

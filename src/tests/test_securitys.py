"""
File: test_securitys.py
Author: Me
Email: yourname@email.com
Github: https://github.com/yourname
Description:
"""

from werkzeug.security import generate_password_hash, \
             check_password_hash

from mixer.backend.flask import mixer

from src.tests.common.base import TestBaseClass
from src.models.users import User
from src.flaskr import db

import pytest


class TestSecurityClass(TestBaseClass):

    """Test case docstring."""

    def test_smoke_test(self):
        """
            import Path 확인을 위한 스모크 테스트입니다.
        """
        assert 1 is 1, "Should be equal"

    def test_verificate_card_then_enc_dec_test(self):
        """
        doc
        """
        card_no = self.valid_card_no1

        print(card_no)

        hashed_card_no = generate_password_hash(card_no)

        assert check_password_hash(hashed_card_no, card_no)

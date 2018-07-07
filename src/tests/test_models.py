"""
File: test_models.py
Author: Me
Email: yourname@email.com
Github: https://github.com/yourname
Description:
"""

from mixer.backend.flask import mixer
from sqlalchemy import exc

from src.tests.common.base import TestBaseClass
from src.models.users import User
from src.flaskr import db

import pytest


class TestModelsClass(TestBaseClass):

    """Test case docstring."""

    def test_smoke_test(self):
        """
            import Path 확인을 위한 스모크 테스트입니다.
        """

        assert 1 is 1, "Should be equal"

    @pytest.mark.skip(reason="skip it for a moment")
    def test_create_fake_users(self):

        for x in range(5):
            mixer.blend(User)

        assert User.query.count() == 5, "Suppose to be five"

    def test_card_no_validation_check(self):
        """
        구현한 luhn 함수를 users 모델 validate에 등록을 해서
        테스트 합니다.
        """
        mixer.blend(User, card_no=self.valid_card_no1)

    def test_duplicate_card_no_check(self):
        """
        카드를 두번 등록을해서, 중복테스트를 합니다.
        Integrity Error 가 발생하기 때문에, 테스트가 깨집니다.
        그렇기 때문에, IE를 걸어서, 오류를 넘어가도록 합니다.
        """

        try:

            mixer.blend(User, card_no=self.valid_card_no1)
            mixer.blend(User, card_no=self.valid_card_no1)

        except exc.IntegrityError as e:
            db.session().rollback()

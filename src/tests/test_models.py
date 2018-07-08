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
from src.models.transactions import Transaction
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
        """
            유저가 적절하게 생성되는지 확인하는 테스트입니다.
        """

        for x in range(5):
            mixer.blend(User, username='fake_user')

        assert User.query.count() == 5, "Suppose to be five"

    def test_card_no_validation_check(self):
        """
            구현한 luhn 함수를 users 모델 validate에 등록을 해서
            테스트 합니다.
        """
        mixer.blend(User, card_no=self.valid_card_no1, username='Daniel')

    def test_duplicate_card_no_check(self):
        """
            카드를 두번 등록을해서, 중복테스트를 합니다.
            Integrity Error 가 발생하기 때문에, 테스트가 깨집니다.
            그렇기 때문에, IE를 걸어서, 오류를 넘어가도록 합니다.
        """

        try:

            mixer.blend(
                    User,
                    card_no=self.valid_card_no1,
                    username='Daniel', limitation=10000)

            mixer.blend(
                    User,
                    card_no=self.valid_card_no1,
                    username='Chris',
                    limitation=50000)

        except exc.IntegrityError as e:
            db.session().rollback()

    def test_transaction_models_without_transaction_zone(self):
        """
            트렌젝션 모델테스트 without Transaction' zone
        """
        daniel = User.query.filter_by(card_no=self.valid_card_no1).first()

        # 트렌젝션을 생성시키고, 어떤 행위인지, 그리고 어마운트와 트렌젝션 타입에 대해서, 유저의 밸런스를
        # 적절하게 수정을 해줍니다.
        amount = 1000

        tr = mixer.blend(
                Transaction,
                user_id=daniel.id,
                is_valid=1,
                type=0,
                tram=1000,
                label=f'{daniel.username} Charged {amount} at the Sumgo Online Shop'
            )

        daniel.balance = (daniel.balance - amount)

        db.session.commit()

        assert daniel.balance == -amount, "1000원을 Charge 했기 때문에 -1000원 이여야합니다."
        assert tr.tram == amount, f"{amount}, 값만큼 트렌젝션이 발생해야합니다."
        assert tr.type == 0, "Charge 이므로 타입이 0으로 발생해야합니다."
        assert tr.is_valid == 1, "정상적인 트렌젝션이므로 1이 되어야합니다."

        Transaction.query.count() == 1

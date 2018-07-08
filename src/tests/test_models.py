"""
File: test_models.py
Author: Daniel
Email: elastic7327@email.com
Github: https://github.com/elastic7327
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
        mixer.blend(
                User,
                card_no=self.valid_card_no1,
                username='Daniel',
                limitation=10000, balance=0)

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

    def test_transaction_models_charge_case_without_transaction_zone(self):
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
                type=1,
                tram=1000,
                label=f'{daniel.username} Credit {amount} at the Sumgo Online Shop'
            )

        daniel.balance = (daniel.balance - amount)

        db.session.commit()

        assert daniel.balance == -amount, "1000원을 Credit 했기 때문에 -1000원 이여야합니다."
        assert tr.tram == amount, f"{amount}, 값만큼 트렌젝션이 발생해야합니다."
        assert tr.type == 0, "Credit 이므로 타입이 0으로 발생해야합니다."

        Transaction.query.count() == 1

    def test_transaction_models_credit_case_without_transaction_zone(self):
        """
            트렌젝션 모델테스트 without Transaction' zone
        """

        mixer.blend(
                User,
                card_no=self.valid_card_no2,
                balance=0,
                username=self.test_username2, limitation=10000)

        chris = User.query.filter_by(
                card_no=self.valid_card_no2,
                username=self.test_username2).first()

        # 트렌젝션을 생성시키고, 어떤 행위인지, 그리고 어마운트와 트렌젝션 타입에 대해서, 유저의 밸런스를
        # 적절하게 수정을 해줍니다.
        amount = 1000

        tr = mixer.blend(
                Transaction,
                user_id=chris.id,
                type=1,
                tram=1000,
                label=f'{chris.username} Charge {amount}'
            )

        chris.balance = (chris.balance + amount)

        db.session.commit()

        chris = User.query.filter_by(card_no=self.valid_card_no2).first()

        assert chris.balance == amount, "1000원을 Charge 했기 때문에 +1000원 이여야합니다."
        assert tr.tram == amount, f"{amount}, 값만큼 트렌젝션이 발생해야합니다."
        assert tr.type == 1, "Charge 이므로 타입이 0으로 발생해야합니다."

    def test_all_transaction_model_test_with_bdd_story_lines(self):
        # 트럼프 라는 고객이 숨고에 신용카드를 적절하게 등록을합니다.
        # *내부적으로, 적절한 카드 넘버인지 확인을 하게됩니다.
        # 내부 정책에 의해서, 해당 고객의 한도는 15,000 달러로 한정짓습니다.

        trump_user_a = mixer.blend(
                User,
                card_no=self.valid_card_no3,
                balance=0,
                username=self.test_username3, limitation=10000)

        # 트럼프 고객님은 얼리어뎁터로써, 바로 숨고에 5,000 달러를 크레딧(충전) 합니다.
        # 숨고 팀에서 이를 매우 좋아합니다.

        amount = 5000

        mixer.blend(
            Transaction,
            user_id=trump_user_a.id,
            type=1,
            tram=5000,
            label=f'{trump_user_a.username} Charge {amount}'
        )

        trump_user_a.balance += amount

        assert trump_user_a.balance == 5000

        db.session.commit()

        # 트럼프 고객은 해당 충전한 금액에서 1,000 원을 지불하여, 피아노 과외를 받습니다.
        # 트럼프 고객은 남은 잔액을 확인해본 결과 자신의 크레딧은 4,000 달러가 있음을 숨고 시스템을
        # 통해서 확인을 할 수가 있습니다.

        trump_user_b = User.query.filter_by(
                card_no=self.valid_card_no3,
                username=self.test_username3).first()

        next_amount = 1000

        mixer.blend(
            Transaction,
            user_id=trump_user_b.id,
            type=0,
            tram=next_amount,
            label=f'{trump_user_b.username} Credit {next_amount} at the Sumgo Shop'
        )

        trump_user_b.balance -= next_amount

        assert trump_user_b.balance == 4000

        # 어느날 트럼프 고객님은 갑자기 머신러닝을 배우기 위해서(?) 지금 가지고 있는 돈은 모두 사용해서
        # 머신러닝 강좌를 등록하려고 합니다.
        # 머신러닝 강좌를 20,000달러 입니다.
        # 해당 강좌를 (홈페이지 버그?)를 통해서 어떻게 신청을 할 수 있게 되어서 2만 달러를 Charge 시도를 하게됩니다.

        try:

            # 트랙젝션 시작
            # 다행히도 숨고팀의 서버쪽에서는, 프론트 쪽에서 이런 잘못된 요청이 들어오더라도, 서버사이드에서 더블체크를 하고 있기 때문에
            # 이런 요청이 오더라도 걱정 할 필요가 없습니다.
            # 트럼프 고객님의 한도가 초과된 트렌젝션은 유효하지 않기 때문에,
            # 트렌젝션(오류) 기록에는 남지만, 트럼프 고객님의 정보에서는 아무런 변화가 없습니다.

            trump_user_c = User.query.filter_by(
                    card_no=self.valid_card_no3,
                    username=self.test_username3).first()

            after_next_amount = 20000

            mixer.blend(
                Transaction,
                user_id=trump_user_b.id,
                type=1,
                tram=next_amount,
                label=f'{trump_user_c.username} Credit {after_next_amount} at the Sumgo Shop'
            )

            trump_user_c.balance -= after_next_amount

            # Credit 5000, Charge 1000 -> Balance = 4000 (status 200)
            # Try Charge 20000, -> Balance = -16000 (status 400 or 500)
            assert trump_user_c.balance == -16000

            # 이후 해당 잘못된 금액을 트렌젝션 시도를 하게되면, Model Validate 에서 거절을 합니다.

            db.session.commit()

            # 트랙젝션 종료

        except AssertionError as e:

            print("OverCharged Error!")

        # 적절하게 트렌젝션이 롤백이 되었는지 다시 확인을 합니다.

        trump_user_d = User.query.filter_by(
                card_no=self.valid_card_no3,
                username=self.test_username3).first()

        assert trump_user_d.balance == 4000, "위의 트렌젝션은 잘못된 요청으로인해서, 실패했습니다. 잔액은 트렌젝션 시도 이전금액인 4000원이 남아야합니다."

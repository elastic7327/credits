"""
File: test_luhn.py
Author: Me
Email: yourname@email.com
Github: https://github.com/yourname
Description:
"""

from src.tests.common.base import TestBaseClass
from src.modules.luhn import luhn

# import pytest


class TestLuhnModules(TestBaseClass):

    """Test case docstring."""
    def test_simple_luhn_validate_case_1(self):
        res = luhn("121232232")
        assert res is not True

    def test_simple_luhn_validate_case_2(self):
        """
            테스트를 위해서 제가 실제로 사용하는
            신용카드 및 체크카드번호를 입력했습니다.
            평가가 끝나면 꼭 해당 코드들은 파기 부탁드립니다.
        """
        assert luhn("4028571169702107") is True

    def test_simple_luhn_validate_case_3(self):
        """
            테스트를 위해서 제가 실제로 사용하는
            신용카드 및 체크카드번호를 입력했습니다.
            평가가 끝나면 꼭 해당 코드들은 파기 부탁드립니다.
        """
        assert luhn("9440038135573607") is True

        # 위의 신용카드 번호에서 한자리수를 지워본다 => False
        # tail 숫자 7을 삭제했다
        assert luhn("944003813557360") is False

        # 앞자리 9의 숫자를 1로 변경했다 => False
        assert luhn("1440038135573607") is False

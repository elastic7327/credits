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
        assert luhn("2028571169702107") is not True

    def test_simple_luhn_validate_case_3(self):
        assert luhn("2028571169702107") is not True
        # 위의 신용카드 번호에서 한자리수를 지워본다 => False
        # tail 숫자 7을 삭제했다
        assert luhn("944003813557360") is False

        # 앞자리 9의 숫자를 1로 변경했다 => False
        assert luhn("1440038135573607") is False

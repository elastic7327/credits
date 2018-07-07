"""
File: luhn.py
Author: Me
Email: yourname@email.com
Github: https://github.com/yourname
Description:
"""


def luhn(n):
    sum, alt, num = 0, 0, 0
    i = len(n) - 1
    while i >= 0:
        num = int(n[i])
        if alt:
            num = num * 2

            if num > 9:
                num = (num % 10) + 1

        sum = sum + num
        alt = not alt
        i -= 1

    return sum % 10 == 0

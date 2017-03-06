"""
Help the bookseller !

https://www.codewars.com/kata/help-the-bookseller
"""
import re
import sys
sys.path.append('..')

from helpers.test_wrapper import Test


def stock_list(b, c):
    stock = [0] * len(c)
    categories = set(c)
    for item in b:
        # Category /space/ Quantity
        match = re.match(r'([A-Z]{3,})\s(\d+)', item)
        if match:
            cat = match.group(1)[0]
            if cat in categories:
                stock[c.index(cat)] += int(match.group(2))
    if sum(stock) > 0:
        res = []
        for c, q in zip(c, stock):
            res.append('({} : {})'.format(c, q))
        return ' - '.join(res)
    return ''


def run_tests():
    with Test() as test:
        b = ["ABAR 200", "CDXE 500", "BKWR 250", "BTSQ 890", "DRTY 600"]
        c = ["A", "B"]
        test.assert_equals(stock_list(b, c), "(A : 200) - (B : 1140)")


if __name__ == '__main__':
    run_tests()

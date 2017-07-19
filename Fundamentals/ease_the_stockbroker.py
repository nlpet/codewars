"""
Ease the Stockbroker

URL: https://www.codewars.com/kata/ease-the-stockbroker
"""
from helpers.test_wrapper import Test
import re
import sys
sys.path.append('..')


def balance_statement(strng):
    prices, badly_formed = {'B': 0, 'S': 0}, []
    for _, order in enumerate(strng.split(', ')):
        # Quote /space/ Quantity /space/ Price /space/ Status
        match = re.match(r'^([A-z0-9\.]+)\s(\d+)\s(\d*\.\d+)\s(B|S)$', order)
        if match:
            if prices.get(match.group(4)) is not None:
                prices[match.group(4)] += int(match.group(2)
                                              ) * float(match.group(3))
            else:
                badly_formed.append(order + ' ;')
        elif order:
            badly_formed.append(order + ' ;')

    res = 'Buy: {:d} Sell: {:d}'.format(round(prices['B']), round(prices['S']))
    if badly_formed:
        res += '; Badly formed {}: '.format(len(badly_formed))
        res += ''.join(badly_formed)

    return res


def run_tests():
    with Test() as test:
        s = 'ZNGA 1300 2.66 B, CLH15.NYM 50 56.32 B, \
             OWW 1000 11.623 B, OGG 20 580.1 B'
        test.assert_equals(balance_statement(s), 'Buy: 29499 Sell: 0')
        s = 'GOOG 300 542.93 B, CLH15.NYM 50 56.32 S, \
             CSCO 250 29.46 B, OGG 20 580.1 B'
        test.assert_equals(balance_statement(s), 'Buy: 181846 Sell: 2816')
        test.assert_equals(balance_statement(''), 'Buy: 0 Sell: 0')
        s = 'GOOG 300 542.0 B, AAPL 50 145.0 B, \
             CSCO 250.0 29 B, GOOG 200 580.0 S'
        expected = 'Buy: 169850 Sell: 116000; \
                    Badly formed 1: CSCO 250.0 29 B ;'
        test.assert_equals(balance_statement(s), expected)
        s = 'CAP 1300 .2 B, CLH16.NYM 50 56 S, OWW 1000 11 S, OGG 20 580.1 S'
        expected = 'Buy: 260 Sell: 11602; Badly formed 2: \
                    CLH16.NYM 50 56 S ;OWW 1000 11 S ;'
        test.assert_equals(balance_statement(s), expected)


if __name__ == '__main__':
    run_tests()

"""
Correct the time-string

You have to create a method, that corrects a given time string. There was a
problem in addition, so many of the time strings are broken. Time-Format is
european. So from "00:00:00" to "23:59:59".

If the input-string is null or empty return exactly this value! (empty string for C++)
If the time-string-format is invalid, return null. (empty string for C++)

Some examples:

"09:10:01" -> "09:10:01"
"11:70:10" -> "12:10:10"
"19:99:99" -> "20:40:39"
"24:01:01" -> "00:01:01"
"""
import re
import sys
sys.path.append('..')

from helpers.test_wrapper import Test


def time_correct(time_str):
    if isinstance(time_str, str) and len(time_str):
        m = re.match(r'^(\d{2}):(\d{2}):(\d{2})$', time_str)

        if m:
            hh, mm, ss = list(map(int, m.groups()))
            srem, ss = divmod(ss, 60)
            mrem, mm = divmod(mm + srem, 60)
            hh = divmod(hh + mrem, 24)[1]

            return '{}:{}:{}'.format(*(str(t).zfill(2) for t in [hh, mm, ss]))
        else:
            return None

    return time_str


def run_tests():
    with Test() as test:
        test.describe("Basic tests")
        test.it("None or empty")
        test.assert_equals(time_correct(None), None)
        test.assert_equals(time_correct(""), "")
        test.it("Invalid Format")
        test.assert_equals(time_correct("001122"), None)
        test.assert_equals(time_correct("00;11;22"), None)
        test.assert_equals(time_correct("0a:1c:22"), None)
        test.it("Correction tests")
        test.assert_equals(time_correct("09:10:01"), "09:10:01")
        test.assert_equals(time_correct("11:70:10"), "12:10:10")
        test.assert_equals(time_correct("19:99:99"), "20:40:39")
        test.assert_equals(time_correct("24:01:01"), "00:01:01")
        test.assert_equals(time_correct("52:01:01"), "04:01:01")


if __name__ == '__main__':
    run_tests()

"""
Write a function, which takes a non-negative integer (seconds) as input and
returns the time in a human-readable format (HH:MM:SS)

HH = hours, padded to 2 digits, range: 00 - 99
MM = minutes, padded to 2 digits, range: 00 - 59
SS = seconds, padded to 2 digits, range: 00 - 59
The maximum time never exceeds 359999 (99:59:59)

You can find some examples in the test fixtures.
"""


def make_readable(seconds):
    mm, ss = divmod(seconds, 60)
    if mm >= 60:
        hh, mm = divmod(mm, 60)
    else:
        hh = 0
    return "{:02}:{:02}:{:02}".format(hh, mm, ss)



if __name__ == '__main__':
    assert(make_readable(0) == "00:00:00")
    assert(make_readable(5) == "00:00:05")
    assert(make_readable(60) == "00:01:00")
    assert(make_readable(86399) == "23:59:59")
    assert(make_readable(3600) == "01:00:00")
    assert(make_readable(359999) == "99:59:59")

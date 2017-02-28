"""
The input is a string str of digits. Cut the string into chunks (a chunk here is a substr
of the initial string) of size sz (ignore the last chunk if its size is less than sz).

If a chunk represents an integer such as the sum of the cubes of its digits is divisible
by 2, reverse that chunk; otherwise rotate it to the left by one position. Put together
these modified chunks and return the result as a string.

If


sz is <= 0 or if str is empty return ""
sz is greater (>) than the length of str it is impossible to take a chunk of size sz
hence return "".
"""


def revrot(strng, sz):
    result, lstring = [], len(strng)

    if sz <= 0 or sz > lstring:
        return ""

    for i in range(0, lstring, sz):
        substr = strng[i:i + sz]
        if len(substr) < sz:
            continue
        if sum(map(lambda x: int(x) ** 2, list(substr))) % 2 == 0:
            result.append(substr[::-1])
        else:
            result.append(substr[1:] + substr[0])
    return "".join(result)


if __name__ == '__main__':
    assert(revrot("123456987654", 6) == "234561876549")
    assert(revrot("123456987653", 6) == "234561356789")
    assert(revrot("66443875", 4) == "44668753")
    assert(revrot("66443875", 8) == "64438756")
    assert(revrot("664438769", 8) == "67834466")
    assert(revrot("123456779", 8) == "23456771")
    assert(revrot("", 8) == "")
    assert(revrot("123456779", 0) == "")
    assert(revrot("563000655734469485", 4) == "0365065073456944")

"""
Take 2 strings s1 and s2 including only letters from a to z.
Return a new sorted string, the longest possible, containing distinct
letters, - each taken only once - coming from s1 or s2.

a = "xyaabbbccccdefww"
b = "xxxxyyyyabklmopq"
longest(a, b) -> "abcdefklmopqwxy"

a = "abcdefghijklmnopqrstuvwxyz"
longest(a, a) -> "abcdefghijklmnopqrstuvwxyz"
"""
import string
import time


def longest(s1, s2):
    letter_positions = dict(zip(string.ascii_lowercase, range(26)))
    placeholders = [None] * 26
    ls1, ls2 = len(s1), len(s2)
    longest_string = []
    for i in range(max(ls1, ls2)):
        if i < ls1 and not placeholders[letter_positions[s1[i]]]:
            placeholders[letter_positions[s1[i]]] = True
        if i < ls2 and not placeholders[letter_positions[s2[i]]]:
            placeholders[letter_positions[s2[i]]] = True

    for i in range(26):
        if placeholders[i]:
            longest_string.append(string.ascii_lowercase[i])

    return ''.join(longest_string)


# faster
def longest2(a1, a2):
    return "".join(sorted(set(a1 + a2)))


if __name__ == '__main__':
    assert(longest("aretheyhere", "yestheyarehere") == "aehrsty")
    assert(longest("loopingisfunbutdangerous", "lessdangerousthancoding") == "abcdefghilnoprstu")
    assert(longest("inmanylanguages", "theresapairoffunctions") == "acefghilmnoprstuy")

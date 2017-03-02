"""
Longest Palindrome

Find the length of the longest substring in the given string s that is the same in reverse.

As an example, if the input was “I like racecars that go fast”, the substring
(racecar) length would be 7.

If the length of the input string is 0, return value must be 0.

Example:

"a" -> 1
"aab" -> 2
"abcde" -> 1
"zzbaabcd" -> 4
"" -> 0
"""
from collections import defaultdict


def longest_palindrome(s):
    ls = len(s)
    if ls == 0:
        return 0
    elif ls == 1 or ls == len(set(s)):
        return 1

    ch_to_ix = defaultdict(list)
    longest_so_far, longest = 0, 1

    for i in range(ls):
        ch_to_ix[s[i]].append(i)

    for i in range(ls):
        for ix in ch_to_ix[s[i]]:
            if ix == i or ix < i:
                continue

            start, end = i, ix

            while end - start > 0:
                if end - start in (1, 2):
                    longest_so_far += (end - start) + 1
                    end -= end - start
                elif s[end - 1] == s[start + 1]:
                    longest_so_far += 2
                    start += 1
                    end -= 1
                else:
                    longest_so_far = 0
                    break
            if longest_so_far > longest:
                longest = longest_so_far
            longest_so_far = 0
    return max(longest, longest_so_far)


if __name__ == '__main__':
    assert(longest_palindrome("a") == 1)
    assert(longest_palindrome("aa") == 2)
    assert(longest_palindrome("baa") == 2)
    assert(longest_palindrome("aab") == 2)
    assert(longest_palindrome("abcdefghba") == 1)
    assert(longest_palindrome("baablkj12345432133d") == 9)

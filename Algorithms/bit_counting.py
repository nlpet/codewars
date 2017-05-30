"""
Write a function that takes an (unsigned) integer as input, and returns the number of
bits that are equal to one in the binary representation of that number.

Example: The binary representation of 1234 is 10011010010,
so the function should return 5 in this case
"""


def count_bits(n):
    return bin(n).count("1")


if __name__ == '__main__':
    assert(count_bits(0) == 0)
    assert(count_bits(4) == 1)
    assert(count_bits(7) == 3)
    assert(count_bits(9) == 2)
    assert(count_bits(10) == 2)

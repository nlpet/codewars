"""
Complementary DNA

Deoxyribonucleic acid (DNA) is a chemical found in the nucleus of
cells and carries the "instructions" for the development and functioning
of living organisms.

If you want to know more http://en.wikipedia.org/wiki/DNA

In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G".
You have function with one side of the DNA (string, except for Haskell); you need
to get the other complementary side. DNA strand is never empty or there is no DNA
at all (again, except for Haskell).

DNA_strand ("ATTGC") # return "TAACG"
DNA_strand ("GTAT") # return "CATA"

"""
import sys
sys.path.append('..')

from helpers.test_wrapper import Test


def DNA_strand(s):
    complements = {
        'A': 'T',
        'T': 'A',
        'G': 'C',
        'C': 'G'
    }
    return ''.join([complements[ch] for ch in s])


# shorter and more pythonic solution
def DNA_strand_ol(s):
    return s.translate(str.maketrans('ATCG', 'TAGC'))


def run_tests():
    with Test() as test:
        test.assert_equals(DNA_strand("AAAA"), "TTTT", "String AAAA is")
        test.assert_equals(DNA_strand("ATTGC"), "TAACG", "String ATTGC is")
        test.assert_equals(DNA_strand("GTAT"), "CATA", "String GTAT is")


if __name__ == '__main__':
    run_tests()

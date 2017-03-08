"""
Salesman's Travel

Description:

A traveling salesman has to visit clients. He got each client's address
e.g. "432 Main Long Road St. Louisville OH 43071" as a list.

The basic zipcode format usually consists of two capital letters followed by a
white space and five digits. The list of clients to visit was given as a string
of all addresses, each separated from the others by a comma, e.g. :

"123 Main Street St. Louisville OH 43071,432 Main Long Road St. Louisville
OH 43071,786 High Street Pollocksville NY 56432".

To ease his travel he wants to group the list by zipcode.

Task

The function travel will take two parameters r (list of all clients' addresses)
and zipcode and returns a string in the following format:

zipcode:street and town,street and town,.../house number,house number,...

The street numbers must be in the same order as the streets where they belong.

If a given zipcode doesn't exist in the list of clients' addresses return "zipcode:/"
"""
from collections import defaultdict
from re import compile, search, VERBOSE
import sys
sys.path.append('..')

from helpers.test_wrapper import Test


# (\d+)\s([A-z0-9\.\s]+)([A-Z]{2}\s\d{5})
REGEX = compile("""
^                  # begin address
(\d+)\s            # address / house number followed by a space
([A-z0-9\.\s]+)    # street and city names
([A-Z]{2}\s\d{5})  # post code
""", VERBOSE)

ADDRESS_BOOK = defaultdict(lambda: defaultdict(list))


def maybe_construct_address_book(addresses):
    if id(addresses) != ADDRESS_BOOK.get('id'):
        for address in addresses.split(','):
            m = search(REGEX, address)
            num, adr, postcode = list(map(lambda x: x.strip(), m.groups()))
            ADDRESS_BOOK[postcode]['adr'].append(adr)
            ADDRESS_BOOK[postcode]['num'].append(num)
        ADDRESS_BOOK['id'] = id(addresses)


def travel(addresses, postcode):
    # dont create the address book every time, simple check on id
    maybe_construct_address_book(addresses)
    return '{}:{}/{}'.format(
        postcode,
        ','.join(ADDRESS_BOOK[postcode]['adr']),
        ','.join(ADDRESS_BOOK[postcode]['num'])
    )


def run_tests():
    with Test() as test:

        ad = ("123 Main Street St. Louisville OH 43071,432 Main Long Road St. Louisville OH 43071,786 High Street Pollocksville NY 56432,"
          "54 Holy Grail Street Niagara Town ZP 32908,3200 Main Rd. Bern AE 56210,1 Gordon St. Atlanta RE 13000,"
          "10 Pussy Cat Rd. Chicago EX 34342,10 Gordon St. Atlanta RE 13000,58 Gordon Road Atlanta RE 13000,"
          "22 Tokyo Av. Tedmondville SW 43098,674 Paris bd. Abbeville AA 45521,10 Surta Alley Goodtown GG 30654,"
          "45 Holy Grail Al. Niagara Town ZP 32908,320 Main Al. Bern AE 56210,14 Gordon Park Atlanta RE 13000,"
          "100 Pussy Cat Rd. Chicago EX 34342,2 Gordon St. Atlanta RE 13000,5 Gordon Road Atlanta RE 13000,"
          "2200 Tokyo Av. Tedmondville SW 43098,67 Paris St. Abbeville AA 45521,11 Surta Avenue Goodtown GG 30654,"
          "45 Holy Grail Al. Niagara Town ZP 32918,320 Main Al. Bern AE 56215,14 Gordon Park Atlanta RE 13200,"
          "100 Pussy Cat Rd. Chicago EX 34345,2 Gordon St. Atlanta RE 13222,5 Gordon Road Atlanta RE 13001,"
          "2200 Tokyo Av. Tedmondville SW 43198,67 Paris St. Abbeville AA 45522,11 Surta Avenue Goodville GG 30655,"
          "2222 Tokyo Av. Tedmondville SW 43198,670 Paris St. Abbeville AA 45522,114 Surta Avenue Goodville GG 30655,"
          "2 Holy Grail Street Niagara Town ZP 32908,3 Main Rd. Bern AE 56210,77 Gordon St. Atlanta RE 13000")

        def testing(actual, expected):
            test.assert_equals(actual, expected)

        test.describe("travel")
        test.it("Basic tests")
        testing(travel(ad, "AA 45522"), "AA 45522:Paris St. Abbeville,Paris St. Abbeville/67,670")
        testing(travel(ad, "EX 34342"), "EX 34342:Pussy Cat Rd. Chicago,Pussy Cat Rd. Chicago/10,100")
        testing(travel(ad, "EX 34345"), "EX 34345:Pussy Cat Rd. Chicago/100")
        testing(travel(ad, "AA 45521"), "AA 45521:Paris bd. Abbeville,Paris St. Abbeville/674,67")
        testing(travel(ad, "AE 56215"), "AE 56215:Main Al. Bern/320")


if __name__ == '__main__':
    run_tests()

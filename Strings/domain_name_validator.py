"""
Domain name validator

Description:

In this kata you have to create a domain name validator mostly compliant
with RFC 1035, RFC 1123, and RFC 2181

For purposes of this kata, following rules apply:

- Domain name may contain subdomains (levels), hierarchically separated by .
- Domain name must not contain more than 127 levels, including top level (TLD)
- Domain name must not be longer than 253 characters (RFC specifies 255,
  but 2 characters are reserved for trailing dot and null character for
  root level)
- Level names must be composed out of lowercase and uppercase ASCII letters,
  digits and - (minus sign) character
- Level names must not start or end with - (minus sign) character
- Level names must not be longer than 63 characters
- Top level (TLD) must not be fully numerical

Additionally, in this kata

- Domain name must contain at least one subdomain (level) apart from TLD
- Top level validation must be naive - ie. TLDs nonexistent in IANA
  register are still considered valid as long as they adhere to the rules
  given above.


The validation function accepts string with the full domain name and
returns boolean value indicating whether the domain name is valid or not.

Examples:

validate('codewars') == False
validate('g.co') == True
validate('codewars.com') == True
validate('CODEWARS.COM') == True
validate('sub.codewars.com') == True
validate('codewars.com-') == False
validate('.codewars.com') == False
validate('example@codewars.com') == False
validate('127.0.0.1') == False
"""
import re
import sys
sys.path.append('..')

from helpers.test_wrapper import Test


def validate(domain_name):
    regex = r'^[a-zA-Z0-9][a-zA-Z0-9-_]{0,61}[a-zA-Z0-9]{0,1}\.([a-zA-Z]{1,6}|[a-zA-Z0-9-]{1,30}\.[a-zA-Z]{2,3})$'
    match = re.match(regex, domain_name)
    return match is not None


def run_tests():
    with Test() as test:
        test.describe('Domain name validator tests')
        test.expect(not validate('codewars'))
        test.expect(validate('g.co'))
        test.expect(validate('codewars.com'))
        test.expect(validate('CODEWARS.COM'))
        test.expect(validate('sub.codewars.com'))
        test.expect(not validate('codewars.com-'))
        test.expect(not validate('.codewars.com'))
        test.expect(not validate('example@codewars.com'))
        test.expect(not validate('127.0.0.1'))
        test.expect(validate('some-horribly-long-domain-name-but-still-shorter-than-63-ch.zzz'))
        test.expect(not validate('some.horribly.long.domain.name.which.has.a.bunch.of.subdomains.to.be.long.enough.to.exceed.128.characters.but.is.still.shorter.than.253.characters'))
        test.expect(not validate('a.b.c.d.e.f.g.h.i.j.k.l.m.n.o.p.q.r.s.t.u.v.w.x.y.z.a.b.c.d.e.f.g.h.i.j.k.l.m.n.o.p.q.r.s.t.u.v.w.x.y.z.a.b.c.d.e.f.g.h.i.j.k.l.m.n.o.p.q.r.s.t.u.v.w.x.y.z.a.b.c.d.e.f.g.h.i.j.k.l.m.n.o.p.q.r.s.t.u.v.w.x.y.z.a.b.c.d.e.f.g.h.i.j.k.l.m.n.o.p.q.r.s.t.u.v.w'))
        test.expect(validate('some-horribly-long-domain-name-this-time-longer-than-63-charaters.zzz'))
        test.expect(validate('xn--example-kva.meow'))
        test.expect(not validate('_http._sctp.example.com'))


if __name__ == '__main__':
    run_tests()

from csirtg_indicator import Indicator
from csirtg_indicator.exceptions import InvalidIndicator
from faker import Faker
fake = Faker()


def _not(data):
    for d in data:
        try:
            d = Indicator(d)
            assert d.itype is not 'ipv6'
        except InvalidIndicator:
            pass


def _ok(data):
    for d in data:
        assert Indicator(d).itype is 'ipv6'


def test_ipv6_ok():
    data = [
        '2001:1608:10:147::21',
        '2001:4860:4860::8888',
        '2001:4860::/64',
        '2001:4860::/48',
        '2001:4860::/32',
        '2001:4860:AC10:FE01:6ab8:1c48:a95a:b1c2'
    ]

    _ok(data)

def test_ipv6_with_ports():
    d = {
        '[2001:1608:10:147::21]:8888': ('2001:1608:10:147::21', '8888'),
        '[2001:db8::1]:8080': ('2001:db8::1', '8080')
    }

    for k, v in d.items():
        k = Indicator(k)
        assert k.indicator == v[0]
        assert k.portlist == v[1]
        assert k.itype == 'ipv6'


def test_ipv6_nok():
    data = [
        'example.com',
        'http://example.com:81',
        '192.168.1.1',
        '127.0.0./1'
    ]

    _not(data)


def test_ipv6_random():
    for d in range(0, 100):
        assert Indicator(indicator=fake.ipv6()).itype == 'ipv6'
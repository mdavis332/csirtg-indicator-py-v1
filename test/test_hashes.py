from csirtg_indicator import Indicator
from csirtg_indicator.exceptions import InvalidIndicator


def _ok(data, expected_itype):
    for d in data:
        assert Indicator(d).itype is expected_itype


def test_md5():
    data = [
        '4eb20288afaed97e82bde371260db8d8',
        '098f6bcd4621d373cade4e832627b4f6',
        'd98c61be17f381abb9eb9c6c33130d63',
        'e239843aeb4a399b167dd1c4c1dbe381'
    ]

    _ok(data, 'md5')

def test_sha1():
    data = [
        'e9a01d04ebe58f51e4291adee6768ce754d155d5',
        'a94a8fe5ccb19ba61c4c0873d391e987982fbbd3',
        'e5e8fb1c63d873160e62a17214a611c33ecf2b78',
        'b2fb98fdbed0a051c1ebfa0003372c379b6f2a34'
    ]

    _ok(data, 'sha1')

def test_sha256():
    data = [
        '07159C2B9BB509C71BD329254B93C1F1A1808A4D8523BDAA5E2FB2DF1BE25177',
        'DD45204E6330E986EA0F5613D3142DC8CE94BF7A405862FBFD972717CF33997B',
        'CA777AD559181538B77CB89D95C76C717871CD432E417D6AD89CF9FA1B9A5DB8',
        '2968036F87F183009B6CBCBD4AD25AA64DA8F8903DDC16923C91A6F6CB7AB822'
    ]

    _ok(data, 'sha256')

def test_sha512():
    data = [
        '33A578B73AA7BDCCD499B1CF303468AC67355A7F88304630FA99AFB5C8BC64E22C252FFCEC4F29DF5800AF1DB0780D8FF7C9F198E29BBB9AA51340F66CB51054',
        'EACE2D4BFDA8A86EA0FCADA90C7786B274FE820B62223DC0940EB6F89A9CC4381E3FC0054DC3BDD17A1882B781A9E93F8DC99AE03FDBD643F24D8A7C1483085D',
        '6E18C1455E89982CB03B059B68F8BF44979DE770F4F1826DE44EC52344C464327BC43DEB5357EEA6BCB45B9F82E011BD9E1AC8AD8AFC0B82EF52514CDF1395FE',
        '79E737CF7DFB6DA7AD9A2D5ACA4D7417EAE48654B8B5484A890700B4573D24DA3169138C9B0FC5CA2B8A41B9B3452014AB4B586A9DD1DD8DBB48C93CB8FC8726'
    ]

    _ok(data, 'sha512')

def test_ssdeep():
    data = [
        '96:s4Ud1Lj96tHHlZDrwciQmA+4uy1I0G4HYuL8N3TzS8QsO/wqWXLcMSx:sF1LjEtHHlZDrJzrhuyZvHYm8tKp/RWO',
        '384:EWo4X1WaPW9ZWhWzLo+lWpct/fWbkWsWIwW0/S7dZhgG8:EWo4X1WmW9ZWhWH/WpchfWgWsWTWtf8',
        '6144:3wSQSlrBHFjOvwYAU/Fsgi/2WDg5+YaNk5xcHrYw+Zg+XrZsGEREYRGAFU25ttR/:ctM7E0L4q',
        '3:q8wK6FuFWcEqlv:3wK6FN1I'
    ]

    _ok(data, 'ssdeep')
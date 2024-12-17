from unittest.mock import patch, MagicMock
from p05_get_only_numbers import get_only_numbers


def test_read_only_numbers():
    #bez mock - pracujeme přímo se souborem 'aa'
    #assert get_only_numbers() == '15|2|8|8|5|15|22|101|5|8|12|7'

    #test_data = ["1,2,4,5,7,8,Hi", "Hello Word, Hi, 5", "456,123,gfgf,2"]
    #expected = "1|2|4|5|7|8|5|456|123|2"

    test_data = open('bb').readlines()
    expected = '15|2|8|8|5|15|22|101|5|8|12|7'

    fake_api = MagicMock()
    fake_api.get_data.return_value = test_data
    with patch('p05_get_only_numbers.API', fake_api):
        assert get_only_numbers() == expected

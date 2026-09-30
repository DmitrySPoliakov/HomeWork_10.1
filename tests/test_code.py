from src.code import up_first, revers_string


def test_up_first():
    assert up_first('skypro') == 'Skypro'


def test_up_first_for_empty():
    assert up_first('') == ''


def test_revers_string(my_string: object) -> None:
    assert revers_string(my_string) == "321"

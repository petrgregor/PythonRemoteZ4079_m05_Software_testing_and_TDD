import pytest

from p03_check_email import check_email_format


@pytest.fixture()
def provide_email():
    print("Příprava emailového účtu")
    emails = ["badmail.com", "bad@email@com"]
    for email in emails:
        yield email
    print("Úklid po testování")


def test_email_exception(provide_email):
    """test zda je vyvolána vyjímka pro nevalidní emaily"""
    with pytest.raises(Exception):
        email = provide_email
        print(f"Test email: '{email}'")
        assert check_email_format(email)  # nevalidní formát emailu, který vyvolá vyjímku
    with pytest.raises(Exception):
        email = provide_email
        print(f"Test email: '{email}'")
        assert check_email_format(email)  # nevalidní formát emailu, který vyvolá vyjímku

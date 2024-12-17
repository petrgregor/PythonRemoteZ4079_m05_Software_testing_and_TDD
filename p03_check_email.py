import re


def check_email_format(email):
    """oveření jestli je formát zadaného emailu správný"""
    if not re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email):
        raise Exception("Nevalidní formát emailu")
    else:
        return "Email je v pořádku"

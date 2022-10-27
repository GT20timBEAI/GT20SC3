from sqlalchemy import create_engine, text
import re


def symbol(string):
    symbol = "!~`@#$%^&*()_-+=]}[{\n|';:/?>.<,abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in string:
        if i in symbol:
            return True


def inValid(email):
    regex = re.compile(
        r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    if re.fullmatch(regex, email):
        return False
    else:
        return True


def get_engine():
    """Creating SQLite Engine to interact"""
    return create_engine("sqlite:///finalproject.db", future=True)


def run_query(query, commit: bool = False):
    """Runs a query against the given SQLite database.

    Args:
        commit: if True, commit any data-modification query (INSERT, UPDATE, DELETE)
    """
    engine = get_engine()
    if isinstance(query, str):
        query = text(query)

    with engine.connect() as conn:
        if commit:
            conn.execute(query)
            conn.commit()
        else:
            return [dict(row) for row in conn.execute(query)]


##############################################################################################
# FOR TESTING
##############################################################################################
class COL:
    BOLD = "\033[1m"
    PASS = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BLUE = "\033[94m"


def assert_eq(expression, expected):
    try:
        if expression == expected:
            return
    except Exception as e:
        raise RuntimeError(
            f"{COL.WARNING}Expression can't be evaluated: {COL.FAIL}{e}{COL.ENDC}")

    errs = [
        "",
        f"{COL.BLUE}Expected: {COL.WARNING}{expected}{COL.ENDC}",
        f"{COL.BLUE}Yours: {COL.FAIL}{expression}{COL.ENDC}",
    ]
    raise AssertionError("\n\t".join(errs))

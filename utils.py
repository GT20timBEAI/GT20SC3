from sqlalchemy import create_engine, text
import re
from datetime import datetime as dt
import os

# TODO: check product id
def checkProduct(id):
    product_id = run_query("select id from \"Product_list\"")
    for i in product_id:
        if id == i["id"]: return True
    return False

#TODO: check image exension from body
def allowed_file(filename):
    ALLOWED_EXTENSIONS = {'png', 'jpg'}
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

#TODO: check category_id
def checkIdCategory(id):
    idCategory = run_query("select category_id from \"Category\"")
    for i in idCategory:
        if i["category_id"] == id:
            return True
    return False

#TODO: time now
def timeNow():
    return dt.now().strftime("%A, %d %B %Y")


#TODO: valid users(True for seller, False for Buyer)
def validUser(token, seller: bool = False):
    users = run_query("select * from \"Users\"")
    cek = 1 if seller else 0
    for i in users:
        if token == i["token"] and i["is_admin"] == cek:
            return True
    return False

#TODO: convert image to bytes
def serveImage(urlPath):
    with open(f"image/{urlPath}", "rb") as image:
        f = image.read()
        return f


 #TODO: get extension
def extensionImage(image):
    allow = ['jpg', 'png']
    extension = image.split('.')[1]
    if extension not in allow or '.' not in image:return False
    return extension

# check number
def symbol(string):
    symbol = "!~`@#$%^&*()_-+=]}[{\n|';:/?>.<,abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in string:
        if i in symbol: return True
        
#TODO: check email valid or not
def inValid(email):
    regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    if re.fullmatch(regex, email):
      return False
    else:
      return True

def get_engine():
    """Creating SQLite Engine to interact"""
    engine_uri = "postgresql+psycopg2://{}:{}@{}:{}/{}".format(
        os.getenv("user"),
        os.getenv("pass"),
        os.getenv("host"),
        os.getenv("port"),
        os.getenv("db"),
    )

    return create_engine(engine_uri, future=True)


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
        raise RuntimeError(f"{COL.WARNING}Expression can't be evaluated: {COL.FAIL}{e}{COL.ENDC}")

    errs = [
        "",
        f"{COL.BLUE}Expected: {COL.WARNING}{expected}{COL.ENDC}",
        f"{COL.BLUE}Yours: {COL.FAIL}{expression}{COL.ENDC}",
    ]
    raise AssertionError("\n\t".join(errs))

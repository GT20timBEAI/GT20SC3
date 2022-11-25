from sqlalchemy import create_engine, text
import re
from datetime import datetime as dt
import base64


def symbol(string):
    symbol = "!~`@#$%^&*()_-+=]}[{\n|';:/?>.<,abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in string:
        if i in symbol:
            return True

def ProductListGet(data):
    dataList = []
    for i in data:
        data_dict = {}
        image = run_query(f"""
        select image_url from "Image"
        WHERE product_id = '{i['id']}'
        limit 1
        """)
        if len(image) == 0:
            image = []
        else:
            image[0]['image_url']
        
        data_dict['id'] = i['id']
        data_dict['title'] = i['product_name']
        data_dict['price'] = i['price']
        data_dict['image'] = image
        dataList.append(data_dict)
    
    return dataList


def ProductListSorted(category_id, sort_by, price, condition, product_name):

    # split category
    if category_id == '0':
        category = ''
    else:
        category_id = category_id.split(",")
        category = ''
        for i in category_id:
            category = f"{category}category_id like \'{i}%\' OR "

    # Initial sorted
    sorted = 'ORDER BY product_name ASC' if sort_by == 'Price a_z' else 'ORDER BY product_name DESC'
    if sorted == '0':
        sorted = ''

    # initial price
    if price == '0':
        price = ''
    else:
        price = price.split(',')
        min = price[0]
        max = price[1]
        price = f"Price BETWEEN {min} AND {max},"
    
    # initial condition
    if condition == '0':
        condition = ''
    else:
        condition = f"\'{condition}\',"
    
    # inital product name
    if product_name == '0':
        product_name = ''
    else:
        product_name = f"product_name like '%{product_name}%',"

    data = run_query(f"""
    SELECT id, product_name, price
    FROM "Product_list"
    WHERE {category}  {price} {condition} {product_name} status = 1
    {sorted}
    """)

    return data
# def name_symbol(name):
#     regex = re.compile("[a-zA-Z0-9 ]")
#     if re.fullmatch(regex, name):
#         return False
#     else:
#         return True

def validUser(token, seller: bool = False):
    users = run_query("select * from Users")
    cek = 1 if seller else 0
    for i in users:
        if token == i['token'] and i['is_admin'] == cek:
            return True
    return False


def timeNow():
    return dt.now().strftime("%A, %d, %B, %Y")


def serve_image(urlPath):
    with open(f"image/{urlPath}", "rb") as image:
        f = image.read()
        return f


def extensionImage(image):
    allow = ['jpg', 'png']
    extension = image.split('.')[1]

    if extension not in allow:
        return False

    return extension


def inValid(email):
    regex = re.compile(
        r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    if re.fullmatch(regex, email):
        return False
    else:
        return True


def isCartIdExist(id):
    CartId = run_query("SELECT Cart_id from Cart")
    for i in CartId:
        if i['Cart_id'] == id:
            return True
    return False


def isCategoryIdExist(id):
    CategoryId = run_query("select category_id from Category")
    for i in CategoryId:
        if i['category_id'] == id:
            return True
    return False


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

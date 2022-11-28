from sqlalchemy import create_engine, text
from datetime import datetime as dt
import os



def countProductList(category_id, sort_by, price, condition, product_name):

    # split category
    if category_id == '0':
        category = ''
    else:
        category_id = category_id.split(",")
        category = ''
        for i in category_id:
            category = f"{category}category_id like '{i}%' OR "

    # Initial sorted
    sorted = 'GROUP BY product_name' if sort_by == 'Price a_z' else 'GROUP BY product_name DESC'
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
    SELECT count(id)
    FROM "Product_list"
    WHERE {category}  {price} {condition} {product_name} status = 1
    """)

    return data




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
from sqlalchemy import create_engine, text
import re
from datetime import datetime as dt
import os
import base64



# get Product list
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
            image = image[0]['image_url']
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

def checkCategoryName(category):
    name = run_query("""
    SELECT category_name from "Category"
    """)
    for i in name:
        if category == i['category_name']: 
            return True
    return False

def base64_split(base64_str):
    if ',' in base64_str:
        base64_list = base64_str.split(',')
        return base64_list[1]
    else:
        return base64_str

# get images from storage
import os
from google.cloud import storage

def uploadStorage(path):
    project_id = 'universal-sun-364614' 
    bucket_name = 'fashion-campuss' 
    bucket_file = f'{path}' 
    local_file = f'{path}'

    # Initialise a client
    client = storage.Client(project_id)
    # Create a bucket object for our bucket
    bucket = client.get_bucket(bucket_name)
    # Create a blob object from the filepath
    blob = bucket.blob(bucket_file)
    # Upload the file to a destination
    blob.upload_from_filename(local_file)
        


# upload file to google storage
def uploadFile(image, name):
    storageconst = storage.Client()
    bucket = storageconst.bucket("fashion-campuss")
    blob = bucket.blob(f"{name}.png")
    blob.upload_from_file(image, content_type="image/png")

# delete file from google storage
def deleteStorage(fileName):
    storageconst = storage.Client()
    bucket = storageconst.bucket("fashion-campuss")
    blob = bucket.blob(fileName)
    blob.delete()

def getStorageImage(image):

    storageconst = storage.Client()
    bucket = storageconst.bucket("fashion-campuss")
    blob = bucket.blob(image)
    with blob.open("rb") as file:
        images = file.read()
    return images


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
    return dt.now().strftime("%A, %d, %B, %Y")


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

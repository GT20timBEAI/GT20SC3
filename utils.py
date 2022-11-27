from sqlalchemy import create_engine, text
import re
from datetime import datetime as dt
import os
import base64

# get product list for get user order
def productListUserOrder(product):
    product_list = []
    for s in product:
        data_product = run_query(f"""
        SELECT product_name, price FROM "Product_list"
        WHERE id = '{s['item_id']}'
        """)
        name = data_product[0]['product_name']
        price = int(data_product[0]['price']) * int(s['quantity'])

        image = run_query(f"""
        SELECT image_url FROM "Image"
        WHERE product_id = '{s['item_id']}'
        """)
        
        if len(image) == 0:
            image = '/image/dummy.png'
        else:
            image = image[0]['image_url']

        dict = {
            "id": s['item_id'],
            "details": {
                "quantity": s['quantity'],
                "size": s['size']
            },
            "price": price,
            "image": image,
            "name": name
            }
        product_list.append(dict)

    data = {
        "products": product_list,
        "shipping_method": product[0]['shipping_method']
    }

    return data


# GET total price from cart
def totalPrice(id):
    item = run_query(f"""
    SELECT item_id, quantity FROM "Cart"
    WHERE user_id = '{id}' and status = 'cart'
    """)
    countPrice = 0
    for i in item:
        price = 0
        price = run_query(f"""
        SELECT price FROM "Product_list"
        WHERE id = '{i['item_id']}'
        """)[0]['price']
        price *= i['quantity']
        countPrice += price

    return countPrice



# check havecart
def checkCartUser(id):
    countShippingPrice = 0
    data = run_query(f"""
    SELECT item_id FROM "Cart"
    WHERE user_id = '{id}'
    """)
    if len(data) == 0:
        return False
    else:
        for i in data:
            price = run_query(f"""
            SELECT price FROM "Product_list"
            WHERE id = '{i['item_id']}'
            """)[0]['price']
            countShippingPrice += price
    
    #initiate reguler
    if countShippingPrice < 200:
        reguler = countShippingPrice / 100 * 15
    else:
        reguler = countShippingPrice / 100 * 20

    #initiate sameday
    if countShippingPrice < 300:
        sameday = countShippingPrice / 100 * 20
    else:
        sameday = countShippingPrice / 100 * 25
    
    data = [
        {"name" : "regular",
        "price" : int(reguler)
        },
        {"name" : "next day",
        "price" : int(sameday)
        }
    ]

    return data

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
            image = '/image/dummy.png'
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
        for i in range(len(category_id)):
            category = f"{category}category_id = \'{category_id[i]}\'"
            if i == len(category_id) - 1:
                category = f"{category} AND "
            else:
                category = f"{category} OR "

    # Initial sorted
    sorted = 'ORDER BY product_name ASC' if sort_by == 'Price a_z' else 'ORDER BY product_name DESC'
    if sort_by == '0':
        sorted = ''
    
    # initial condition
    if condition == '0':
        condition = ''
    else:
        condition = f"condition = \'{condition}\' AND "
    
    # inital product name
    if product_name == '0':
        product_name = ''
    else:
        product_name = f"product_name like '%{product_name}%', "

    data = run_query(f"""
    SELECT id, product_name, price
    FROM "Product_list"
    WHERE {category}{condition}{product_name} status = 1
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
    bucket_name = 'fashion-campuss-gt20' 
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
    bucket = storageconst.bucket("fashion-campuss-gt20")
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
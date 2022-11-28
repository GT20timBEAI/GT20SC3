from services.utils import run_query
from google.cloud import storage

# TODO: check product id
def checkProduct(id):
    product_id = run_query("select id from \"Product_list\"")
    for i in product_id:
        if id == i["id"]: return True
    return False


# delete file from google storage
def deleteStorage(fileName):
    storageconst = storage.Client()
    bucket = storageconst.bucket("fashion-campuss")
    blob = bucket.blob(fileName)
    blob.delete()

# split from base64
def base64_split(base64_str):
    if ',' in base64_str:
        base64_list = base64_str.split(',')
        return base64_list[1]
    else:
        return base64_str

#upload storage
def uploadStorage(path):
    project_id = 'advance-medium-369816' 
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


# sorted productlist
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
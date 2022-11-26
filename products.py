"""
QUERY PARAMS EXAMPLE

[Key]           [Example]
page            1
page_size       100
sort_by         Price a_z, Price z_a
category        Id category a, id category b
price           0,10000
condition       used
product_name    name


[CREATE PRODUCTS]
Requirements (from the earliest to check):
==> name
    - if product name is not given:
        - return {"error": "Please fill in the product name"}
        - status code: 400
==> description
    - if description is not given:
        - return {"error": "Please fill in the description"}
        - status code: 400
==> condition [new, second]
    - if condition is not given:
        - return {"error": "Please fill in the condition"}
        - status code: 400
    # Maybe use this
    - if condition not in list table
        - return {"error" : "condiiton not in the list"}
==> images [image1, image2, image3]
    - if images is not given:
        - return {"error": "Please fill in the images"}
        - status code: 400
==> category [A, B, C]
    - if category is not given:
        - return {"error": "Please fill in the category"}
        - status code: 400
    - if category_id not in category
        - return {"error" : "category not found"}
        - status code : 401
==> Price
    - If price is not a positive number:
        - return {"error": "Please specify a positive amount"}
        - status code: 400
    - If price not integer
        - return {"error" : "price must be integer"}
        - status code : 400
- if user not found
    - return {"error" : "user not found"}
    - status code : 401
- if user not admin
    - return {"error" : "user not admin"}
    - status code : 401
- Else, everything is valid:
    - return {"message": "Product added"}
    - status code: 201

[UPdate PRODUCTS]
Requirements (from the earliest to check):
==> name
    - if product name is not given:
        - return {"error": "Please fill in the product name"}
        - status code: 400
==> description
    - if product description is not given:
        - return {"error": "Please fill in the product description"}
        - status code: 400
==> images
    - if product description is not given:
        - return {"error": "Please fill in the product images"}
        - status code: 400
==> condition [new, second]
    - if product description is not given:
        - return {"error": "Please fill in the product condition"}
        - status code: 400
    # Maybe use this
    - if condition not in list table
        - return {"error" : "condiiton not in the list"}
==> category
    - if product description is not given:
        - return {"error": "Please fill in the product description"}
        - status code: 400
    - if category_id not in category
        - return {"error" : "category not found"}
        - status code : 401
==> price
    - if product price is not given:
        - return {"error": "Please fill in the product price"}
        - status code: 400
    - If price not integer
        - return {"error" : "price must be integer"}
        - status code : 400
==> product_id
    - if product product_id is not given:
        - return {"error": "Please fill in the product product_id"}
        - status code: 400
    - if product_id not found in table
        - return {"error" : "product not found"}
        - status code : 401
- if user not found
    - return {"error" : "user not found"}
    - status code : 401
- if user not admin
    - return {"error" : "user not admin"}
    - status code : 401
- if everything oke
    - return {"message" : "Product updated"}
    - status code : 200

"""


from flask import Blueprint, request
from utils import (
    run_query, 
    validUser, 
    allowed_file, 
    checkProduct, 
    symbol,
    deleteStorage, 
    base64_split, 
    uploadStorage,
    ProductListSorted,
    countProductList, 
    ProductListGet
    )
import uuid
from werkzeug.utils import secure_filename
import os
import base64
import json


products_bp = Blueprint("products", __name__, url_prefix="/products")

# DONE with Front End
@products_bp.route("", methods=["GET"])
def productlist():
    jwt_token = request.headers.get("Authentication")

    # TODO: check valid user are seller
    if validUser(jwt_token, True): 
        data = run_query(f"""
            SELECT id, product_name, price
            FROM "Product_list"
            """)
        
        data = ProductListGet(data)
        return {"data" : data}, 200

    else:
        params = request.args
        page = params['page']
        page_size = params['page_size']

        if 'sort_by' in params:
            sort_by = params['sort_by']
        else:
            sort_by = '0'
        if 'category' in params:
            category = params['category']
        else:
            category = '0'
        if 'harga' in params:
            price = params['harga']
        else:
            price = '0'
        if 'kondisi' in params:
            condition = params['kondisi']
        else:
            condition = '0'
        if 'product_name' in params:
            product_name = params['product_name']
        else:
            product_name = '0'
        
        # GET data 
        data = ProductListSorted(category, sort_by, price, condition, product_name)

        # count product 
        count = len(data)
        print(data)
        dataList = []
        for i in range(int(page_size) * (int(page)-1), int(page_size) * int(page)):
            if count <= i:
                break
            data_dict = {}
            image = run_query(f"""
            select image_url from "Image"
            WHERE product_id = '{data[i]['id']}'
            limit 1
            """)[0]['image_url']
            data_dict['id'] = data[i]['id']
            data_dict['title'] = data[i]['product_name']
            data_dict['price'] = data[i]['price']
            data_dict['image'] = image
            dataList.append(data_dict)


        return {"data" : dataList, "total_rows" : len(dataList) }, 200


# DONE TINGGAL TUNGGU AI
@products_bp.route("/search_image", methods=["POST"])
def searchimage():
    body = request.get_data()
    body = body.decode('utf-8')
    body = json.loads(body)

    # FIXME: base64 consume data AI
    image = body['images']


    #source code tim AI
    category_name = None
    
    id = run_query(f"""
    select category_id from "Category"
    where category_name='{category_name}'
    """)[0]['category_id']
    return {"category_id" : id }, 200

#DONE: TIME TO REVIEW
@products_bp.route("/<string:urlpath>", methods=["GET"])
def productDetailPage(urlpath):
    size = ["S", "M", "L"]

    product = run_query(f"""
    SELECT id,category_id, product_name, price, product_detail
    FROM "Product_list" 
    WHERE id like '{urlpath}'
    """)

    list_image = []
    image = run_query(f"""
    SELECT image_url from "Image" 
    WHERE product_id like '{urlpath}'
    """)
    for i in image:
        list_image.append(i['image_url'])

    category = run_query(f"""
    SELECT category_name FROM "Category"
    WHERE category_id = '{product[0]['category_id']}'
    """)[0]['category_name']

    data = {
         "id": product[0]['id'],
        "title":product[0]['product_name'],
        "size":size,
        "product_detail": product[0]['product_detail'],
        "price" : product[0]['price'] ,
        "images_url": list_image,
        "category_id": product[0]['category_id'],
        "category_name": category
    }

    return {"data" : data}, 200



    

# TODO: in admin page
@products_bp.route("", methods=["POST"])
def createProduct():
    # try:
    body = request.get_data()
    body = body.decode('utf-8')
    body = json.loads(body)
    image = body['images']
    jwt_token = request.headers.get("Authentication")
    product_name = body["product_name"]
    if 'description' not in body:
        description = None
    else:
        description = body["description"]
    condition = body["condition"]
    category = body["category"]
    price = body["price"]


    # TODO: check valid user are seller
    if not validUser(jwt_token, True): 
        return {"message" : "user not valid"}, 400

    #TODO: check price is integer
    if symbol(str(price)): 
        return {"message": "price must be number"}, 400

    no = 1
    list = []
    #upload to google storage
    for i in image:
        i = base64_split(i)

        #decode base64 string data
        decoded_data=base64.b64decode((i))

        #write the decoded data back to original format in  file
        img_file = open(f'{product_name}{no}.png', 'wb')
        img_file.write(decoded_data)
        img_file.close()

        #upload file from local to google storage and add name file
        uploadStorage(f'{product_name}{no}.png')
        list.append(f'{product_name}{no}.png')
        
        #delete file
        os.remove(f'{product_name}{no}.png')
        no += 1

    #TODO: insert into database product_list
    id = uuid.uuid4() # ==> id  product with uuid
    run_query(f"""
    INSERT into "Product_list"(id, category_id, product_name, condition, price, product_detail, status)
    VALUES('{id}', '{category}', '{product_name}', '{condition}', {price}, '{description}', 1)
    """, True)
    for i in list:
        run_query(f"""
        INSERT into "Image" (product_id, image_url)
        VALUES('{id}' , '/image/{i}' )
        """, True)
    return {"message" : "Product added"}, 200
    # except:
    #     return {"message" : "something wrong"}, 400


@products_bp.route("", methods=["PUT"])
def UpdateProducts():
    jwt_token = request.headers.get("Authentication")

    #TODO: check users
    if not validUser(jwt_token, True): return {"message" : "user not valid"}, 400

    body = request.get_data()
    body = body.decode('utf-8')
    body = json.loads(body)
    image = body['images']
    jwt_token = request.headers.get("Authentication")
    product_name = body["product_name"]
    if 'description' not in body:
        description = None
    else:
        description = body["description"]
    condition = body["condition"]
    category = body["category"]
    price = body["price"]
    product_id = body['product_id']

    #TODO: check price is integer
    if symbol(str(price)): return {"message": "price must be number"}, 400

    #TODO: check product id
    if not checkProduct(product_id): return {"message" : "product not found"}, 400
    
    #TODO: check price is integer
    if symbol(str(price)): return {"message": "price must be number"}, 400

    imageBefore = run_query(f"""
    SELECT image_url from "Image"
    WHERE product_id like '{product_id}'
    """)


    list = []
    no = 1
    #upload to google storage
    if image[0].split('/')[0] == 'data:image':
        if 'image_url' in imageBefore[0]:
        #Delete image_url from Google Storage
            for i in imageBefore:
                great = i['image_url'].split('/')[2]
                deleteStorage(great)

        #Delete image_url on database
        run_query(f"""
        DELETE FROM "Image" where product_id like '{product_id}'
        """, True)



        for i in image:
            i = base64_split(i)

            #decode base64 string data
            decoded_data = base64.b64decode((i))

            #write the decoded data back to original format in  file
            img_file = open(f'{product_name}{no}.png', 'wb')
            img_file.write(decoded_data)
            img_file.close()

            #upload file from local to google storage and add name file
            uploadStorage(f'{product_name}{no}.png')
            list.append(f'{product_name}{no}.png')
            
            #delete file
            os.remove(f'{product_name}{no}.png')
            no += 1
        for i in list:
            run_query(f"""
            INSERT into "Image" (product_id, image_url)
            VALUES('{product_id}' , '/image/{i}' )
            """, True)
            
    run_query(f"""
    UPDATE "Product_list"
    SET product_name = '{product_name}', category_id = '{category}',
    condition = '{condition}', price = {price}, product_detail = '{description}'
    WHERE id like '{product_id}'
    """, True)
    return{"message": "Product updated"}, 200



#delete products softs
@products_bp.route("/<string:urlpath>", methods=["DELETE"])
def DeleteProducts(urlpath):

    jwt_token = request.headers.get("Authentication")

    #TODO: check users
    if not validUser(jwt_token, True): return {"message" : "user not valid"}, 400


    #TODO: check product id
    if not checkProduct(urlpath): return {"message" : "product id not found"}, 400

    # imageBefore = run_query(f"""
    # SELECT image_url from "Image"
    # WHERE product_id like {urlpath}%
    # """)

    #Delete image_url from Google Storage
    # for i in imageBefore:
    #     deleteStorage(i)

    #Delete image_url on database
    # run_query(f"""
    # DELETE FROM "Image" where product_id like '{urlpath}%'
    # """, True)

    # Delete product on database
    print(urlpath)
    run_query(f"""
    UPDATE "Product_list" 
    SET status = 0
    WHERE id like '{urlpath}'
    """, True)
    return {"message" : "Product deleted"}, 200
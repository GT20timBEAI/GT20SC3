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

"""


from flask import Blueprint, request
from utils import run_query, validUser, allowed_file, checkProduct, symbol
import uuid
from werkzeug.utils import secure_filename
import os


products_bp = Blueprint("products", __name__, url_prefix="/products")

# untuk request cek di scr
@products_bp.route("", methods=["GET"])
def productlist():
    pass

@products_bp.route("/search_image", methods=["POST"])
def searchimage():
    pass

@products_bp.route("/{id}", methods=["POST"])
def productDetailPage():
    pass

# TODO: in admin page
@products_bp.route("", methods=["POST"])
def createProduct():
    # pass
    jwt_token = request.headers.get("Authentication")
    body = request.json# request.json
    product_name = body["product_name"]
    description = body["description"]
    images = body["image"]
    condition = body["condition"]
    category = body["category_id"]
    price = body["price"]
    
    #TODO: check valid user are buyer
    if not validUser(jwt_token, True): return {"error" : "user not valid"}, 400

    #TODO: check price is integer
    if symbol(str(price)): return {"error": "price must be number"}, 400


    #FIXME: save image to folder image
    # save url directory with name image to list image
    # listImagess =[] # ==> save to this for insert to database
    # for i in images:
    #     if not allowed_file(i) return {"error" : "file extension must png or jpg"}, 400
    #     listImages.append(i)
    # for i in images:
    # images = request.files.get('image')
    # image_name = secure_filename(images.filename)
    # images.save(os.path.join("image/", image_name))
    #TODO: make requirements


    #TODO: insert into database product_list
    id = uuid.uuid4() # ==> id  product with uuid
    run_query(f"insert into \"Product_list\"(id, category_id,\
            product_name,condition, price, product_detail, image_url)\
            values(\'{id}\', \'{category}\', \'{product_name}\', \'{condition}\',\
            {price}, \'{description}\', \'{images}\')",True)
    return {"message" : "Product added"},200


@products_bp.route("/{category_id}", methods=["PUT"])
def UpdateProducts():
    jwt_token = request.headers.get("Authentication")

    #TODO: check users
    if not validUser(jwt_token, True): return {"error" : "user not valid"}, 400

    body = request.json# request.json
    product_name = body["product_name"]
    description = body["description"]
    images = body["image"]
    condition = body["condition"]
    category = body["category_id"]
    price = body["price"]
    product_id = body["product_id"]

    #TODO: check price is integer
    if symbol(str(price)): return {"error": "price must be number"}, 400

    #TODO: check product id
    if not checkProduct(product_id): return {"error" : "product not found"}, 400

    #TODO: update product
    run_query(f"update \"Product_list\" set product_name=\'{product_name}\',\
            description=\'{description}\', condition=\'{condition}\',\
            category_id = \'{category}\', price={price}, image_url=\'{images}\'\
            where id=\'{product_id}\'", True)
    return{"message": "Product updated"}, 200



#delete products softs
@products_bp.route("/,path:urlpath", methods=["DELETE"])
def DeleteProducts(urlpath):

    #TODO: check product id
    if not checkProduct(urlpath): return {"error" : "product id not found"}, 400
    run_query(f"delete from \"Product_list\" where id=\'{urlpath}\'", True)
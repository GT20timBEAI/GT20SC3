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
from utils import run_query, validUser
import uuid


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
    jwt_token = request.headers.get("jwt_token")
    body = request.json
    product_name = body["product_name"]
    description = body["description"]
    images = body["images"]
    condition = body["condition"]
    category = body["category_id"]
    price = body["price"]
    
    if not validUser(jwt_token, True): return {"error" : "user not valid"}, 400

    #FIXME: save image to folder image
    # save url directory with name image to list image
    listImages =[] # ==> save to this for insert to database


    #TODO: make requirements


    #TODO: insert into database product_list
    id = uuid.uuid4() # ==> id  product with uuid
    run_query(f"insert into Product_list(id, category_id,\
            product_name,condition, price, product_detail, image_url)\
            values(\'{id}\', \'{category}\', \'{product_name}\', \'{condition}\',\
            {price}, \'{description}\', {listImage})",True)
    return {"message" : "Product added"},200


@products_bp.route("/{category_id}", methods=["PUT"])
def UpdateProducts():
    pass


#delete products softs
@products_bp.route("", methods=["DELETE"])
def DeleteProducts():
    pass
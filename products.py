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
from utils import run_query, validUser, symbol, checkProduct


products_bp = Blueprint("products", __name__, url_prefix="/products")

# untuk request cek di scr


@products_bp.route("", methods=["GET"])
def productlist():
    pass


@products_bp.route("/search_image", methods=["POST"])
def searchimage():
    pass


@products_bp.route("/<path:id>", methods=["GET"])
def productDetailPage(id):
    try:
        product_detail = run_query(
            f"select * from  Product_List where id = {id}")
        data = {
            "id": product_detail['id'],
            "title": product_detail['product_name'],
            "size": product_detail['size'],
            "product_detail": product_detail['product_detail'],
            "price": product_detail['price'],
            "image_url": product_detail['image_url']
        }
        return data, 200
    except KeyError:
        return {"message": "error, user already exist"}, 400


@products_bp.route("", methods=["POST"])
def createProduct():
    try:
        jwt_token = request.headers.get('token')
        body = request.json
        product_name, description, images = body['product_name'], body['product_detail'], body['image_url']
        condition, category, price = body['condition'], body['category_id'], body['price']

        if not validUser(jwt_token, True):
            return {"error": "user not valid"}, 400

        # FIXME: Buat algoritma buat nyimpan url
        listImages = []

        id = uuid.uuid4()
        run_query("insert into Product_List(id, category_id, product_name, condition, price, product_detail, image_url\
            values(\'{id}\', \'{category}\', \'{product_name}\', \'{condition}\', \'{price}\', \'{description}\', \'{listImages}\')", True)
        return {"message": "Product added"}
    except KeyError:
        return {"message": "error, user already exist"}


@products_bp.route("/{category_id}", methods=["PUT"])
def UpdateProducts():
    jwt_token = request.headers.get('Authentication')

    if not validUser(jwt_token, True):
        return {"error": "user not valid"}, 400

    body = request.json
    # req = [product_name, description, images,
    #        condition, category, price, product_id]
    # for i in req:
    #     req[i] = body["\'i\'"]
    product_name, description, images = body['product_name'], body['description'], body['image']
    condition, category, price, product_id = body['condition'], body[
        'category_id'], body['price'], body['product_id']

    #####################################################
    # Check if price is integer or not
    # if symbol(str(req['price'])):
    #     return {"error": "price must be number"}, 400
    #####################################################

    if symbol(str(price)):
        return {"error": "price must be number"}, 400

    #####################################################
    # if not checkProduct(req['product_id']):
    #     return {"error": "product not found"}, 400
    #####################################################

    if not checkProduct(product_id):
        return {"error": "product not found"}, 400

    #####################################################
    # run_query(
    #     f"update \'Product_list\' set product_name=\'{req['product_name']}\', \
    #     description = \'{req['description']}\', condition = \'{req['condition']}\',\
    #     category_id = \'{req['category']}\', price = \'{req['price']}\', image_url=\'{req['images']}\',\
    #     where id = \'{req['product_id']}\', True")
    #####################################################

    run_query(f"update \"Product_list\" set product_name=\'{product_name}\',\
            description=\'{description}\', condition=\'{condition}\',\
            category_id = \'{category}\', price={price}, image_url=\'{images}\'\
            where id=\'{product_id}\'", True)

    return {"message": "Product added"}, 200

    # delete products softs


@products_bp.route("", methods=["DELETE"])
def DeleteProducts():
    pass

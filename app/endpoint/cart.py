from flask import Blueprint, request
from app.helper.utils import run_query, validUser
import uuid
import json

cart_bp = Blueprint("cart", __name__, url_prefix="/cart")

# DONE With Frond END
@cart_bp.route("", methods=["POST"])
def addtoCart():
    jwt_token = request.headers.get('Authentication')

    if not validUser(jwt_token):
        return {"message": "user not valid or try login again"}, 400

    body = request.get_data()
    body = body.decode('utf-8')
    body = json.loads(body)
    id, quantity, size = body['id'], body['quantity'], body['size']
    

    cart_id = uuid.uuid4()
    user_id = run_query(f"""
    select id from "Users" where token = '{jwt_token}'
    """)[0]['id']
    run_query(f"""
    Insert into "Cart" (cart_id, item_id, user_id, quantity, size, status )
    VALUES ('{cart_id}','{id}','{user_id}',{quantity},'{size}', 'cart' )
    """, True)
    return {"message": "success"}, 200

# Front end error
@cart_bp.route("", methods=["GET"])
def getUserCart():
    jwt_token = request.headers.get('Authentication')
    # Check buyer
    if not validUser(jwt_token):
        return {"message": "user not valid"}, 400

    user_id = run_query(f"""
    SELECT id from "Users"
    WHERE token = '{jwt_token}'
    """)[0]['id']

    cart = run_query(f"""
    select cart_id, quantity, size, item_id from "Cart"
    WHERE user_id = '{user_id}' and status = 'cart'
    """)
    data = []
    for i in cart:
        item_id = run_query(f"""
        select product_name, price from "Product_list"
        where id = '{i['item_id']}'
        """)[0]
        image = run_query(f"""
        SELECT image_url from "Image"
        WHERE product_id = '{i['item_id']}'
        """)
        if len(image) > 0:
            image = image[0]['image_url']
        else:
            image = '/image/dummy.jpg'
        dict = {}
        detail_dict = {}
        detail_dict['quantity'] = i['quantity']
        detail_dict['size'] = i['size']
        dict['id'] = i['cart_id']
        dict['details'] = detail_dict
        dict['price'] = item_id['price']
        dict['image'] = image
        dict['name'] = item_id['product_name']
        data.append(dict)
    return {"data" : data, "message" : "success"}, 200



# Review with Frond END
@cart_bp.route("/<string:cartId>", methods=["DELETE"])
def deleteCartItem(cartId):

    jwt_token = request.headers.get('Authentication')

    if not validUser(jwt_token):
        return {"message": "user not valid"}, 400

    run_query(f"""
    DELETE FROM "Cart" where cart_id = '{cartId}'
    """, True)

    return {"message" : "Cart Deleted"}, 200
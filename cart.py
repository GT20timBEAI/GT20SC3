from flask import Blueprint, request
from utils import run_query, validUser
import uuid

cart_bp = Blueprint("cart", __name__, url_prefix="/cart")


@cart_bp.route("", methods=["POST"])
def addtoCart():
    try:
        jwt_token = request.headers.get('Authentication')
        body = request.form
        id, quantity, size = body['id'], body['quantity'], body['size']
        
        if not validUser(jwt_token):
            return {"message": "user not valid"}, 400

        cart_id = uuid.uuid4()
        user_id = run_query(f"""
        select id from "Users" where token='{jwt_token}'
        """)[0]['id']
        run_query(f"""
        Insert into "Cart" (cart_id, item_id, user_id, quantity, size )
        VALUES ('{cart_id}','{id}','{user_id}',{quantity},'{size}' )
        """, True)
        return {"message": "Item added to cart"}, 200

    except:
        return {"message": "user already exist"}


@cart_bp.route("", methods=["GET"])
def getUserCart():
    try:
        jwt_token = request.headers.get('Authentication')
        # Check buyer
        if not validUser(jwt_token):
            return {"message": "user not valid"}, 400

        cart = run_query("""
        select cart_id, quantity, size, item_id from "Cart"
        """)
        data = []
        for i in cart:
            item_id = run_query(f"""
            select product_name, price, image_url from "Product_list"
            where id = '{i['item_id']}'
            """)[0]
            dict = {}
            detail_dict = {}
            detail_dict['quantity'] = i['quantity']
            detail_dict['size'] = i['size']
            dict['id'] = i['cart_id']
            dict['detail'] = detail_dict
            dict['price'] = item_id['price']
            dict['image'] = item_id['image_url']
            dict['name'] = item_id['product_name']
            data.append(dict)
        return {"data" : data}, 200
    except:
        return {"Error": "Not found cart data"}, 400



@cart_bp.route("/<string:cartId>", methods=["DELETE"])
def deleteCartItem(cartId):

    jwt_token = request.headers.get('Authentication')
    if not validUser(jwt_token):
        return {"message": "user not valid"}, 400

    run_query(f"""
    DELETE FROM "Cart" where cart_id = '{cartId}'
    """, True)

    return {"message" : "Cart Deleted"}, 200
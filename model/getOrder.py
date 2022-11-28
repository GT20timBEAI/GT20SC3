from flask import Blueprint, request
from services.utils import validUser, run_query



getOrder_bp = Blueprint("getOrder", __name__, url_prefix="/orders")


# FIXME: In Admin Page
@getOrder_bp.route("", methods=["GET"])
def getOrder():

    jwt_token = request.headers.get("Authentication")
    if not validUser(jwt_token, True): 
        return {"message" : "user not valid"}, 400
        
    order_id = run_query("""
    SELECT order_id, created_at from "Orders"
    """)
    price = 0
    list_data = []
    for i in order_id:
        data = {}
        # Get data on Cart
        cart = run_query(f"""
        SELECT user_id, quantity, item_id FROM "Cart"
        WHERE order_id = '{i['order_id']}'
        """)

        # count price
        for pri in cart:
            get_price = run_query(f"""
            SELECT price FROM "Product_list"
            WHERE id = '{pri['item_id']}'
            """)[0]['price']
            get_price = get_price * pri['quantity']
            price = price + get_price
    

    # GET data user
    user = run_query(f"""
    SELECT name, email FROM "Users"
    WHERE id = '{cart[0]['user_id']}'
    """)
    data = {
        "id": i['order_id'],
        "user_name": user[0]['name'],
        "created_at": i['created_at'],
        "user_id": cart[0]['user_id'],
        "user_email": user[0]['email'],
        "total": price
    }

    list_data.append(data)
    return {"data" : list_data}, 200

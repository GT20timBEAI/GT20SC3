from flask import Blueprint, request
from app.helper.utils import validUser, run_query,  timeNow
from app.helper.shipping import checkCartUser, totalPrice
from app.helper.sendemail import sendOrderEmail
import json
import uuid

shipping_bp = Blueprint("shipping", __name__, url_prefix="/order")

# Done with frond end
@shipping_bp.route("", methods=["POST"])
def createOrder():

    # Auth token
    jwt_token = request.headers.get('Authentication')
    if not validUser(jwt_token):
        return {"message": "user not valid"}, 400

    # Initiate request
    body = request.get_data()
    body = body.decode('utf-8')
    body = json.loads(body)
    shipping_method = body['shipping_method']
    user = body['shipping_address']

    if user['name'] == None or user['city'] == None or user['address'] == None or user['phone_number'] == None:
        return {"message" : "Please Change Your Shipping address on admin page"}, 400

    # GET user ID
    id = run_query(f"""
    SELECT id FROM "Users"
    WHERE token = '{jwt_token}'
    """)[0]['id']

    # CHECK shipping address


    # GET balance
    balance = run_query(f"""
    SELECT name, balance, email FROM "Users"
    WHERE id = '{id}'
    """)[0]

    # GET shipping price
    data = checkCartUser(id)
    shipping_price = 0
    for i in data:

        if i['name'] == shipping_method:
            shipping_price = i['price']
        elif i['name'] == shipping_method:
            shipping_price = i['price']

    # total price
    price = totalPrice(id) + shipping_price

    # Check balance enough or not
    if price > balance['balance']:
        return {"message" : "Your Balance Not enough for complete this order"}

    # send total price to email user
    sendOrderEmail(balance['name'], int(price), balance['email'])

    time = timeNow()
    order_id = uuid.uuid4()

    # Update Balance on user
    run_query(f"""
    UPDATE "Users"
    SET balance = balance - {price}
    WHERE id = '{id}'
    """, True)

    # Update orders on table orders
    run_query(f"""
    INSERT INTO "Orders"(order_id, created_at, name, address, city, phone_number)
    VALUES('{order_id}','{time}', '{user['name']}', '{user['address']}', '{user['city']}', '{user['phone_number']}')
    """, True)

    # Update status cart
    run_query(f"""
    Update "Cart"
    SET status = 'order', order_id = '{order_id}', shipping_method = '{shipping_method}'
    WHERE user_id = '{id}' and status = 'cart'
    """, True)

    # Update sales admin
    run_query(f"""
    Update "Users"
    SET balance = balance + {price}
    WHERE is_admin = 1
    """, True)

    print(f"""
    Update "Users"
    SET balance = balance + {price}
    WHERE is_admin = 1
    """)

    
    return {"message" : "Order success"}, 200


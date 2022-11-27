from flask import Blueprint, request
from utils import run_query, validUser, symbol, productListUserOrder
import json


user_bp = Blueprint("user", __name__, url_prefix="/user")


@user_bp.route("/order", methods=["GET"])
def userOrder():
    # Check user are buyer
    jwt_token = request.headers.get('Authentication')

    if not validUser(jwt_token):
        return {"message": "user not valid"}, 400

    user_id = run_query(f"""
    SELECT id FROM "Users"
    WHERE token = '{jwt_token}'
    """)[0]['id']

    order_id = run_query(f"""
    SELECT DISTINCT order_id FROM "Cart"
    WHERE user_id = '{user_id}'
    """)


    if order_id[0]['order_id'] == None:
        return {"data" : []}
    

    list_data = []
    for i in order_id:
        order = run_query(f"""
        select * FROM "Orders"
        WHERE order_id = '{i['order_id']}'
        """)

        product = run_query(f"""
        SELECT item_id, quantity, size, shipping_method FROM "Cart"
        WHERE order_id = '{i['order_id']}'
        """)
        product_list = productListUserOrder(product)

        data = {
                "id": i['order_id'],
                "created_at": order[0]['created_at'],
                "products": product_list['products'],
                "shipping_method": product_list['shipping_method'],
                "shipping_address": {
                    "name": order[0]['name'],
                    "phone_number": order[0]['phone_number'],
                    "address": order[0]['address'],
                    "city": order[0]['city']
                }
            }

        list_data.append(data)
    
    return {"data" : list_data}, 200






    [
    {
   	 "id": "uuid",
   	 "created_at": "Mon, 22 august 2022",
   	 "products": [
   		 {
   			 "id": "uuid",
   			 "details": {
   				 "quantity": 100,
   				 "size": "M"
   			 },
   			 "price": 10000,
   			 "image": "/url/image.jpg",
   			 "name": "Product a"
   		 }
   	 ],
   	 "shipping_method": "same day",
   	 "shipping_address": {
   		 "name": "address name",
   		 "phone_number": "082713626",
   		 "address": "22, ciracas, east jakarta",
   		 "city": "Jakarta"
   	 }
    }
]



# Done with frond end
@user_bp.route("/shipping_address", methods=["GET"])
def getUserShippingAddress():

    jwt_token = request.headers.get('Authentication')

    if not validUser(jwt_token):
        return {"message": "user not valid"}, 400

    id = run_query(f"""
    SELECT id FROM "Users"
    where token = '{jwt_token}'
    """)[0]['id']

    user_sp = run_query(f"""SELECT address, city, name, phone_number
        FROM "Buyer_Shipping"
        WHERE user_id = '{id}'
        """)

    if len(user_sp) != 0:
        address = user_sp[0]['address'] 
        city = user_sp[0]['city']
        name = user_sp[0]['name']
        phone = user_sp[0]['phone_number']
    else:
        address = None
        city = None
        name = None
        phone = None

    data = {
        "id": id,
        "name": name,
        "phone_number": phone,
        "address": address,
        "city": city
    }
    
    return {"data" : data}, 200

# DONE with Front end
@user_bp.route("", methods=["GET"])
def userDetail():

    jwt_token = request.headers.get('Authentication')

    if not validUser(jwt_token):
        return {"message": "user not valid"}, 400


    userDetail = run_query(f"""
    select name, email, phone_number from "Users"
    WHERE token = '{jwt_token}'
    """)
    data = {
        "name": userDetail[0]['name'],
        "email": userDetail[0]['email'],
        "phone_number": userDetail[0]['phone_number']
    }
    return {"data" : data}, 200

# Done with front end
@user_bp.route("/shipping_address", methods=["POST"])
def changeShippingAddress():
    jwt_token = request.headers.get('Authentication')

    if not validUser(jwt_token):
        return {"message": "user not valid"}, 400
    id = run_query(f"""
    SELECT id FROM "Users"
    where token = '{jwt_token}'
    """)[0]['id']
    body = request.json
    address = body['address']
    city = body['city']
    name = body['name']
    phone = body['phone_number']

    # ceck phone number
    # if symbol(phone): 
    #     return {"message": "phone just containt number"},400

    run_query(f"""
    Insert into "Buyer_Shipping" (user_id, address, city, name, phone_number)
    VALUES('{id}', '{address}', '{city}', '{name}' , {int(phone)})
    """, True)
    return {
        "message": "success",
        "name" : name,
        "phone_number" : phone,
        "address" : address,
        "city" : city
    }, 200


# DONE with front end
@user_bp.route("/balance", methods=["POST"])
def topupBalance():
    try:
        jwt_token = request.headers.get('Authentication')
        body = request.get_data()
        body = body.decode('utf-8')
        body = json.loads(body)
        amount = body['amount']

        if not validUser(jwt_token):
            return {"message": "user not valid"}, 400

        if amount <= 0:
            return {"message": "Please specify a positive amount"}, 400

        user = run_query(f"""
        select id from "Users"
        WHERE token like '{jwt_token}%'
        """)[0]['id']

        # || Update Balance ||
        run_query(f"""
        UPDATE "Users"
        SET balance = balance + {int(amount)}
        WHERE id='{user}'
        """, True)
        return {"message": "Top up balance success"}, 200

    except KeyError:
        return {"message": "message, user already exist"}, 400

# DONE with front end
@user_bp.route("/balance", methods=["GET"])
def getBalance():
    try:
        jwt_token = request.headers.get('Authentication')
        if not validUser(jwt_token):
            return {"message": "user not valid"}, 400

        user = run_query(f"""
        select id from "Users"
        WHERE token like '{jwt_token}%'
        """)[0]['id']
    
        balance = run_query(f"""
        SELECT balance from "Users"
        WHERE id = '{user}'
        """)[0]['balance']
        data = {
            "balance": balance
        }
        return {"data" : data}, 200

    except KeyError:
        return {"message": "message, user already exist"}



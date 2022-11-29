from flask import Blueprint, request
from utils import run_query, validUser


user_bp = Blueprint("user", __name__, url_prefix="/user")


@user_bp.route("/shipping_address", methods=["GET"])
def getUserShippingAddress():
    try:

        jwt_token = request.headers.get('Authentication')

        if not validUser(jwt_token, True):
            return {"error": "user not valid"}, 400

        user_shipping = run_query(f"""
        SELECT u.id, u.name, u.phone_number u.token, by.address, by.city
        FROM Users u
        INNER JOIN Buyer_Shipping by
        ON by.user_id = u.id
        WHERE u.token = \'{jwt_token}\'
        """)[0]

        shipping_Data = {
            "id": user_shipping['u.id'],
            "name": user_shipping['u.name'],
            "phone_number": user_shipping['u.phone_number'],
            "address": user_shipping['by.address'],
            "city": user_shipping['by.city']
        }

        return {"data": shipping_data}, 200

    except KeyError:
        return {"message": "error, user already exist"}


@user_bp.route("", methods=["GET"])
def userDetail():
    try:
        jwt_token = request.headers.get('Authentication')

        if not validUser(jwt_token, True):
            return {"error": "user not valid"}, 400

        userDetail = run_query(f"""
        SELECT name, email, phone_number
        FROM Users
        WHERE token = \'{jwt_token}\'
        """)[0]

        user_Data = {
            "name": userDetail[0]['name'],
            "email": userDetail[0]['email'],
            "phone_number": userDetail[0]['phone_number']
        }

        return {"data": user_Data}, 200

    except KeyError:
        return {"message": "error, user already exist"}, 400


@user_bp.route("/shipping_address", methods=["POST"])
def changeShippingAddress():
    try:
        jwt_token = request.headers.get('Authentication')
        body = request.json
        name, phone_number, address, city = body['name'], body['phone_number'], body['address'], body['city']

        if not validUser(jwt_token, True):
            return {"error": "user not valid"}, 400

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
        if symbol(phone):
            return {"message": "phone just containt number"}, 400

        run_query(f"""
        Insert into "Buyer_Shipping" (user_id, address, city, name, phone_number)
        VALUES('{id}', '{address}', '{city}', '{name}' , {int(phone)})
        """, True)
        return {
            "name": name,
            "phone_number": phone,
            "address": address,
            "city": city
        }, 200

    except KeyError:
        return {"message": "User already exist"}


@user_bp.route("/balance", methods=["POST"])
def topupBalance():
    try:
        jwt_token = request.headers.get('Authentication')
        amount = request.args.get('amount')

        if not validUser(jwt_token, True):
            return {"error": "user not valid"}, 400

        if amount <= 0:
            return {"error": "Please specify a positive amount"}, 400

        user = run_query(f"select id from Users where token = \"{jwt_token}\"")[
            0]["id"]

        run_query(
            f"update Buyer_Shipping set balance = balance + {int(amount)} where user_id = \"{user}\"", True)

        return {"message": "Top up balance success"}, 200

    except KeyError:
        return {"message": "error, user already exist"}, 400


@user_bp.route("/balance", methods=["GET"])
def getBalance():
    try:
        jwt_token = request.headers.get('Authentication')
        if not validUser(jwt_token, True):
            return {"error": "user not valid"}, 400

        user = run_query(f"select id from Users where id = \"{jwt_token}\"")[
            0]['id']
        balance = run_query(
            f"select balance from Buyer_Shipping where user_id = \"{user}\"")

        data = {
            "balance": balance['balance']
        }
        return data, 200

    except KeyError:
        return {"message": "error, user already exist"}

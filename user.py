from flask import Blueprint, request
from utils import run_query, validUser


user_bp = Blueprint("user", __name__, url_prefix="/user")


@user_bp.route("/shipping_address", methods=["GET"])
def getUserShippingAddress():
    try:

        jwt_token = request.headers.get('Authentication')

        if not validUser(jwt_token, True):
            return {"error": "user not valid"}, 400
            
        user_shipping = run_query("""
        SELECT u.id, u.name, u.phone_number u.token, by.address, by.city
        FROM Users u
        WHERE u.token = \'{jwt_token}\'
        INNER JOIN Buyer_Shipping by
        ON by.user_id = u.id
        """)[0]

        shipping_data = {
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

        userDetail = run_query("""
        SELECT name, email, phone_number, token
        FROM Users
        WHERE token = \'{jwt_token}\'
        """)
        
        for i in userDetail:
            return {

            }

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
        
        run_query(f'UPDATE Users set name=\'{name}\', phone_number=\'{phone_number}\'', True)
        run_query(f'UPDATE Buyer_Shipping set address=\'{address}\', city=\'{city}\'', True)

        shipping_addresss = run_query('SELECT u.name, u.phone number, b.address, b.city \
        FROM Users u\
        INNER JOIN Buyer_Shipping b\
        ON b.user_id = u.\'"id"\';')

        data = {
            "name": shipping_addresss['name'],
            "phone_number": shipping_addresss['phone_number'],
            "address": shipping_addresss['addess'],
            "city": shipping_addresss['city']
        }
        return data, 200

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

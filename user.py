from flask import Blueprint, request
from utils import run_query, validUser


user_bp = Blueprint("user", __name__, url_prefix="/user")


@user_bp.route("/shipping_address", methods=["GET"])
def getUserShippingAddress():
    try:
        user_sp = run_query("select id, name, phone_number, address, city from From Users \
            inner join Buyer_Shipping using(user_id)")
        data = {
            "id": user_sp['id'],
            "name": user_sp['name'],
            "phone_number": user_sp['phone_number'],
            "address": user_sp['address'],
            "city": user_sp['city']
        }, 200

    except KeyError:
        return {"message": "error, user already exist"}


@user_bp.route("", methods=["GET"])
def userDetail():
    try:
        jwt_token = request.headers.get('Authentication')

        if not validUser(jwt_token, True):
            return {"error": "user not valid"}, 400

        userDetail = run_query("select name, email, phone_number from Users")
        data = {
            "name": userDetail['name'],
            "email": userDetail['email'],
            "phone_number": userDetail['phone_number']
        }
        return data, 200

    except KeyError:
        return {"message": "error, user already exist"}, 400


@user_bp.route("/shipping_address", methods=["POST"])
def changeShippingAddress():
    pass


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

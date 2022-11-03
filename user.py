from flask import Blueprint, request
from utils import run_query, validUser


user_bp = Blueprint("user", __name__, url_prefix="/user")


@user_bp.route("/shipping_address", methods=["GET"])
def getUserShippingAddress():
    pass


@user_bp.route("", methods=["GET"])
def userDetail():
    pass

@user_bp.route("/shipping_address", methods=["GET"])
def changeShippingAddress():
    pass

@user_bp.route("/balance", methods=["POST"])
def topupBalance():
    jwt_token = request.headers.get('Authentication')
    amount = request.args.get("amount")

    if not validUser(jwt_token, True):
        return {"error": "user not valid"}, 400

    if amount <= 0:
        return {"error": "Please specify a positive amount"}, 400

    user = run_query(f"SELECT id FROM Users WHERE token = '{jwt_token}'")[0]["id"]

    run_query(f"UPDATE Buyer_Shipping SET balance = balance + {int(amount)} WHERE user_id = '{user}'", commit=True)
    return {"message": "Top up balance success"}, 200
    

    


@user_bp.route("/balance", methods=["GET"])
def getBalance():
    jwt_token = request.headers.get('Authentication')

    if not validUser(jwt_token, True):
        return {"error": "user not valid"}, 400

    user = run_query(f"SELECT id FROM Users WHERE token = '{jwt_token}'")[0]["id"]
    balance = run_query(f"SELECT balance FROM Buyer_Shipping WHERE user_id = '{user}'")

    data = {
            "balance": balance['balance']
        }, 200
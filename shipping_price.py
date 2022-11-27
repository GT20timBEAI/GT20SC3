from flask import Blueprint, request
from utils import validUser, run_query, checkCartUser
import json


price_bp = Blueprint("shipping_price", __name__, url_prefix="/shipping_price")

# Blank on front end
@price_bp.route("", methods=["GET"])
def getShippingPrice():
    """
    Catatan:
        - Hanya bisa diakses oleh user yang sudah login
        - Hanya bisa diakses oleh user yang sudah memiliki cart 
        - Dihitung based on cart user yang sekarang
    Akan ada 2 jenis shipping method:
        - Regular:
            Jika total harga item < 200: Shipping price merupakan 15% dari total harga item yang dibeli
            Jika total harga item >= 200: Shipping price merupakan 20% dari total harga item yang dibeli
        - Next Day:
            Jika total harga item < 300: Shipping price merupakan 20% dari total harga item yang dibeli
            Jika total harga item >= 300: Shipping price merupakan 25% dari total harga item yang dibeli
    """
    # FIXME: Auth token
    jwt_token = request.headers.get('Authentication')
    if not validUser(jwt_token):
        return {"message": "user not valid"}, 400

    # GET user ID
    id = run_query(f"""
    SELECT id FROM "Users"
    WHERE token = '{jwt_token}'
    """)[0]['id']

    #FIXME: have cart
    if checkCartUser(id) == False: 
        return {"message" : "You not have Item on Cart"}, 400
    # if have, Get data
    else:
        data = checkCartUser(id)
    
    return {"data" : data}, 200
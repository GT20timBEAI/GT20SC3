from flask import Blueprint, request
from app.helper.utils import validUser, run_query
from app.helper.shipping import checkCartUser



price_bp = Blueprint("shipping_price", __name__, url_prefix="/shipping_price")

# Blank on front end
@price_bp.route("", methods=["GET"])
def getShippingPrice():
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
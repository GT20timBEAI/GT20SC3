from flask import Blueprint, request
from services.utils import validUser, run_query

sales_bp = Blueprint("sales", __name__, url_prefix="/sales")



@sales_bp.route("", methods=["GET"])
def gettotalsales():
    jwt_token = request.headers.get("Authentication")
    
    # TODO: check valid user are seller
    if not validUser(jwt_token, True): 
        return {"message" : "user not valid"}, 400

    # GET total sales from database
    sales = run_query("""
    SELECT balance FROM "Users"
    WHERE is_admin = 1
    """)[0]['balance']

    sales = {"total" : sales}
    return {"data" : sales}, 200
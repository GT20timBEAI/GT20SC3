from flask import Blueprint, request
from app.helper.utils import run_query
from app.helper.template import verifEmailPage, errorPage

verif_bp = Blueprint("verif_email", __name__, url_prefix="/verify")

@verif_bp.route("", methods=["GET"])
def verifEmail():
    id = request.args.get('uuid')

    #Get data
    data = run_query(f"""
    Select name, is_admin from "Users"
    WHERE id = '{id}'
    """)

    if len(data) == 0 or data[0]['is_admin'] == 1:
        return errorPage()

    # update user to verif buyer
    run_query(f"""
    UPDATE "Users" 
    SET is_admin = 0
    WHERE id = '{id}'
    """, True)

    # if success
    return verifEmailPage(data[0]['name'])


    



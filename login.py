"""
Requirements (from the earliest to check):
- Password needs to satisfy certain standard:
    - each password will be checked (in this order) whether it:
        - contains >= 8 characters
        - contains >= 1 lowercase letter
        - contains >= upercase letter 
        - contains a number
    - if password is less than 8 characters:
        - return {"error": "Password must contain at least 8 characters"}
        - status code: 400
    - if password doesn't contain any lowercase letters:
        - return {"error": "Password must contain a lowercase letter"}
        - status code: 400
    - if password doesn't contain any uppercase letters:
        - return {"error": "Password must contain an uppercase letter"}
        - status code: 400
    - if password doesn't contain any numbers:
        - return {"error": "Password must contain a number"}
        - status code: 400
-email must be:
    - have alphabet
    - have @ character
    - have alphabet after @
    - have . character after @ character and alphabet
        - return {"error": "your email is wrong"}
        - status code: 400
- if email not registered
    - return {"error": "Email is not registered"}
    - status code: 409
- if password is wrong
    - return {"error": "Your password is wrong"}
    - status code: 409
- if everything is corect
    - return {"user_information" : {
        "name": "Raihan Parlaungan",
        "email": "raihan@gmail.com",
        "phone_number": "08138073126",
        "type:" : "buyer"( there are 2 types of user, "buyer" and "seller"
        } , "token" :  "jwt_token" , "message" : "Login success" }
"""


from flask import Blueprint, request
from utils import run_query, inValid

login_bp = Blueprint("login", __name__, url_prefix="/login")

# import your jwt token to this variabel for testing
testToken = None

# untuk request cek di scr


@login_bp.route("", methods=["POST"])
def login():
    body = request.json
    email, password = body['email'], body['password']

    # TODO: Email Rule
    if inValid(email):
        return {"error": "your email is wrong"}, 400

    # TODO: Password Rule
    if len(password) < 8:
        return {"error": "Password must contain at least 8 characters"}, 400
    elif any(i.islower for i in password) == False:
        return {"error": "Password must contain a lowercase letter"}, 400
    elif any(i.isupper for i in password) == False:
        return {"error": "Password must contain an uppercase letter"}, 400
    elif any(i.isdigit for i in password) == False:
        return {"error": "Password must contain a number"}, 400

    # TODO: Test user Email and Password
    cred_test = run_query(
        "select email, password from users where(email == email)")
    for i in cred_test:
        if email != i["email"]:
            return {"error": "Email is not registered"}, 409
        if password != i["password"]:
            return {"error": "Your password is wrong"}, 409

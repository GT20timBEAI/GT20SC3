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

import jwt
from flask import Blueprint, request
from utils import run_query, inValid, user_jwt

login_bp = Blueprint("login", __name__, url_prefix="/login")

# import your jwt token to this variabel for testing
testToken = user_jwt
# untuk request cek di scr


def token_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        token = request.args.get('token')
        if not token:
            return {"Error": "Authentication is failed"}, 400

        try:
            result = jwt.decode(
                token, user_jwt, algorithms=["HS256"])
        except:
            return {"Authentication Failed 2"}
        return f(*args, **kwargs)
    return decorator


@login_bp.route("", methods=["POST"])
def login():
    body = request.json
    email, password = body['email'], body['password']
    cred_test = run_query("select * from users")

    # TODO: Test user Password
    if len(password) < 8:
        return {"error": "Password must contain at least 8 characters"}, 400
    elif not any(filter(str.islower, password)):
        return {"error": "Password must contain a lowercase letter"}, 400
    elif not any(filter(str.isupper, password)):
        return {"error": "Password must contain an uppercase letter"}, 400
    elif not any(filter(str.isdigit, password)):
        return {"error": "Password must contain a number"}, 400

    # TODO: Test user Email
    if inValid(email):
        return {"error": "your email is wrong"}, 400

    # TODO: Check if email and password is exist in database or not
    for i in cred_test:
        if email != i['email']:
            return {"error": "Email is not registered"}, 409
        if password != i['password']:
            return {"error": "Your password is wrong"}, 409
        return {'user_information': {'name': i['name'], 'email': 'darulcrypto@gmail.com', 'phone number': i['phone_number'], 'type': i['is_admin']}, 'token': testToken, 'message': 'Login succes'}

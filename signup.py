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
-name must be:
    - contains >= 5 characters
        - return {"error": "name must contain at least 5 character"}
        - status code: 400
    - no numbers, symbol and spesial caracter
        - return {"error": "name just alphabet"}
        - status code: 400
-email must be:
    - have alphabet
    - have @ character
    - have alphabet after @
    - have . character after @ character and alphabet
        - if email incorect 
            - return {"error": "your email is wrong"}
            - status code: 400
-phone number must be:
    - just number(no alphabet, simbol and special character)
        - return {"error": "phone just containt number"}
        - status code:400
    - contains = 12 characters
        - return {"error": "phone must contain less than 12 character"}
        - status code:400
- if email already used
    - return {"error": "email already exist"}
    -status code: 409
- if phone number already used
    - return {"error": "phone number already exist"}
    - status code: 409
- if everything is correct 
    - return {"message": "success, user created"}
    - status code: 201
"""

from flask import Blueprint, request
import re

signup_bp = Blueprint("signup", __name__, url_prefix="/sign-up")

# untuk request cek di scr


@signup_bp.route("", methods=["POST"])
def signup():
    try:

        pattern_name = "[a-zA-Z0-9 ]"
        pattern_email = "[a-zA-Z0-9]+@[a-zA-Z]+\.(com|edu|net)"
        body = request.json
        name, email, phone_number, password = body['name'], body[
            'email'], body['phone_number'], body['password']

        # TODO: Name Rule
        if len(name) < 5:
            return {"error": "Name must contain at least 5 characters"}, 400

        if not any(filter(str.islower, name)):
            return {"error": "Name must contain a lowercase letter"}, 400

        if not any(filter(str.isupper, name)):
            return {"error": "Name must contain an uppercase letter"}, 400

        if any(filter(str.isdigit, name)):
            return {"error": "Name only contain alphabet"}, 400

        if not (re.search(pattern_name, name)):
            return {"error": "Name only contain alphabet"}, 400

        # FIXME: Mungkin ada saran lain untuk filter satu ini
        # if any(filter(str.isalnum, name)):
        #     return {"error": "Name only contain alphabet"}, 400

        # TODO: Email Rule
        if not (re.search(pattern_email, email)):
            return {"error": "your email is wrong"}, 400

        # TODO: Phone Number Rule
        if len(phone_number) < 12 and len(phone_number) > 12:
            return {"error": "Phone number must contain 12 characters"}, 400

        if any(filter(str.isalpha, phone_number)):
            return {"error": "name just containt number"}, 400

        # TODO: Password Rule

        if len(password) < 8:
            return {"error": "Password must contain at least 8 characters"}, 400

        if not any(filter(str.islower, password)):
            return {"error": "Password must contain a lowercase letter"}, 400

        if not any(filter(str.isupper, password)):
            return {"error": "Password must contain an uppercase letter"}, 400

        if not any(filter(str.isdigit, password)):
            return {"error": "Password must contain a number"}, 400

    except KeyError:
        return {"error": "name or email or phone number or password are not given"}, 400

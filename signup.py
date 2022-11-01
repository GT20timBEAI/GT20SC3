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
- if request between name, email, phone number not entered:
    return {"error" : "Email, password, name, phone number not entered"}
    status code : 400
- if everything is correct 
    - return {"message": "success, user created"}
    - status code: 201
"""

from flask import Blueprint, request
from utils import check_email, check_number, run_query
import re

signup_bp = Blueprint("signup", __name__, url_prefix="/sign-up")

# untuk request cek di scr
@signup_bp.route("", methods=["POST"])
def signup():
    body = request.json
    name = body["name"]
    email = body["email"]
    phone = body["phone_number"]
    password = body["password"]

    if len(password) < 8:
        return {"error": "Password must contain at least 8 characters"}, 400
    elif not re.search('[a-z]', password):
        return {"error": "Password must contain a lowercase letter"}, 400
    elif not re.search('[A-Z]', password):
        return {"error": "Password must contain an uppercase letter"}, 400
    elif not re.search('[0-9]', password):
        return {"error": "Password must contain a number"}, 400

    if len(name) < 5:
        return {"error": "name must contain at least 5 character"}, 400
    if any(c.isdigit() for c in name) == True:
        return {"error": "name only contain letters"}, 400
    
    if check_email(email):
        return {"error": "your email is wrong"}, 400

    if len(phone) < 12:
        return {"error": "phone must contain less than 12 character"}, 400
    if check_number(phone):
        return {"error": "phone can only containt number"}, 400
    
    users = run_query(f"SELECT email, phone_number FROM users")

    for i in users:
        if email == i["email"]:
            return {"error": "email already exist"}, 409
        if phone == i["phone_number"]:
            return {"error": "phone number already exist"}, 409

    run_query(f"INSERT INTO users(name, email, phone_number, password) VALUES ('{name}', '{email}', '{phone}', '{password}')", commit=True)
    return {"message": "success, user created"}, 201

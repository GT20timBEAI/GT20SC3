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
        - return {"error": "name just containt number"}
        - status code:400
    - contains = 12 characters
        - return {"error": "name must contain 12 character"}
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


from flask import Blueprint

signup_bp = Blueprint("signup", __name__, url_prefix="/sign-up")

# untuk request cek di scr
@signup_bp.route("", methods=["POST"])
def signup():
    pass
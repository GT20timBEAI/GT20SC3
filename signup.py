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

from flask import Blueprint,request
from utils import inValid, run_query, symbol
import uuid

signup_bp = Blueprint("signup", __name__, url_prefix="/sign-up")

# DONE with front end
@signup_bp.route("", methods=["POST"])
def signup():
    try:
        body = request.json
        name, email, phone, password = body["name"], body["email"], body["phone_number"], body["password"]
        users = run_query("select email, phone_number from \"Users\"")
        
        # TODO: Pasword requirements
        if len(password) < 8:
            return {"message": "Password must contain at least 8 characters"},400
        elif any(i.islower() for i in password) == False:
            return {"message": "Password must contain a lowercase letter"}, 400
        elif any(i.isupper() for i in password) == False:
            return {"message": "Password must contain an uppercase letter"}, 400
        elif any(c.isdigit() for c in password) == False:
            return {"message": "Password must contain a number"},400

        # TODO: name requirements  
        elif len(name) < 5: return {"message": "name must contain at least 5 character"},400
        elif any(c.isdigit() for c in name) == True: return {"message": "name just alphabet"},400

        # TODO: email requirements
        elif inValid(email): return {"message": "your email is wrong"}, 400

        #TODO: phone number requirements
        elif symbol(phone): return {"message": "phone just containt number"},400
        elif len(phone) < 12: return {"message": "phone must contain less than 12 character"},400

        #TODO: email and phone exist in database
        for i in users:
            if email == i["email"]:return {"message": "email already exist"}, 409
            if phone == i["phone_number"]: return {"message": "phone number already exist"}, 409

        #TODO: Succesfull
        id = uuid.uuid4()
        run_query(f"insert into \"Users\"(id, name, email, phone_number, password, is_admin, balance)\
             values(\'{id}\',\'{name}\',\'{email}\',{phone},\'{password}\', 0 , 0)", True)
        return {"message": "success, user created"}, 201

    except:
        return {"error" : "Email, password, name, phone number not entered"}, 400

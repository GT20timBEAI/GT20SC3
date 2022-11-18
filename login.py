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

- if between email or passwor not entered
    return {"error" : "Email or password not entered"}
    status code : 400

- if everything is corect
    - return {"user_information" : {
        "name": "Raihan Parlaungan",
        "email": "raihan@gmail.com",
        "phone_number": "628138073126",
        "type:" : "buyer"( there are 2 types of user, "buyer" and "seller"
        } , "token" :  "jwt_token" , "message" : "Login success" }


- using this:
    save token to config["token"]
"""


from flask import Blueprint, request
from utils import run_query, inValid
import jwt

login_bp = Blueprint("login", __name__, url_prefix="/sign-in")


# untuk request cek di scr
@login_bp.route("", methods=["POST"])
def login():
    # try:
    body = request.json
    email, password = body["email"], body["password"]

    # TODO Pasword requirements
    if len(password) < 8:
        return {"error": "Password must contain at least 8 characters"},400
    elif any(i.islower() for i in password) == False:
        return {"error": "Password must contain a lowercase letter"}, 400
    elif any(i.isupper() for i in password) == False:
        return {"error": "Password must contain an uppercase letter"}, 400
    elif any(c.isdigit() for c in password) == False:
        return {"error": "Password must contain a number"},400

    # TODO email requirements
    elif inValid(email): return {"error": "your email is wrong"}, 400
    
    users = run_query("select * from \"Users\"")
    for i in users:
        if i["email"] == email:
            if i["password"] == password:
                token = jwt.encode({"email" : email},
                "inirahasiakita") #dont using algorithm because on output jwt not be
                                  #available to use this case 
                # jwt.decode(token, "inirahasiakita", algorithms=["RS256"]
                type = "buyer" if i["is_admin"] == 0  else "seller"
                run_query(f"update \"Users\" set token=\'{token}\' where email=\'{email}\'", True)
                return {"user_information" : {
                            "name": i["name"],
                            "email": email,
                            "phone_number": i["phone_number"],
                            "type:" : type} ,
                        "message" : "Login success",
                        "token" :  str(token)   }, 200
            return {"error": "Your password is wrong"},409

    return {"error": "Email is not registered"}, 409


    # #TODO if email or password not entered                
    # except:
    #     return {"error" : "Email or password not entered"}, 400


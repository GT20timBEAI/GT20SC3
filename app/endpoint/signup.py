from flask import Blueprint, request
from app.helper.utils import run_query
from app.helper.auth import inValid, symbol
from app.helper.sendemail import sendVerifyEmail
import uuid


signup_bp = Blueprint("signup", __name__, url_prefix="/sign-up")

# DONE with front end
@signup_bp.route("", methods=["POST"])
def signup():
    try:
        body = request.json
        name, email, phone, password = body["name"], body["email"], body["phone_number"], body["password"]
        users = run_query("select email, phone_number from \"Users\"")
        email = email.lower()

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
             values(\'{id}\',\'{name}\',\'{email}\',{phone},\'{password}\', 2 , 0)", True)

        # send email verification
        sendVerifyEmail(name, id, email)

        return {"message": "success, user created Check your email"}, 201

    except:
        return {"error" : "Email, password, name, phone number not entered"}, 400

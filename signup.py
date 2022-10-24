from flask import Blueprint

signup_bp = Blueprint("signup", __name__, url_prefix="/sign-up")

# untuk request cek di scr


@signup_bp.route("", methods=["POST"])
def signup():
    try:

        body = request.json
        name, email, phone_number, password = body['name'], body['email'], body[phone_number], body['password']

        if len(name) < 5:
            return {"error": "Name must contain at least 5 characters"}, 400

        if not any(filter(str.islower, name)):
            return {"error": "Name must contain a lowercase letter"}, 400

        if not any(filter(str.isupper, name)):
            return {"error": "Name must contain an uppercase letter"}, 400

        if len(phone_number) < 12 and len(phone_number) > 12:
            return {"error": "Phone number must contain 12 characters"}, 400

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

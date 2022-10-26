from flask import Flask
import os
from signup import signup_bp
from utils import get_engine
from products import products_bp
from home import home_bp
from login import login_bp, testToken
from categories import categories_bp
from cart import cart_bp
from shipping import shipping_bp
from user import user_bp
from sqlalchemy import (
    MetaData, 
    Table, 
    Column, 
    String, 
    create_engine
    )

def create_app():
    app = Flask(__name__)

    # always register your blueprint(s) when creating application
    blueprints = [signup_bp, login_bp, products_bp, home_bp, categories_bp, cart_bp, shipping_bp, user_bp]
    for blueprint in blueprints:
        app.register_blueprint(blueprint)

    # IMPLEMENT THIS
    # - setup SQLite database (if already exists, clear/reset the database)
    # - create necessary tables
    db_name = "finalproject.db"
    if os.path.isfile(db_name):
        os.remove(db_name)
    
    # buat table dengan template ORM dibawah
    engine = get_engine()
    meta = MetaData()
    Table(
        "users",
        meta,
        Column("type", String, nullable=False),
        Column("username", String, nullable=False,unique = True),
        Column("password", String, nullable=False),
        Column("token", String, nullable=True)
    )
    meta.create_all(engine)

    return app



app = create_app()

# =======================================================
#                     TESTING
# =======================================================


if __name__ == "__main__":
    from utils import assert_eq
    from utils import COL
    app.config.update({"TESTING": True})
    c = app.test_client()

    print(f"{COL.BOLD}Testing...{COL.ENDC}")

    # register user
    register_user_response = c.post(
        "/sign-up",
        json={"name": "darul","email" : "darulcrypto@gmail.com", "phone_number": "085268487440", "password": "Ab123456"},
    )
    assert_eq(
        register_user_response.json,
        {"message": "success, user created"},
    )
    assert_eq(register_user_response.status_code, 201)

    # password incorect(less than 8 character)
    register_user_response = c.post(
        "/sign-up",
        json={"name": "wahyu","email" : "wahyusani@gmail.com", "phone_number": "085268487440", "password": "456"},
    )
    assert_eq(
        register_user_response.json,
        {"error": "Password must contain at least 8 characters"},
    )
    assert_eq(register_user_response.status_code, 400)

    # password incorect(doesn't contain any lowercase letters)
    register_user_response = c.post(
        "/sign-up",
        json={"name": "wahyu","email" : "wahyusani@gmail.com", "phone_number": "085268487440", "password": "ABCD456"},
    )
    assert_eq(
        register_user_response.json,
        {"error": "Password must contain a lowercase letter"},
    )
    assert_eq(register_user_response.status_code, 400)

    # password incorect(doesn't contain any uppercase letters)
    register_user_response = c.post(
        "/sign-up",
        json={"name": "wahyu","email" : "wahyusani@gmail.com", "phone_number": "085268487440", "password": "abcde456"},
    )
    assert_eq(
        register_user_response.json,
        {"error": "Password must contain an uppercase letter"},
    )
    assert_eq(register_user_response.status_code, 400)


    # password incorect(doesn't contain any numbers)
    register_user_response = c.post(
        "/sign-up",
        json={"name": "wahyu","email" : "wahyusani@gmail.com", "phone_number": "085268487440", "password": "abcDdeabc"},
    )
    assert_eq(
        register_user_response.json,
        {"error": "Password must contain a number"},
    )
    assert_eq(register_user_response.status_code, 400)

    # name incorect(name less than 5 caracter)
    register_user_response = c.post(
        "/sign-up",
        json={"name": "wa","email" : "wahyusani@gmail.com", "phone_number": "085268487440", "password": "abcDdeabc123"},
    )
    assert_eq(
        register_user_response.json,
        {"error": "name must contain at least 5 character"},
    )
    assert_eq(register_user_response.status_code, 400)

    # name incorect(name just alphabet)
    register_user_response = c.post(
        "/sign-up",
        json={"name": "wahayu123","email" : "wahyusani@gmail.com", "phone_number": "085268487440", "password": "abcDdeabc123"},
    )
    assert_eq(
        register_user_response.json,
        {"error": "name just alphabet"},
    )
    assert_eq(register_user_response.status_code, 400)

    # testing email
    register_user_response = c.post(
        "/sign-up",
        json={"name": "wahayu123","email" : "wahyusani", "phone_number": "085268487440", "password": "abcDdeabc123"},
    )
    assert_eq(
        register_user_response.json,
        {"error": "your email is wrong"},
    )
    assert_eq(register_user_response.status_code, 400)

    # testing email
    register_user_response = c.post(
        "/sign-up",
        json={"name": "wahayu123","email" : "wahyusani@", "phone_number": "085268487440", "password": "abcDdeabc123"},
    )
    assert_eq(
        register_user_response.json,
        {"error": "your email is wrong"},
    )
    assert_eq(register_user_response.status_code, 400)

    # testing email
    register_user_response = c.post(
        "/sign-up",
        json={"name": "wahayu123","email" : "wahyusani@gmail", "phone_number": "085268487440", "password": "abcDdeabc123"},
    )
    assert_eq(
        register_user_response.json,
        {"error": "your email is wrong"},
    )
    assert_eq(register_user_response.status_code, 400)

    # testing email
    register_user_response = c.post(
        "/sign-up",
        json={"name": "wahayu123","email" : "wahyusani@gmail.", "phone_number": "085268487440", "password": "abcDdeabc123"},
    )
    assert_eq(
        register_user_response.json,
        {"error": "your email is wrong"},
    )
    assert_eq(register_user_response.status_code, 400)

    # testing phone number
    register_user_response = c.post(
        "/sign-up",
        json={"name": "darul","email" : "darulc8rypto@gmail.com", "phone_number": "0852684874", "password": "Ab123456"},
    )
    assert_eq(
        register_user_response.json,
        {"error": "name must contain 12 character"},
    )
    assert_eq(register_user_response.status_code, 400)

    # testing phone number
    register_user_response = c.post(
        "/sign-up",
        json={"name": "darul","email" : "darulcryptop@gmail.com", "phone_number": "08526848744!", "password": "Ab123456"},
    )
    assert_eq(
        register_user_response.json,
        {"error": "name just containt number"},
    )
    assert_eq(register_user_response.status_code, 400)

    # testing mail address
    register_user_response = c.post(
        "/sign-up",
        json={"name": "darul","email" : "darulcrypto@gmail.com", "phone_number": "085268487440", "password": "Ab123456"},
    )
    assert_eq(
        register_user_response.json,
        {"error": "email already exist"},
    )
    assert_eq(register_user_response.status_code, 409)

    # testing phone number
    register_user_response = c.post(
        "/sign-up",
        json={"name": "darul","email" : "darulcryp7to@gmail.com", "phone_number": "085268487440", "password": "Ab123456"},
    )
    assert_eq(
        register_user_response.json,
        {"error": "phone number already exist"},
    )
    assert_eq(register_user_response.status_code, 409)

    # register user
    register_user_response = c.post(
        "/sign-up",
        json={"name": "wahyu sani","email" : "wahyusani@gmail.com", "phone_number": "085268487040", "password": "Ab123456"},
    )
    assert_eq(
        register_user_response.json,
        {"message": "success, user created"},
    )
    assert_eq(register_user_response.status_code, 201)

    """
    ================================================
                    TESTING LOGIN
    ================================================
    """
    # password is less than 8 characters
    register_user_response = c.post(
        "/login",
        json={"email" : "darulcrypto@gmail.com", "password" : "ABC"},
    )
    assert_eq(
        register_user_response.json,
        {"error": "Password must contain at least 8 characters"},
    )
    assert_eq(register_user_response.status_code, 400)

    # password doesn't contain any lowercase letters
    register_user_response = c.post(
        "/login",
        json={"email" : "darulcrypto@gmail.com", "password" : "ABC123456"},
    )
    assert_eq(
        register_user_response.json,
        {"error": "Password must contain a lowercase letter"},
    )
    assert_eq(register_user_response.status_code, 400)

    # password doesn't contain any lowercase letters
    register_user_response = c.post(
        "/login",
        json={"email" : "darulcrypto@gmail.com", "password" : "abc123456"},
    )
    assert_eq(
        register_user_response.json,
        {"error": "Password must contain an uppercase letter"},
    )
    assert_eq(register_user_response.status_code, 400)

    # password doesn't contain any lowercase letters
    register_user_response = c.post(
        "/login",
        json={"email" : "darulcrypto@gmail.com", "password" : "abcABCDE"},
    )
    assert_eq(
        register_user_response.json,
        {"error": "Password must contain a number"},
    )
    assert_eq(register_user_response.status_code, 400)

    # testing email
    register_user_response = c.post(
        "/login",
        json={"email" : "darulcrypto", "password" : "Ab123456"},
    )
    assert_eq(
        register_user_response.json,
        {"error": "your email is wrong"},
    )
    assert_eq(register_user_response.status_code, 400)

    # testing email
    register_user_response = c.post(
        "/login",
        json={"email" : "darulcrypto@", "password" : "Ab123456"},
    )
    assert_eq(
        register_user_response.json,
        {"error": "your email is wrong"},
    )
    assert_eq(register_user_response.status_code, 400)

    # testing email
    register_user_response = c.post(
        "/login",
        json={"email" : "darulcrypto@gmail", "password" : "Ab123456"},
    )
    assert_eq(
        register_user_response.json,
        {"error": "your email is wrong"},
    )
    assert_eq(register_user_response.status_code, 400)

    # email not registered
    register_user_response = c.post(
        "/login",
        json={"email" : "darulcrypto7@gmail.com", "password" : "Ab123456"},
    )
    assert_eq(
        register_user_response.json,
        {"error": "Email is not registered"},
    )
    assert_eq(register_user_response.status_code, 409)

    # password wrong
    register_user_response = c.post(
        "/login",
        json={"email" : "darulcrypto@gmail.com", "password" : "Abc123456"},
    )
    assert_eq(
        register_user_response.json,
        {"error": "Your password is wrong"},
    )
    assert_eq(register_user_response.status_code, 409)

    # succesful login
    
    register_user_response = c.post(
        "/login",
        json={"email" : "darulcrypto@gmail.com", "password" : "Ab123456"},
    )
    assert_eq(
        register_user_response.json,
        {"user_information" : {"name": "darul",
        "email": "darulcrypto@gmail.com",
        "phone_number": "085268487440",
        "type:" : "buyer"
        },"token" :  testToken , "message": "Login succes"},
    )
    assert_eq(register_user_response.status_code, 200)


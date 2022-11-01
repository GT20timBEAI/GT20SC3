from flask import Flask
import os
from image import image_bp
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
    create_engine,
    Integer,
    )



def create_app():
    app = Flask(__name__)

    # always register your blueprint(s) when creating application
    blueprints = [signup_bp, login_bp, products_bp, home_bp, categories_bp, cart_bp, shipping_bp, user_bp, image_bp]
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
        Column("id", Integer, primary_key= True),
        Column("name", String, nullable=False),
        Column("email", String, nullable=False, unique= True),
        Column("phone_number", String, nullable=False, unique=True),
        Column("password", String, nullable=False),
        Column("is_admin", Integer, nullable=True, default=0)
    )
    meta.create_all(engine)

    return app



app = create_app()

class IsString:
    def __eq__(self, other):
        return isinstance(other, str)

    def __repr__(self):
        return "<must_be_a_string>"
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
        json={"name": "darul","email" : "darulcrypto@gmail.com", "phone_number": "6285268487440", "password": "Ab123456"},
    )
    assert_eq(
        register_user_response.json,
        {"message": "success, user created"},
    )
    assert_eq(register_user_response.status_code, 201)
    num=1
    print("==================================================")
    print(f" [task {num} passed ] succes created user                         ")
    print("==================================================")
    num+=1
    # password incorect(less than 8 character)
    register_user_response = c.post(
        "/sign-up",
        json={"name": "wahyu","email" : "wahyusani@gmail.com", "phone_number": "6285268487440", "password": "456"},
    )
    assert_eq(
        register_user_response.json,
        {"error": "Password must contain at least 8 characters"},
    )
    assert_eq(register_user_response.status_code, 400)
    print("==================================================")
    print(f"[task {num} passed ] Password less than 8 letters                         ")
    print("==================================================")
    num+=1
    # password incorect(doesn't contain any lowercase letters)
    register_user_response = c.post(
        "/sign-up",
        json={"name": "wahyu","email" : "wahyusani@gmail.com", "phone_number": "6285268487440", "password": "ABCD4567"},
    )
    assert_eq(
        register_user_response.json,
        {"error": "Password must contain a lowercase letter"},
    )
    assert_eq(register_user_response.status_code, 400)
    print("==================================================")
    print(f"[task {num} passed ] Password not contain lowercase letter                        ")
    print("==================================================")
    num+=1

    # password incorect(doesn't contain any uppercase letters)
    register_user_response = c.post(
        "/sign-up",
        json={"name": "wahyu","email" : "wahyusani@gmail.com", "phone_number": "6285268487440", "password": "abcde456"},
    )
    assert_eq(
        register_user_response.json,
        {"error": "Password must contain an uppercase letter"},
    )
    assert_eq(register_user_response.status_code, 400)
    print("==================================================")
    print(f"[task {num} passed ] Password not contain uppercase letter                         ")
    print("==================================================")

    

    # password incorect(doesn't contain any numbers)
    register_user_response = c.post(
        "/sign-up",
        json={"name": "wahyu","email" : "wahyusani@gmail.com", "phone_number": "6285268487440", "password": "abcDdeabc"},
    )
    assert_eq(
        register_user_response.json,
        {"error": "Password must contain a number"},
    )
    assert_eq(register_user_response.status_code, 400)
    print("==================================================")
    print(f" [task {num} passed ] password must contain a number                         ")
    print("==================================================")
    num += 1

    # name incorect(name less than 5 caracter)
    register_user_response = c.post(
        "/sign-up",
        json={"name": "wa","email" : "wahyusani@gmail.com", "phone_number": "6285268487440", "password": "abcDdeabc123"},
    )
    assert_eq(
        register_user_response.json,
        {"error": "name must contain at least 5 character"},
    )
    assert_eq(register_user_response.status_code, 400)
    print("==================================================")
    print(f" [task {num} passed ] name must contain at least 5 character                       ")
    print("==================================================")
    num+=1
    
    # name incorect(name just alphabet)
    register_user_response = c.post(
        "/sign-up",
        json={"name": "wahayu123","email" : "wahyusani@gmail.com", "phone_number": "6285268487440", "password": "abcDdeabc123"},
    )
    assert_eq(
        register_user_response.json,
        {"error": "name only contain letters"},
    )
    assert_eq(register_user_response.status_code, 400)
    print("==================================================")
    print(f" [task {num} passed ] name only contain letters                        ")
    print("==================================================")
    num+=1
    
    # testing email
    register_user_response = c.post(
        "/sign-up",
        json={"name": "wahayu","email" : "wahyusani", "phone_number": "6285268487440", "password": "abcDdeabc123"},
    )
    assert_eq(
        register_user_response.json,
        {"error": "your email is wrong"},
    )
    assert_eq(register_user_response.status_code, 400)
    print("==================================================")
    print(f"  [task {num} passed ] Email is wrong           ")
    print("==================================================")
    num+=1
    
    # testing email
    register_user_response = c.post(
        "/sign-up",
        json={"name": "wahayu","email" : "wahyusani@", "phone_number": "6285268487440", "password": "abcDdeabc123"},
    )
    assert_eq(
        register_user_response.json,
        {"error": "your email is wrong"},
    )
    assert_eq(register_user_response.status_code, 400)
    print("==================================================")
    print(f" [task {num} passed ] Email is wrong                        ")
    print("==================================================")
    num+=1
    
    # testing email
    register_user_response = c.post(
        "/sign-up",
        json={"name": "wahayu","email" : "wahyusani@gmail", "phone_number": "6285268487440", "password": "abcDdeabc123"},
    )
    assert_eq(
        register_user_response.json,
        {"error": "your email is wrong"},
    )
    assert_eq(register_user_response.status_code, 400)
    print("==================================================")
    print(f"    [task {num} passed ] Email is wrong                         ")
    print("==================================================")
    num+=1
    
    # testing email
    register_user_response = c.post(
        "/sign-up",
        json={"name": "wahayu","email" : "wahyusani@gmail.", "phone_number": "6285268487440", "password": "abcDdeabc123"},
    )
    assert_eq(
        register_user_response.json,
        {"error": "your email is wrong"},
    )
    assert_eq(register_user_response.status_code, 400)
    print("==================================================")
    print(f"   [task {num} passed ] Email is wrong                          ")
    print("==================================================")
    num+=1
    
    # testing phone number
    register_user_response = c.post(
        "/sign-up",
        json={"name": "darul","email" : "darulc8rypto@gmail.com", "phone_number": "62852684874", "password": "Ab123456"},
    )
    assert_eq(
        register_user_response.json,
        {"error": "phone must contain less than 12 character"},
    )
    assert_eq(register_user_response.status_code, 400)
    print("==================================================")
    print(f"[task {num} passed ] phone must contain less than 12 character                        ")
    print("==================================================")
    num+=1
    
    # testing phone number
    register_user_response = c.post(
        "/sign-up",
        json={"name": "darul","email" : "darulcryptop@gmail.com", "phone_number": "628526848744!", "password": "Ab123456"},
    )
    assert_eq(
        register_user_response.json,
        {"error": "phone can only containt number"},
    )
    assert_eq(register_user_response.status_code, 400)
    print("==================================================")
    print(f" [task {num} passed ] phone can only containt number                         ")
    print("==================================================")
    num+=1
    
    # testing mail address
    register_user_response = c.post(
        "/sign-up",
        json={"name": "darul","email" : "darulcrypto@gmail.com", "phone_number": "6285268487440", "password": "Ab123456"},
    )
    assert_eq(
        register_user_response.json,
        {"error": "email already exist"},
    )
    assert_eq(register_user_response.status_code, 409)
    print("==================================================")
    print(f"   [task {num} passed ] email already exist                        ")
    print("==================================================")
    num+=1
    
    # testing phone number
    register_user_response = c.post(
        "/sign-up",
        json={"name": "darul","email" : "darulcryp7to@gmail.com", "phone_number": "6285268487440", "password": "Ab123456"},
    )
    assert_eq(
        register_user_response.json,
        {"error": "phone number already exist"},
    )
    assert_eq(register_user_response.status_code, 409)
    print("==================================================")
    print(f" [task {num} passed ] phone number already exist                         ")
    print("==================================================")
    num+=1
    
    # register user
    register_user_response = c.post(
        "/sign-up",
        json={"name": "wahyu sani","email" : "wahyusani@gmail.com", "phone_number": "6285268487040", "password": "Ab123456"},
    )
    assert_eq(
        register_user_response.json,
        {"message": "success, user created"},
    )
    assert_eq(register_user_response.status_code, 201)
    print("==================================================")
    print(f"       [task {num} passed ] success, user created                      ")
    print("==================================================")
    num+=1

    # request not input
    register_user_response = c.post(
        "/sign-up",
        json={"password": "Ab123456"},
    )
    assert_eq(
        register_user_response.json,
        {"error" : "Email, password, name, phone number not entered"},
    )
    assert_eq(register_user_response.status_code, 400)
    print("==================================================")
    print(f"       [task {num} passed ] success, user created                      ")
    print("==================================================")

    
    """
    ================================================
                    TESTING LOGIN
    ================================================
    """

    print("\n\n\n\n             L O G I N")
    num=1
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
    print("\n\n\n\n\n==================================================")
    print(f" [Task {num}] password is less than 8 characters                        ")
    print("==================================================")
    num+=1
    
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
    print("==================================================")
    print(f"[Task {num}] password doesn't contain any lowercase                     ")
    print("==================================================")
    num+=1
    
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
    print("==================================================")
    print(f"[Task {num}] password doesn't contain any lowercase                    ")
    print("==================================================")
    num+=1
    
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
    print("==================================================")
    print(f"[Task {num}] password doesn't contain any lowercase                     ")
    print("==================================================")
    num+=1
    
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
    print("==================================================")
    print(f"            [Task {num}] testing email                       ")
    print("==================================================")
    num+=1
    
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
    print("==================================================")
    print(f"        [Task {num}] testing email                       ")
    print("==================================================")
    num+=1
    
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
    print("==================================================")
    print(f"            [Task {num}] testing email                      ")
    print("==================================================")
    num+=1
    
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
    print("==================================================")
    print(f"      [Task {num}]  email not registered                     ")
    print("==================================================")
    num+=1
    
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
    print("==================================================")
    print(f"            [Task {num}]  password wrong                  ")
    print("==================================================")
    num+=1

    # not entered email or password
    register_user_response = c.post(
        "/login",
        json={"password" : "Ab123456"},
    )
    assert_eq(
        register_user_response.json,
        {"error" : "Email or password not entered"},
    )
    assert_eq(register_user_response.status_code, 400)
    print("==================================================")
    print(f"   [Task {num}]  not entered email or password                    ")
    print("==================================================")
    num+=1

    # succesful login
    register_user_response = c.post(
        "/login",
        json={"email" : "darulcrypto@gmail.com", "password" : "Ab123456"},
    )
    assert_eq(
        register_user_response.json,
        {"user_information" : {"name": "darul",
        "email": "darulcrypto@gmail.com",
        "phone_number": "6285268487440",
        "type:" : "buyer"},
        "message": "Login succes","token" :  IsString()
        }
    )
    assert_eq(register_user_response.status_code, 200)
    print("==================================================")
    print(f"           [Task {num}] succesful login                      ")
    print("==================================================")
    num+=1
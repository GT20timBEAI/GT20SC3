from flask import Flask
import os
from signup import signup_bp
from utils import get_engine
from products import products_bp
from home import home_bp
from login import login_bp
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
    register_seller_response = c.post(
        "/sign-up",
        json={"name": "darul","email" : "darulcrypto@gmail.com", "username": "darulcrypto", "password": "Ab123456"},
    )
    assert_eq(
        register_seller_response.json,
        {"message": "success, user created"},
    )
    assert_eq(register_seller_response.status_code, 201)

    # password incorect
    register_buyer_response = c.post(
        "/register",
        json={"name": "wahyu","email" : "wahyusani@gmail.com", "username": "A", "password": "Ab123456"},
    )
    assert_eq(
        register_buyer_response.json,
        {"error": "username already used"},
    )
    assert_eq(register_buyer_response.status_code, 400)

    # example for invalid password
    invalid_password_response = c.post(
        "/register",
        json={"name": "rohma","email" : "rohma@gmail.com", "username": "c", "password": "ABZZCDZZ"},
    )
    assert_eq(
        invalid_password_response.json,
        {"error": "Password must contain a lowercase letter"},
    )
    assert_eq(invalid_password_response.status_code, 400)

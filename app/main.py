from flask import Flask
from app.static.swagger import swagger_ui_blueprint
from app.endpoint.verifEmail import verif_bp
from app.endpoint.sales import sales_bp
from app.endpoint.image import image_bp
from app.endpoint.getOrder import getOrder_bp
from app.endpoint.signup import signup_bp
from app.helper.utils import get_engine
from app.endpoint.products import products_bp
from app.endpoint.home import home_bp
from app.endpoint.login import login_bp
from app.endpoint.categories import categories_bp
from app.endpoint.cart import cart_bp
from app.endpoint.shipping import shipping_bp
from app.endpoint.user import user_bp
from app.endpoint.shipping_price import price_bp
from sqlalchemy import (
    MetaData, 
    Table, 
    Column, 
    String, 
    Integer,
    ForeignKey,
    BigInteger
    )
from flask_cors import CORS



cors = CORS()

def create_app():
    app = Flask(__name__)
    cors.init_app(app)
    # always register your blueprint(s) when creating application
    blueprints = [verif_bp, signup_bp, login_bp, products_bp, home_bp, categories_bp, cart_bp, shipping_bp, user_bp, image_bp, price_bp, sales_bp, getOrder_bp, swagger_ui_blueprint]
    for blueprint in blueprints:
        app.register_blueprint(blueprint)
    
    # from app.services.utils import run_query
    # import uuid
    # id = uuid.uuid4()
    # run_query(f"insert into \"Users\" (id, name, email, phone_number,\
    #     password,is_admin, balance) VALUES (\'{id}\', \'Darul\', \'gt20@gmail.com\',\
    #         6285268487441, \'Qwerty123\', 1, '0')", True)
    # run_query("""
    #     drop table "Users", "Category", "Product_list", "Cart", "Orders", "Buyer_Shipping", "Image"
    #     """, True)
    # buat table dengan template ORM dibawah
    engine = get_engine()
    meta = MetaData()
    Table(
        "Users",
        meta,
        Column("id", String, primary_key= True),
        Column("name", String, nullable=False),
        Column("email", String, nullable=False, unique= True),
        Column("phone_number", String, nullable=False, unique=True),
        Column("password", String, nullable=False),
        Column("is_admin", Integer, nullable=True),
        Column("token", String, nullable=True),
        Column("balance", BigInteger, nullable=True)
    )

    Table(
        "Category",
        meta,
        Column("category_id", String, primary_key= True),
        Column("category_name", String, nullable=False, unique=True)
        
    )

    Table(
        "Product_list",
        meta,
        Column("id", String, primary_key= True),
        Column("category_id", String, ForeignKey("Category.category_id")),
        Column("product_name", String, nullable=False, unique= True),
        Column("condition", String, nullable=False),
        Column("price", Integer, nullable=False),
        Column("product_detail", String, nullable=True),
        Column("status", Integer, nullable=False)
    )


    Table(
        "Orders",
        meta,
        Column("order_id", String, primary_key=True),
        Column("created_at", String),
        Column("name", String, nullable=False),
        Column("address", String, nullable=False),
        Column("city", String, nullable=False),
        Column("phone_number", String, nullable=False)
    )

    Table(
        "Cart",
        meta,
        Column("cart_id", String, primary_key=True),
        Column("item_id", String, ForeignKey(
            "Product_list.id"), nullable=False),
        Column("user_id", String, ForeignKey("Users.id"), nullable=False),
        Column("order_id", String, ForeignKey(
            "Orders.order_id"), nullable=True),
        Column("quantity", Integer, nullable=False),
        Column("size", String, nullable=False),
        Column("status", String, nullable=True),
        Column("shipping_method", String, nullable=True)
    )

    Table(
        "Buyer_Shipping",
        meta,
        Column("user_id", String, ForeignKey("Users.id"), nullable=False),
        Column("address", String, nullable=False),
        Column("city", String, nullable=False),
        Column("name", String, nullable=False),
        Column("phone_number", BigInteger, nullable=False)
    )

    Table(
        "Image",
        meta,
        Column("product_id", String, ForeignKey("Product_list.id"), nullable=False),
        Column("image_url", String, nullable=False)
    )

    
    meta.create_all(engine)

    return app

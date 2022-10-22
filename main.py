from flask import Flask
import os
from signup import signup_bp
from utils import get_engine_bp
from products import products_bp
from home import home_bp
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
    blueprints = [signup_bp, login_bp, products_bp, home_bp]
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
from flask import Blueprint
from utils import run_query


home_bp = Blueprint("home", __name__, url_prefix="/home")


@home_bp.route("/banner", methods=["GET"])
def getBanner():
    banner = run_query("select * from Banner")
    banner_data = []
    for i in banner:
        banner_data.append(i)
    return {"data": banner_data}, 200


@home_bp.route("/category", methods=["GET"])
def getCategory():
    Category_ = run_query(
        "select Product_List.id, Product_List.image_url, Category.category_name \
        inner join Category ON Product_List.id = Category.category_id")
    category_data = []
    for i in Category_:
        category_data.append(i)
    return {"data": category_data}, 200

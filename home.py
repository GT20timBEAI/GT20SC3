from flask import Blueprint
from utils import run_query

home_bp = Blueprint("home", __name__, url_prefix="/home")


@home_bp.route("/banner", methods=["GET"])
def getBanner():
    banner = run_query("select id, image, title from Banner")
    list_banner = []
    for i in banner:
        list_banner.append(i)
    return {"data": list_banner}

@home_bp.route("/category", methods=["GET"])
def getCategory():
    data = run_query("SELECT Product_list.id, Product_list.image_url, Category.category_name INNER JOIN Category ON Product_list.category_id=Category.category_id")
    list = []
    for i in data:
        list.append(i)
    return {"data": [list]}
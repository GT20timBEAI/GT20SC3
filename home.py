from flask import Blueprint


home_bp = Blueprint("home", __name__, url_prefix="/home")


@home_bp.route("/banner", methods=["GET"])
def getBanner():
    pass

@home_bp.route("/category", methods=["GET"])
def getCategory():
    pass
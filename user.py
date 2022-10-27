from flask import Blueprint


user_bp = Blueprint("user", __name__, url_prefix="/user")


@user_bp.route("/shipping_address", methods=["GET"])
def getUserShippingAddress():
    pass


@user_bp.route("", methods=["GET"])
def userDetail():
    pass

@user_bp.route("/shipping_address", methods=["GET"])
def changeShippingAddress():
    pass

@user_bp.route("/balance", methods=["POST"])
def topupBalance():
    pass


@user_bp.route("/balance", methods=["GET"])
def getBalance():
    pass



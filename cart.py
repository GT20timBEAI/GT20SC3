from flask import Blueprint


cart_bp = Blueprint("cart", __name__, url_prefix="/cart")


@cart_bp.route("", methods=["POST"])
def addtoCart():
    pass


@cart_bp.route("", methods=["GET"])
def getUserCart():
    pass


@cart_bp.route("/{cart_id}", methods=["DELETE"])
def deleteCartItem():
    pass
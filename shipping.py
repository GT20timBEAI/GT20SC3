from flask import Blueprint


shipping_bp = Blueprint("shipping", __name__)


@shipping_bp.route("/shipping_price", methods=["GET"])
def getShippingPrice():
    pass

@shipping_bp.route("/order", methods=["POST"])
def createOrder():
    pass

@shipping_bp.route("/order", methods=["GET"])
def userOrder():
    pass

@shipping_bp.route("/orders", methods=["GET"])
def getOrder():
    pass

@shipping_bp.route("/sales", methods=["GET"])
def gettotalsales():
    pass

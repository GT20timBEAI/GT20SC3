from flask import Blueprint, request
from utils import run_query


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
    # args = request.args
    # if "is_admin" in args.keys() == True:
    #     pass
    pass
    # token = request.headers.get('token')
    # admin = request.args.get('is_admin')
    # data = run_query()
    # if is_admin == '1':
    #     return run_query


@shipping_bp.route("/sales", methods=["GET"])
def gettotalsales():
    pass

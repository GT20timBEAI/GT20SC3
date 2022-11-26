from flask import Blueprint


shipping_bp = Blueprint("shipping", __name__)


@shipping_bp.route("/shipping_price", methods=["GET"])
def getShippingPrice():
    """
    Catatan:
        - Hanya bisa diakses oleh user yang sudah login
        - Hanya bisa diakses oleh user yang sudah memiliki cart 
        - Dihitung based on cart user yang sekarang
    Akan ada 2 jenis shipping method:
        - Regular:
            Jika total harga item < 200: Shipping price merupakan 15% dari total harga item yang dibeli
            Jika total harga item >= 200: Shipping price merupakan 20% dari total harga item yang dibeli
        - Next Day:
            Jika total harga item < 300: Shipping price merupakan 20% dari total harga item yang dibeli
            Jika total harga item >= 300: Shipping price merupakan 25% dari total harga item yang dibeli
    """
    # FIXME: Auth token


    #FIXME: have cart


    #TODO: based on cart


    #TODO: must complete based on cart


@shipping_bp.route("/order", methods=["POST"])
def createOrder():
    pass

@shipping_bp.route("/order", methods=["GET"])
def userOrder():
    pass

# FIXME: In Admin Page
@shipping_bp.route("/orders", methods=["GET"])
def getOrder():
    pass

@shipping_bp.route("/sales", methods=["GET"])
def gettotalsales():
    pass



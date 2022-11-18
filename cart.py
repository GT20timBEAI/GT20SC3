from flask import Blueprint
from utils import run_query, validUser

cart_bp = Blueprint("cart", __name__, url_prefix="/cart")


@cart_bp.route("", methods=["POST"])
def addtoCart():
    try:
        pass

    except SQLAlchemyError:
        return {"error": "user already exist"}


@cart_bp.route("", methods=["GET"])
def getUserCart():
    try:
        jwt_token = request.headers.get('Authentication')
        cart_data = run_query("SELECT c.Cart_id, c.quantity, c.size, c.item_id p.price, p.image_url, p.product_name\
                              FROM Cart c\
                              INNER JOIN Product_List p\
                              ON p.\"id\" = c.item_id;")
        data = [{
            "id": cart_data["Cart_id"],
            "details": {
                "quantity": cart_data["quantity"],
                "size": cart_data["size"]
            },
            "price": cart_data["price"],
            "image": cart_data["image_url"],
            "name": cart_data["product_name"]
        }]
        return data, 200

    except SQLAlchemyError:
        return {"Error": "Not found cart data"}


@cart_bp.route("/{cart_id}", methods=["DELETE"])
def deleteCartItem():
    pass

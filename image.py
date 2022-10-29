from flask import Blueprint

image_bp = Blueprint("image", __name__, url_prefix="/image/<path:urlPath>")

@image_bp.route("", methods=["GET"])
def getImage(urlPath):
    pass
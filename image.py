from flask import Blueprint, send_file
image_bp = Blueprint("image", __name__, url_prefix="/image/<path:urlPath>")


@image_bp.route("", methods=["GET"])
def getImage(urlPath):
    return send_file(f"image/{urlPath}")

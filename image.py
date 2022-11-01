from flask import Blueprint, send_file
from utils import serve_image, extensionImage
import io
image_bp = Blueprint("image", __name__, url_prefix="/image/<path:urlPath>")


@image_bp.route("", methods=["GET"])
def getImage(urlPath):
    try:
        extension = extensionImage(urlPath)
        if not extensionImage(urlPath):
            return {"message": "error, user already exist"}
        content = serve_image(urlPath)
        return send_file(io.BytesIO(content), mimetype=f"image/{extension}")
    except KeyError:
        return {"message": "error, image not found"}, 404

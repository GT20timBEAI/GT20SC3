
from flask import Blueprint, send_file
import io
from utils import serveImage, extensionImage

image_bp = Blueprint("image", __name__, url_prefix="/image/<path:urlPath>")

@image_bp.route("", methods=["GET"])
def getImage(urlPath):
    extension = extensionImage(urlPath)
    conten = serveImage(urlPath)
    return send_file(io.BytesIO(conten), mimetype=f"image/{extension}")





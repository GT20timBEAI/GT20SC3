from flask import Blueprint, send_file
import io
from utils import serveImage, extensionImage

image_bp = Blueprint("image", __name__, url_prefix="/image/<path:urlPath>")

@image_bp.route("", methods=["GET"])
def getImage(urlPath):
    try:
        extension = extensionImage(urlPath)
        if not extensionImage(urlPath):return {"message" : "error, Image not Found"},400
        conten = serveImage(urlPath)
        return send_file(io.BytesIO(conten), mimetype=f"image/{extension}")
    except:
        return {"message" : "error, Image not Found"},400
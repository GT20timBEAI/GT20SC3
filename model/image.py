from flask import Blueprint, send_file
import io
from services.image import  extensionImage, getStorageImage


image_bp = Blueprint("image", __name__, url_prefix="/image/<path:urlPath>")

@image_bp.route("", methods=["GET"])
def getImage(urlPath):
  
    extension = extensionImage(urlPath)
    if not extensionImage(urlPath):return {"message" : "error, Image not Found"},400
    conten = getStorageImage(urlPath)
    return send_file(io.BytesIO(conten), mimetype=f"{extension}")






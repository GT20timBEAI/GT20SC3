import os
from flask import Blueprint, send_file
import io


image_bp = Blueprint("image", __name__, url_prefix="/image/<path:urlPath>")

@image_bp.route("", methods=["GET"])
def getImage(urlPath):
    extension = extensionImage(urlPath)
    conten = serveImage(urlPath)
    return send_file(io.BytesIO(conten), mimetype=f"image/{extension}")


def serveImage(urlPath):
    #TODO: convert image to bytes
    with open(f"image/{urlPath}", "rb") as image:
        f = image.read()
        return f


def extensionImage(image):
    #TODO: get extension

    allow = ['jpg', 'png']
    extension = image.split('.')[1]

    if extension not in allow:
        os.abort()
    
    return extension



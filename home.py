from flask import Blueprint


home_bp = Blueprint("home", __name__, url_prefix="/home")

# untuk request cek di scr
@home_bp.route("/{namefile.extension}", methods=["GET"])
def getImage():
    pass

@home_bp.route("/banner", methods=["GET"])
def getBanner():
    pass
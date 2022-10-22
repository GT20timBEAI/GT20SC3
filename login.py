from flask import Blueprint

login_bp = Blueprint("login", __name__, url_prefix="/login")

# untuk request cek di scr
@login_bp.route("", methods=["POST"])
def login():
    pass
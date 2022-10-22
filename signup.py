from flask import Blueprint

signup_bp = Blueprint("signup", __name__, url_prefix="/sign-up")

# untuk request cek di scr
@signup_bp.route("", methods=["POST"])
def signup():
    pass
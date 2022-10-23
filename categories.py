from flask import Blueprint


categories_bp = Blueprint("categories", __name__, url_prefix="/categories")


@categories_bp.route("", methods=["GET"])
def getCategories():
    pass

@categories_bp.route("", methods=["POST"])
def createCategories():
    pass

@categories_bp.route("/{category_id}", methods=["GET"])
def updateCategories():
    pass

@categories_bp.route("/{category_id}", methods=["DELETE"])
def deleteCategories():
    pass
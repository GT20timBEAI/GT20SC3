from flask import Blueprint, request
from utils import run_query, validUser


categories_bp = Blueprint("categories", __name__, url_prefix="/categories")


@categories_bp.route("", methods=["GET"])
def getCategories():
    pass


@categories_bp.route("", methods=["POST"])
def createCategories():
    try:
        jwt_token = request.headers.get('token')
        category_name = request.json.get('category_name')

        if not validUser(jwt_token, True):
            return {"error": "user not valid"}, 400

        id = uuid.uuid4()
        run_query("insert into Category(category_id, category_name) \
            values(\"{id}\", \"{category_name}\")")
        return {"message": "Category added"}
    except KeyError:
        return {"message": "error, user already exist"}


@categories_bp.route("/{category_id}", methods=["GET"])
def updateCategories():
    pass


@categories_bp.route("/{category_id}", methods=["DELETE"])
def deleteCategories():
    pass

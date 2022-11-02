from flask import Blueprint, request
from utils import validUser, run_query
import uuid


categories_bp = Blueprint("categories", __name__, url_prefix="/categories")


@categories_bp.route("", methods=["GET"])
def getCategories():
    pass

@categories_bp.route("", methods=["POST"])
def createCategories():
    try:
        jwt_token = request.headers.get('Authentication')
        body = request.json
        category = body['category_name']

        if not validUser(jwt_token, True):
            return {"error": "user not valid"}, 400

        id = uuid.uuid4()
        run_query(f"insert into Category(category_id, category_name) \
            values(\"{id}\", \"{category}\")", True)
        return {"message": "Category added"}, 200
    except KeyError:
        return {"message": "error, user already exist"}, 200

@categories_bp.route("/{category_id}", methods=["GET"])
def updateCategories():
    pass

@categories_bp.route("/{category_id}", methods=["DELETE"])
def deleteCategories():
    pass
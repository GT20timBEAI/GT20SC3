from flask import Blueprint, request
from utils import run_query, validUser
import uuid


categories_bp = Blueprint("categories", __name__, url_prefix="/categories")


@categories_bp.route("", methods=["GET"])
def getCategories():
    try:
        jwt_token = request.headers.get('Authentication')

        if not validUser(jwt_token, True):
            return {"error": "user not valid"}, 400

        get_category = run_query("select * from Category")
        category_data = []
        for i in get_category:
            category_data.append(i)
        return {"data": category_data}, 200
    except KeyError:
        return {"message": "error, user already exist"}


@categories_bp.route("", methods=["POST"])
def createCategories():
    try:
        jwt_token = request.headers.get('Authentication')
        body = request.json
        category = body['category_name']

        if not validUser(jwt_token, True):
            return {"error": "user not valid"}, 400

        id = uuid.uuid4()
        run_query("insert into Category(category_id, category_name) \
            values(\"{id}\", \"{category_name}\"), True")
        return {"message": "Category added"}, 200
    except KeyError:
        return {"message": "error, user already exist"}


@categories_bp.route("/{category_id}", methods=["PUT"])
def updateCategories():
    pass


@categories_bp.route("/{category_id}", methods=["DELETE"])
def deleteCategories():
    pass

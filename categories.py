from flask import Blueprint, request
from utils import run_query, validUser, isCategoryIdExist
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


@categories_bp.route("/<string:urlPath>", methods=["PUT"])
def updateCategories(urlPath):
    jwt_token = request.headers.get('Authentication')
    body = request.json
    category_id = body['category_id']
    category_name = body['category_name']

    if not validUser(jwt_token, True):
        return {"error": "user not valid"}, 400

    if not isCategoryIdExist(urlPath):
        return {"error": "category not found"}, 400

    run_query(f"update Category set category_id=\"{category_id}\", category_name=\"{category_name}\"\
        where category_id = \"{urlPath}\"", True)

    return {"message": "category added"}, 200


@categories_bp.route("/<string:urlPath>", methods=["DELETE"])
def deleteCategories(urlPath):
    jwt_token = request.headers.get('Authentication')
    if not validUser(jwt_token, True):
        return {"error": "user not valid"}, 400

    if not isCategoryIdExist(urlPath):
        return {"error": "category not found"}, 400

    run_query(f"delete from Category where category_id = \"{urlPath}\"", True)

    return {"message": "Category deleted"}, 200

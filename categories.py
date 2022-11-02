from flask import Blueprint, request
from utils import validUser, run_query, checkIdCategory
import uuid

categories_bp = Blueprint("categories", __name__, url_prefix="/categories")


@categories_bp.route("", methods=["GET"])
def getCategories():
    try:
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

        #FIXME: category_id dont know
        id = uuid.uuid4()
        run_query(f"insert into Category(category_id, category_name) \
            values(\"{id}\", \"{category}\")", True)
        return {"message": "Category added"}, 200
    except KeyError:
        return {"message": "error, user already exist"}, 200

@categories_bp.route("/<string:urlPath>", methods=["PUT"])
def updateCategories(urlPath):
    jwt_token = request.headers.get('Authentication')
    body = request.json
    category_idBody = body["category_id"]
    category_name = body["category_name"]
    if not validUser(jwt_token, True):
        return {"error": "user not valid"}, 400


    #TODO: check category in table category
    if not checkIdCategory(urlPath): return {"error" : "category id not found"}, 400

    #TODO: update category_id on table category
    run_query(f"update Category set category_id=\"{category_idBody}\",\
                category_name=\"{category_name}\" \
                where category_id=\"{urlPath}\"", True)
    return {"message": "Category updated"}, 200
    


@categories_bp.route("/<string:category_id>", methods=["DELETE"])
def deleteCategories(category_id):
    jwt_token = request.headers.get('Authentication')
    if not validUser(jwt_token, True):
            return {"error": "user not valid"}, 400
    #TODO: check category in table category
    if not checkIdCategory(category_id): 
        return {"error" : "category id not found"}, 400
    
    run_query("delete from Category where category_id=\"{category_id}\"", True)
    return {"message":"Category deleted"}, 200

        
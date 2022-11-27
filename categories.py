from flask import Blueprint, request
from utils import validUser, run_query, checkCategoryName
import uuid
import json

categories_bp = Blueprint("categories", __name__, url_prefix="/categories")


@categories_bp.route("", methods=["GET"])
def getCategories():
    try:
        get_category = run_query("select * from \"Category\"")
        category_data = []
        for i in get_category:
            dict = {}
            dict["id"] = i["category_id"]
            dict["title"] = i["category_name"]
            category_data.append(dict)
        return {"data": category_data}, 200
    except KeyError:
        return {"message": "error, user already exist"}

# DONE WITH FRONT END
@categories_bp.route("", methods=["POST"])
def createCategories():
    # try:
    jwt_token = request.headers.get('Authentication')
    body = request.get_data()
    body = body.decode('utf-8')
    body = json.loads(body)

    category = body['category_name']

    if not validUser(jwt_token, True):
        return {"error": "user not valid"}, 400

    if checkCategoryName(category):
        return {"message" : "Category Name already exist"}, 400

    #FIXME: category_id dont know
    id = uuid.uuid4()
    run_query(f"insert into \"Category\"(category_id, category_name) \
        values(\'{id}\', \'{category}\')", True)
    return {"message": "Category added"}, 200
    # except:
    #     return {"message": "error, user already exist"}, 200


# DONE WITH FRONT END
@categories_bp.route("/<string:urlPath>", methods=["PUT"])
def updateCategories(urlPath):
    jwt_token = request.headers.get('Authentication')
    body = request.get_data()
    body = body.decode('utf-8')
    body = json.loads(body)

    category_name = body["category_name"]

    if not validUser(jwt_token, True):
        return {"error": "user not valid"}, 400


    #TODO: update category_id on table category
    run_query(f"""
        UPDATE "Category"
        SET category_name = '{category_name}'
        WHERE category_id like '{urlPath}%'
        """, True)
    return {"message": "Category updated"}, 200
    

# DONE with front end
@categories_bp.route("/<string:category_id>", methods=["DELETE"])
def deleteCategories(category_id):

    jwt_token = request.headers.get('Authentication')
    if not validUser(jwt_token, True):
            return {"error": "user not valid"}, 400
    
    # Delete Product where same Category
    run_query(f"""
    delete from \"Product_list\" where category_id like \'{category_id}%\'
    """, True)
    run_query(f"delete from \"Category\" where category_id like \'{category_id}%\'", True)
    return {"message":"Category deleted"}, 200

        
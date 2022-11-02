"""
QUERY PARAMS EXAMPLE

[Key]           [Example]
page            1
page_size       100
sort_by         Price a_z, Price z_a
category        Id category a, id category b
price           0,10000
condition       used
product_name    name


[CREATE PRODUCTS]
Requirements (from the earliest to check):
==> name
    - if product name is not given:
        - return {"error": "Please fill in the product name"}
        - status code: 400
==> description
    - if description is not given:
        - return {"error": "Please fill in the description"}
        - status code: 400
==> condition [new, second]
    - if condition is not given:
        - return {"error": "Please fill in the condition"}
        - status code: 400
    # Maybe use this
    - if condition not in list table
        - return {"error" : "condiiton not in the list"}
==> images [image1, image2, image3]
    - if images is not given:
        - return {"error": "Please fill in the images"}
        - status code: 400
==> category [A, B, C]
    - if category is not given:
        - return {"error": "Please fill in the category"}
        - status code: 400
    - if category_id not in category
        - return {"error" : "category not found"}
        - status code : 401
==> Price
    - If price is not a positive number:
        - return {"error": "Please specify a positive amount"}
        - status code: 400
    - If price not integer
        - return {"error" : "price must be integer"}
        - status code : 400
- if user not found
    - return {"error" : "user not found"}
    - status code : 401
- if user not admin
    - return {"error" : "user not admin"}
    - status code : 401
- Else, everything is valid:
    - return {"message": "Product added"}
    - status code: 201

[UPdate PRODUCTS]
Requirements (from the earliest to check):
==> name
    - if product name is not given:
        - return {"error": "Please fill in the product name"}
        - status code: 400
==> description
    - if product description is not given:
        - return {"error": "Please fill in the product description"}
        - status code: 400
==> images
    - if product description is not given:
        - return {"error": "Please fill in the product images"}
        - status code: 400
==> condition [new, second]
    - if product description is not given:
        - return {"error": "Please fill in the product condition"}
        - status code: 400
    # Maybe use this
    - if condition not in list table
        - return {"error" : "condiiton not in the list"}
==> category
    - if product description is not given:
        - return {"error": "Please fill in the product description"}
        - status code: 400
    - if category_id not in category
        - return {"error" : "category not found"}
        - status code : 401
==> price
    - if product price is not given:
        - return {"error": "Please fill in the product price"}
        - status code: 400
    - If price not integer
        - return {"error" : "price must be integer"}
        - status code : 400
==> product_id
    - if product product_id is not given:
        - return {"error": "Please fill in the product product_id"}
        - status code: 400
    - if product_id not found in table
        - return {"error" : "product not found"}
        - status code : 401
- if user not found
    - return {"error" : "user not found"}
    - status code : 401
- if user not admin
    - return {"error" : "user not admin"}
    - status code : 401
- if everything oke
    - return {"message" : "Product updated"}
    - status code : 200

"""





from flask import Blueprint


products_bp = Blueprint("products", __name__, url_prefix="/products")

# untuk request cek di scr
@products_bp.route("", methods=["GET"])
def productlist():
    pass

@products_bp.route("/search_image", methods=["POST"])
def searchimage():
    pass

@products_bp.route("/{id}", methods=["GET"])
def productDetailPage():
    pass

@products_bp.route("", methods=["POST"])
def createProduct():
    pass

@products_bp.route("/{category_id}", methods=["PUT"])
def UpdateProducts():
    pass


#delete products softs
@products_bp.route("", methods=["DELETE"])
def DeleteProducts():
    pass
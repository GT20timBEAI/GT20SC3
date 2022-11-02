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

[Create Product]
- URL: /products
- method: POST

Requirements (from the earliest to check):
- if product name is not given:
    - return {"error": "Please fill in the product name"}
    - status code: 400
- if condition is not given:
    - return {"error": "Please fill in the condition"}
    - status code: 400
- if category is not given:
    - return {"error": "Please fill in the category"}
    - status code: 400
- If price is not a positive number:
    - return {"error": "Please specify a positive amount"}
    - status code: 400
- Else, everything is valid:
    - return {"message": "Product added"}
    - status code: 201

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

@products_bp.route("/{id}", methods=["POST"])
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
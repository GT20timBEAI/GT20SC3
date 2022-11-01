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


- URL: /seller/stock
- method: POST
- Request body:
    - item: string (required) -> name of this item
    - amount: integer (required) -> how many items to stock
    - price: integer (required) -> unit price (price per individual item)
- Headers:
    - token: string (required) -> token obtained from login to identify this seller

Requirements (from the earliest to check):
- If amount is not a positive number:
    - return {"error": "Please specify a positive amount"}
    - status code: 400
- If price is is not a positive number:
    - return {"error": "Please specify a positive amount"}
    - status code: 400
- If token does not identify a seller:
    - return {"error": "Unauthorized seller"}
    - status code: 403
- If the same item (name) has been previously stocked:
    - return {"error": "Item with the same name already exists"}
    - status code: 400
- Else, everything is valid:
    - Add <amount> of this item to the stock
    - return {"message": "Stocking successful"}
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
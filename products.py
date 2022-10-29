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
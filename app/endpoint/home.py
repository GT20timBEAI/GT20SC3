
from flask import Blueprint
from app.helper.utils import run_query

home_bp = Blueprint("home", __name__, url_prefix="/home")


@home_bp.route("/banner", methods=["GET"])
def getBanner():
    banner = run_query("""
    SELECT id, product_name FROM "Product_list"
    """)
    list_banner = []
    loop = 0
    for i in banner:
        if loop <= 3 and len(banner) > loop:
            dict = {}
            image = run_query(f"""
            SELECT image_url FROM "Image"
            WHERE product_id = '{i['id']}'
            """)
            if len(image) == 0:
                image = '/image/dummy.png'
            else:
                image = image[0]['image_url']
            # image = list_image[loop]
            dict['id'] = i['id']
            dict['image'] = image
            dict['title'] = i['product_name']
            list_banner.append(dict)
            loop += 1

    return {"data": list_banner}

@home_bp.route("/category", methods=["GET"])
def getCategory():
    data = run_query("""
    select category_id, category_name from \"Category\"
    """)

    list = []
    for i in data:
        dict = {}
        id = i["category_id"]

        # FIXME: if product not have what must i do
        idProduct = run_query(f"""
        SELECT id from "Product_list"
        WHERE category_id = '{id}'
        LIMIT 1
        """)
        if len(idProduct) == 0:
            image = '/image/dummy.png'
        else:
            idProduct = idProduct[0]['id']

        image = run_query(f"""
        SELECT image_url from "Image"
        WHERE product_id = '{idProduct}'
        """)
        if len(image) == 0:
            image = '/image/dummy.png'
        else:
            image = image[0]['image_url']

        dict["id"] = i["category_id"]
        dict["title"] = i["category_name"]
        dict["image"] = image
        list.append(dict)

    return {"data": list}, 200

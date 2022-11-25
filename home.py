"""
- response get banner
        {
            "data": [
            {
                "id": "uuid",
                "image": "/banner/image.png",
                "title": "lorem ipsum blablabla"
            }
            ]
        }

- response home/category
    {
    "data": [
   	     {
   		 "id": "uuid",
   		 "image": "/something/image.png",
   		 "title": "Category A"
   	     }
            ]
    }

"""


from flask import Blueprint
from utils import run_query

home_bp = Blueprint("home", __name__, url_prefix="/home")


@home_bp.route("/banner", methods=["GET"])
def getBanner():
    banner = run_query("select id, image, title from Banner")
    list_banner = []
    for i in banner:
        list_banner.append(i)
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
        """)[0]['id']
        image = run_query(f"""
        SELECT image_url from "Image"
        WHERE product_id = '{idProduct}'
        """)[0]['image_url']


        dict["id"] = i["category_id"]
        dict["title"] = i["category_name"]
        dict["image"] = image
        list.append(dict)

    return {"data": list}, 200

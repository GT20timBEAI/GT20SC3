from services.utils import run_query

# get product list for get user order
def productListUserOrder(product):
    product_list = []
    for s in product:
        price = 0
        data_product = run_query(f"""
        SELECT product_name, price FROM "Product_list"
        WHERE id = '{s['item_id']}'
        """)
        name = data_product[0]['product_name']
        price = int(data_product[0]['price'])

        image = run_query(f"""
        SELECT image_url FROM "Image"
        WHERE product_id = '{s['item_id']}'
        """)
        
        if len(image) == 0:
            image = '/image/dummy.png'
        else:
            image = image[0]['image_url']

        dict = {
            "id": s['item_id'],
            "details": {
                "quantity": s['quantity'],
                "size": s['size']
            },
            "price": price,
            "image": image,
            "name": name
            }
        product_list.append(dict)

    data = {
        "products": product_list,
        "shipping_method": product[0]['shipping_method']
    }

    return data
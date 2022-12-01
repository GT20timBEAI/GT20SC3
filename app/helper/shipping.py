from app.helper.utils import run_query

# check havecart
def checkCartUser(id):
    countShippingPrice = 0
    data = run_query(f"""
    SELECT item_id FROM "Cart"
    WHERE user_id = '{id}' and status = 'cart'
    """)
    if len(data) == 0:
        return False
    else:
        for i in data:
            price = run_query(f"""
            SELECT price FROM "Product_list"
            WHERE id = '{i['item_id']}'
            """)[0]['price']
            countShippingPrice += price
    
    print(countShippingPrice)
    #initiate reguler
    if countShippingPrice < 200:
        reguler = countShippingPrice / 100 * 15
    else:
        reguler = countShippingPrice / 100 * 20

    #initiate sameday
    if countShippingPrice < 300:
        sameday = countShippingPrice / 100 * 20
    else:
        sameday = countShippingPrice / 100 * 25
    
    data = [
        {"name" : "regular",
        "price" : int(reguler)
        },
        {"name" : "next day",
        "price" : int(sameday)
        }
    ]
    return data


# GET total price from cart
def totalPrice(id):
    item = run_query(f"""
    SELECT item_id, quantity FROM "Cart"
    WHERE user_id = '{id}' and status = 'cart'
    """)
    countPrice = 0
    for i in item:
        price = 0
        price = run_query(f"""
        SELECT price FROM "Product_list"
        WHERE id = '{i['item_id']}'
        """)[0]['price']
        price = price * i['quantity']
        countPrice += price

    return countPrice
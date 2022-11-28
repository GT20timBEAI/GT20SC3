from service.utils import run_query

def checkCategoryName(category):
    name = run_query("""
    SELECT category_name from "Category"
    """)
    for i in name:
        if category == i['category_name']: 
            return True
    return False
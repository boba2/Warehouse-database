from bson import ObjectId

from models.category import Category


def check_if_category_is_empty(client, id: str) -> bool:
    category = client.konrad_borowik.categories.find_one({"_id": ObjectId(id)})
    
    parts = client.konrad_borowik.parts.aggregate([
            {
                '$match': {
                    'category': category['name']
                }
            },
        ])
    
    if len(list(parts)) > 0:
        return False
    return True
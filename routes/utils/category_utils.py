from bson import ObjectId


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


def check_if_child_catogories_are_empty(client, id: str) -> bool:
    category = client.konrad_borowik.categories.find_one({"_id": ObjectId(id)})

    sub_categories = client.konrad_borowik.categories.aggregate([
        {
            '$match': {
                'parent_name': category['name']
            }
        }
    ])
    output = False
    for sc in sub_categories:
        output = check_if_category_is_empty(client, sc['_id'])
    return output
        
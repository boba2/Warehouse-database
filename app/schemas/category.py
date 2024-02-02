from typing import List


def categoryEntity(item) -> dict:
    return {
        'id': str(item['_id']),
        'name': item['name'],
        'parent_name': item['parent_name']
    }


def categoryEntities(entity) -> List:
    return [categoryEntity(item) for item in entity]

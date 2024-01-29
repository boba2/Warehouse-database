from typing import List


def categoryEntity(item) -> dict:
    return {
        'name': item['name'],
        'parent_name': item['parent_name']
    }


def categoriesEntity(entity) -> List:
    return [categoryEntity(item) for item in entity]
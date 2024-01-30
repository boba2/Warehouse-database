from typing import List


def partEntity(item) -> dict:
    return {
        'id': str(item['_id']),
        'serial_number': item['serial_number'],
        'name': item['name'],
        'description': item['description'],
        'category': item['category'],
        'quantity': item['quantity'],
        'price': item['price'],
        'location': item['location']
    }


def partEntities(entity) -> List:
    return [partEntity(item) for item in entity]

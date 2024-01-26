from pymongo import MongoClient
import json


class Database():
    def __init__(self, dummy_categories, dummy_parts) -> None:
        client = MongoClient(
            host='localhost',
            port=27017,
            username='myMongoAdmin',
            password='okon',
        )
        self.db = client['konrad_borowik']
        self.categories = self.db['categories']
        self.parts = self.db['parts']

        self.categories.insert_many(dummy_categories)
        self.parts.insert_many(dummy_parts)

    def insert_category(
            self,
            name: str,
            parent_name: str
    ) -> None:
        self.categories.insert_one(
            {
                'name': name,
                'parent_name': parent_name
            }
        )

    def insert_part(
            self,
            serial_number:str,
            name: str,
            description: str,
            category: str,
            quantity: int,
            price: float,
            location: dict,            
    ) -> None:
        self.parts.insert_one(
            {
                'serial_number': serial_number,
                'name': name,
                'description': description,
                'category': category,
                'quantity': quantity,
                'price': price,
                'location': location
            }
        )

from pymongo import MongoClient


class Database():
    def __init__(self) -> None:
        client = MongoClient('localhost', 27017)
        self.db = client['konrad_borowik']
        self.categories = self.db['categories']
        self.parts = self.db['parts']
        

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


    def create_database(self) -> None:
        self._insert_category('Fasteners')
        
        self._insert_category('Nuts')
        self._insert_category('Bolts')

        starter_parts = ['Hex', 'Flange', 'Cap', 'Nylon', 'Wood', 'Socket']
        



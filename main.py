import json
from typing import List

from mongodb_setup import Database


def read_file(filename: str) -> List:
    with open(f'data/{filename}') as f:
        data = json.load(f)
    f.close()
    return data
    

def main():
    dummy_categories = read_file('dummy_categories.json')
    dummy_parts = read_file('dummy_parts.json')
    database = Database(dummy_categories, dummy_parts)


if __name__ == '__main__':
    main()

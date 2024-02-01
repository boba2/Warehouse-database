import yaml


def parse_key(key: str) -> str:
    location_keys = ['warehouse', 'room', 'bookcase', 'shelf', 'cuvette', 'column', 'row']
    return 'location.' + key if key in location_keys else key


def parse_value(value: str) -> str | int | float:
    return yaml.safe_load(value)
    
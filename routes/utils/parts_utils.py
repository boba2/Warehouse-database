def parse_input(key: str, value: str | int) -> dict:
    int_fields = ['quantity', 'room', 'bookcase', 'shelf', 'cuvette', 'column', 'row']
    float_fields = ['price']
    if key.replace('location.', '') in int_fields:
        value = int(value)
    elif key in float_fields:
        value = float(value)

    return {key: value}
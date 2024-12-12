def transform_data(data):
    """Transforms the data by converting all text to uppercase."""
    return [[item.upper() for item in row] for row in data]

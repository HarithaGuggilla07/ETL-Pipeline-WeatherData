import csv

def extract_data(file_path):
    """Extracts data from the given CSV file."""
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        data = [row for row in reader]
    return data

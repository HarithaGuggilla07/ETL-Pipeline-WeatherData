def load_data(data, output_file):
    """Loads transformed data into a specified output file."""
    with open(output_file, 'w') as file:
        for row in data:
            file.write(','.join(row) + '\n')

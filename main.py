from scripts.extract import extract_data
from scripts.transform import transform_data
from scripts.load import load_data

# Define file paths
input_file = 'data/sample_data.csv'
output_file = 'data/transformed_data.csv'

# Extract data
print("Extracting data...")
data = extract_data(input_file)
print(f"Extracted {len(data)} rows.")

# Transform data
print("Transforming data...")
transformed_data = transform_data(data)
print(f"Transformed data: {len(transformed_data)} rows.")

# Load data
print("Loading data...")
load_data(transformed_data, output_file)
print(f"Data loaded into {output_file}")

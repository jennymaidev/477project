import requests
import pandas as pd
import os

# Define constants
DATA_DIR = '../data/raw/'
filename = 'sales_data.csv'
url = 'https://datacatalog.cookcountyil.gov/resource/wvhk-k5uv.csv?$limit=3000000'
full_filepath = os.path.join(DATA_DIR, filename)

# Download the dataset
response = requests.get(url, stream=True)
response.raise_for_status()

# Save the dataset to a CSV file
with open(full_filepath, 'wb') as file:
    for chunk in response.iter_content(chunk_size=8192):
        file.write(chunk)
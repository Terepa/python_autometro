from datetime import datetime, timedelta
import requests
import pandas as pd
from concurrent.futures import ThreadPoolExecutor
import sys
import time

# Function to check if product exists in Magento
def check_product_existence(itemcode, token):
    magento_url = f"https://autometroclient.indvp.com/rest/V1/products/{itemcode}"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
    }

    response = requests.get(magento_url, headers=headers)

    if response.status_code == 200:
        return "exists"
    elif response.status_code == 404:
        return "not found"
    else:
        return "error"

# Function to check master product existence in Magento
def check_master_product_existence(itemcode, token):
    modified_itemcode = "MAS" + itemcode[3:]  # Remove first 3 symbols and add "MAS"
    return check_product_existence(modified_itemcode, token)

# Function to check if product exists in carlist
def check_carlist_product_existence(modified_itemcode, api_key):
    carlist_url = f"https://dati.autometro.lv/parts/{modified_itemcode}/json"
    headers = {
        "accept": "application/json",
        "x-api-key": api_key,
    }

    response = requests.get(carlist_url, headers=headers)

    if response.status_code == 200:
        return "exists"
    elif response.status_code == 404:
        return "not found"
    else:
        return "error"

# Function to process a single row
def process_row(row, total_rows, start_time):
    itemcode = row.itemcode  # Use attribute-style access

    # Process simple_product
    row_dict = row._asdict()
    row_dict["simple_product"] = check_product_existence(itemcode, magento_token)

    # Process master_product
    modified_itemcode = "MAS" + itemcode[3:]
    row_dict["master_product"] = check_master_product_existence(itemcode, magento_token)

    # Process carlist_product
    row_dict["carlist_product"] = check_carlist_product_existence(modified_itemcode, carlist_api_key)

    # Print progress
    current_time = time.time()
    elapsed_time = current_time - start_time
    progress_percentage = row.Index / total_rows

    if progress_percentage > 0:
        average_time_per_row = elapsed_time / progress_percentage
        estimated_time_remaining = average_time_per_row * (1 - progress_percentage)
    else:
        estimated_time_remaining = 0

    sys.stdout.write("\r")
    sys.stdout.write(f"Processing: {progress_percentage:.2%} | Elapsed Time: {timedelta(seconds=elapsed_time)} | Estimated Time Remaining: {timedelta(seconds=estimated_time_remaining)}")
    sys.stdout.flush()

    return pd.Series(row_dict, index=row._fields)

# Load CSV file
df = pd.read_csv("./output/moneo_daily.csv")

# Drop the 'sernr' column if it exists
df = df.drop(columns=["sernr"], errors="ignore")

# Add new columns for status
df["simple_product"] = ""
df["master_product"] = ""
df["carlist_product"] = ""

# Define the tokens
magento_token = "lqtmon07mm77b31eee42n4vuu11t5ydi"
carlist_api_key = "22F788B8-5CA8-46F9-9023-BAF1CD12D555"

# Process rows concurrently
total_rows = len(df)
start_time = time.time()  # Record start time

with ThreadPoolExecutor(max_workers=30) as executor:  # Use None for auto-detecting the number of available CPUs
    processed_rows = list(executor.map(lambda row: process_row(row, total_rows, start_time), df.itertuples(index=True)))

# Update the DataFrame with processed rows
df = pd.DataFrame(processed_rows)

# Generate filename with current date and time
current_datetime = datetime.now().strftime("%Y%m%d_%H%M%S")
filename = f"./output/checked_SKU_{current_datetime}.csv"
df.to_csv(filename, index=False)

# Calculate elapsed time
elapsed_time = time.time() - start_time

# Display final progress
sys.stdout.write("\r")
sys.stdout.write(f"\nProcessing completed in {timedelta(seconds=elapsed_time)}\n")
sys.stdout.flush()

print("\nUpdated data saved to output_with_status.csv")

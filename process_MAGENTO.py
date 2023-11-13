import requests
import pandas as pd
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm

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
def process_row(row):
    itemcode = row["itemcode"]

    # Process simple_product
    row["simple_product"] = check_product_existence(itemcode, magento_token)

    # Process master_product
    modified_itemcode = "MAS" + itemcode[3:]
    row["master_product"] = check_master_product_existence(itemcode, magento_token)

    # Process carlist_product
    row["carlist_product"] = check_carlist_product_existence(modified_itemcode, carlist_api_key)

    return row

# Load CSV file
df = pd.read_csv("output.csv")

# Drop the 'sernr' column if it exists
df = df.drop(columns=["sernr"], errors="ignore")

# Add new columns for status
df["simple_product"] = ""
df["master_product"] = ""
df["carlist_product"] = ""

# Define the tokens
magento_token = "lqtmon07mm77b31eee42n4vuu11t5ydi"
carlist_api_key = "22F788B8-5CA8-46F9-9023-BAF1CD12D555"

# Add a visual scrollbar using tqdm
with tqdm(total=len(df), desc="Processing", unit="itemcode") as pbar:
    with ThreadPoolExecutor(max_workers=5) as executor:
        # Submit tasks
        futures = [executor.submit(process_row, row) for _, row in df.iterrows()]

        # Process completed tasks
        for future in as_completed(futures):
            pbar.update(1)  # Update the progress bar
            try:
                # Get the result from the completed task
                row = future.result()
                df.iloc[row.name] = row
            except Exception as e:
                print(f"Error processing row: {e}")

# Save the updated DataFrame to CSV file without the 'sernr' column
df.to_csv("output_with_status.csv", index=False)

print("Updated data saved to output_with_status.csv")

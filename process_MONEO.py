import requests
import pandas as pd
from requests.packages.urllib3.exceptions import InsecureRequestWarning

# Suppress only the InsecureRequestWarning, not all warnings
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

url = "https://176.31.239.70:8003/api/v2/stock.batchinfo"
headers = {
    "Authorization": "pPcMYQ0060ufA7DFlHUyfw",
    "Content-Type": "application/json",
}

data = {
    "fieldlist": ["itemcode", "itemname", "instock", "originaltransdate"],
    "request": {
        "compuid": "db73d96f-29b37c7d-5d60ae8a-78a6305c-7edf3e9b"
    }
}

# Send POST request with SSL verification disabled
response = requests.post(url, json=data, headers=headers, verify=False)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    try:
        # Parse JSON response
        result = response.json()["result"]["records"]

        # Convert the result to a DataFrame
        df = pd.DataFrame(result)

        # Convert 'instock' column to numeric
        df['instock'] = pd.to_numeric(df['instock'], errors='coerce')

        # Drop rows where 'instock' is less than or equal to 0
        df = df[df['instock'] > 0]

        # Exclude rows where 'itemcode' starts with "ORD"
        df = df[~df['itemcode'].str.startswith("ORD")]

        # Drop duplicate rows based on 'itemcode'
        df.drop_duplicates(subset='itemcode', keep='first', inplace=True)

        # Save DataFrame to CSV file
        df.to_csv("./output/moneo_daily.csv", index=False)

        print("Data saved to ./output/moneo_daily.csv")
    except Exception as e:
        print(f"Error processing response: {e}")
else:
    print(f"Error: {response.status_code}, {response.text}")

import os
import glob
import pandas as pd
from datetime import datetime


###  -----------------------------   AUTOMETRO_LV -----------------------   ###

# Find the latest file that starts with "checked_SKU_"
files = glob.glob("./output/autometro_LV_simple_*.csv")

if files:
    latest_file = max(files, key=os.path.getctime)
    # Rest of your code...
else:
    print("No files matching the pattern found.")

# Load CSV data
df = pd.read_csv(latest_file)

# Remove SKUs starting with 'MOP', 'VMO', or 'OEM'
df = df[~df['SKU'].str.startswith(('MOP', 'VMO', 'OEM'))]

# Remove first three characters from the SKU column and add 'XXX' to the beginning
df['SKU'] = 'XXX' + df['SKU'].str[3:]

# Filter the data for SKUs with QTY > 0
greater_than_zero = df[df['QTY'] > 0]

# Group by SKU and get the lowest cost for each SKU where QTY > 0
summary_gt_zero = greater_than_zero.groupby('SKU').agg({'QTY': 'sum', 'Cost': 'min'})

# Concatenate summaries
summary = pd.concat([summary_gt_zero])

# Generate filename with current date and time
current_datetime = datetime.now().strftime("%Y%m%d_%H%M%S")
filename = f"./output/autometro_LV_xxx_{current_datetime}.csv"
summary.to_csv(filename, index_label='SKU')


###  -----------------------------   AUTOMETRO_UK -----------------------   ###

# Find the latest file that starts with "checked_SKU_"
files = glob.glob("./output/autometro_UK_simple*.csv")

if files:
    latest_file = max(files, key=os.path.getctime)
    # Rest of your code...
else:
    print("No files matching the pattern found.")

# Load CSV data
df = pd.read_csv(latest_file)

df = df[~df['SKU'].str.startswith(('MOP', 'VMO', 'OEM'))]

df['SKU'] = 'XXX' + df['SKU'].str[3:]

greater_than_zero = df[df['QTY'] > 0]

summary_gt_zero = greater_than_zero.groupby('SKU').agg({'QTY': 'sum', 'Cost': 'min'})

summary = pd.concat([summary_gt_zero])


# Generate filename with current date and time
current_datetime = datetime.now().strftime("%Y%m%d_%H%M%S")
filename = f"./output/autometro_UK_xxx_{current_datetime}.csv"
summary.to_csv(filename, index_label='SKU')

###  -----------------------------   AUTOMETRO_IT -----------------------   ###


# Find the latest file that starts with "checked_SKU_"
files = glob.glob("./output/autometro_IT_simple*.csv")

if files:
    latest_file = max(files, key=os.path.getctime)
    # Rest of your code...
else:
    print("No files matching the pattern found.")

# Load CSV data
df = pd.read_csv(latest_file)

df = df[~df['SKU'].str.startswith(('MOP', 'VMO', 'OEM'))]

df['SKU'] = 'XXX' + df['SKU'].str[3:]

greater_than_zero = df[df['QTY'] > 0]

summary_gt_zero = greater_than_zero.groupby('SKU').agg({'QTY': 'sum', 'Cost': 'min'})

summary = pd.concat([summary_gt_zero])


# Generate filename with current date and time
current_datetime = datetime.now().strftime("%Y%m%d_%H%M%S")
filename = f"./output/autometro_IT_xxx_{current_datetime}.csv"
summary.to_csv(filename, index_label='SKU')

###  -----------------------------   AUTOMETRO_DE -----------------------   ###

# Find the latest file that starts with "checked_SKU_"
files = glob.glob("./output/autometro_DE_simple*.csv")

if files:
    latest_file = max(files, key=os.path.getctime)
    # Rest of your code...
else:
    print("No files matching the pattern found.")

# Load CSV data
df = pd.read_csv(latest_file)

df = df[~df['SKU'].str.startswith(('MOP', 'VMO', 'OEM'))]

df['SKU'] = 'XXX' + df['SKU'].str[3:]

greater_than_zero = df[df['QTY'] > 0]

summary_gt_zero = greater_than_zero.groupby('SKU').agg({'QTY': 'sum', 'Cost': 'min'})

summary = pd.concat([summary_gt_zero])


# Generate filename with current date and time
current_datetime = datetime.now().strftime("%Y%m%d_%H%M%S")
filename = f"./output/autometro_DE_xxx_{current_datetime}.csv"
summary.to_csv(filename, index_label='SKU')
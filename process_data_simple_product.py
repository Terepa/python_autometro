from datetime import datetime
import pandas as pd


# Read the CSV file into a Pandas DataFrame
df = pd.read_csv("upload/autometro_LV.csv")

# Sum the 'Krasta QTY' and 'Remte QTY' columns into a new 'QTY' column
df['QTY'] = df['Krasta QTY'] + df['Remte QTY']

# Filter the data for SKUs with QTY > 0
greater_than_zero = df[df['QTY'] > 0]

# Create a mask for SKUs with QTY > 0
sku_mask_gt_zero = greater_than_zero['SKU \ QTY']

# Group by SKU and get the lowest cost for each SKU where QTY > 0
summary_gt_zero = greater_than_zero.groupby('SKU \ QTY').agg({'QTY': 'sum', 'Cost': 'min'})

# Filter the data for SKUs with QTY <= 0 and not in the QTY > 0 list
less_than_or_equal_to_zero = df[(df['QTY'] <= 0) & ~df['SKU \ QTY'].isin(sku_mask_gt_zero)]

# Group by SKU and get the lowest cost for each SKU where QTY <= 0
summary_lte_zero = less_than_or_equal_to_zero.groupby('SKU \ QTY').agg({'QTY': 'sum', 'Cost': 'min'})

# Concatenate the two summaries
summary = pd.concat([summary_gt_zero, summary_lte_zero])

# Generate filename with current date and time
current_datetime = datetime.now().strftime("%Y%m%d_%H%M%S")
filename = f"./output/autometro_LV_simple_{current_datetime}.csv"
summary.to_csv(filename, index_label='SKU')




####  -----------------------------   AUTOMETRO_UK -----------------------   ###


df = pd.read_csv("upload/autometro_UK.csv")

# Create a mask for SKUs with QTY > 0
sku_mask_gt_zero = greater_than_zero['SKU \ QTY']

# Group by SKU and get the lowest cost for each SKU where QTY > 0
summary_gt_zero = greater_than_zero.groupby('SKU \ QTY').agg({'QTY': 'sum', 'Cost': 'min'})

# Filter the data for SKUs with QTY <= 0 and not in the QTY > 0 list
less_than_or_equal_to_zero = df[(df['QTY'] <= 0) & ~df['SKU \ QTY'].isin(sku_mask_gt_zero)]

summary_lte_zero = less_than_or_equal_to_zero.groupby('SKU \ QTY').agg({'QTY': 'sum', 'Cost': 'min'})

summary = pd.concat([summary_gt_zero, summary_lte_zero])

# Generate filename with current date and time
current_datetime = datetime.now().strftime("%Y%m%d_%H%M%S")
filename = f"./output/autometro_UK_simple_{current_datetime}.csv"
summary.to_csv(filename, index_label='SKU')



###  -----------------------------   AUTOMETRO_IT -----------------------   ###

df = pd.read_csv("upload/autometro_IT.csv")

# Create a mask for SKUs with QTY > 0
sku_mask_gt_zero = greater_than_zero['SKU \ QTY']

# Group by SKU and get the lowest cost for each SKU where QTY > 0
summary_gt_zero = greater_than_zero.groupby('SKU \ QTY').agg({'QTY': 'sum', 'Cost': 'min'})


# Filter the data for SKUs with QTY <= 0 and not in the QTY > 0 list
less_than_or_equal_to_zero = df[(df['QTY'] <= 0) & ~df['SKU \ QTY'].isin(sku_mask_gt_zero)]

summary_lte_zero = less_than_or_equal_to_zero.groupby('SKU \ QTY').agg({'QTY': 'sum', 'Cost': 'min'})

summary = pd.concat([summary_gt_zero, summary_lte_zero])

# Generate filename with current date and time
current_datetime = datetime.now().strftime("%Y%m%d_%H%M%S")
filename = f"./output/autometro_IT_simple_{current_datetime}.csv"
summary.to_csv(filename, index_label='SKU')



###  -----------------------------   AUTOMETRO_DE -----------------------   ###

df = pd.read_csv("upload/autometro_DE.csv")

# Create a mask for SKUs with QTY > 0
sku_mask_gt_zero = greater_than_zero['SKU \ QTY']

# Group by SKU and get the lowest cost for each SKU where QTY > 0
summary_gt_zero = greater_than_zero.groupby('SKU \ QTY').agg({'QTY': 'sum', 'Cost': 'min'})

# Filter the data for SKUs with QTY <= 0 and not in the QTY > 0 list
less_than_or_equal_to_zero = df[(df['QTY'] <= 0) & ~df['SKU \ QTY'].isin(sku_mask_gt_zero)]

summary_lte_zero = less_than_or_equal_to_zero.groupby('SKU \ QTY').agg({'QTY': 'sum', 'Cost': 'min'})

summary = pd.concat([summary_gt_zero, summary_lte_zero])

# Generate filename with current date and time
current_datetime = datetime.now().strftime("%Y%m%d_%H%M%S")
filename = f"./output/autometro_DE_simple_{current_datetime}.csv"
summary.to_csv(filename, index_label='SKU')
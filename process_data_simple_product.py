import pandas as pd

###  -----------------------------   AUTOMETRO_LV -----------------------   ###

# Read the CSV file into a Pandas DataFrame
df = pd.read_csv("input_files/autometro_LV.csv")

# Sum the 'Krasta QTY' and 'Remte QTY' columns into a new 'QTY' column
df['QTY'] = df['Krasta QTY'] + df['Remte QTY']


# Filter the data for SKUs with QTY > 0
greater_than_zero = df[df['QTY'] > 0]

# Group by SKU and get the lowest cost for each SKU where QTY > 0
summary_gt_zero = greater_than_zero.groupby('SKU \ QTY').agg({'QTY': 'sum', 'Cost': 'min'})

# Filter the data for SKUs with QTY <= 0
less_than_or_equal_to_zero = df[df['QTY'] <= 0]

# Group by SKU and get the lowest cost for each SKU where QTY <= 0
summary_lte_zero = less_than_or_equal_to_zero.groupby('SKU \ QTY').agg({'QTY': 'sum', 'Cost': 'min'})

# Concatenate the two summaries
summary = pd.concat([summary_gt_zero, summary_lte_zero])

# Export the result to a new CSV file
summary.to_csv('autometro_LV_simple_product.csv', index_label='SKU')


###  -----------------------------   AUTOMETRO_UK -----------------------   ###


df = pd.read_csv("input_files/autometro_UK.csv")

greater_than_zero = df[df['QTY'] > 0]

summary_gt_zero = greater_than_zero.groupby('SKU \ QTY').agg({'QTY': 'sum', 'Cost': 'min'})

less_than_or_equal_to_zero = df[df['QTY'] <= 0]

summary_lte_zero = less_than_or_equal_to_zero.groupby('SKU \ QTY').agg({'QTY': 'sum', 'Cost': 'min'})

summary = pd.concat([summary_gt_zero, summary_lte_zero])

summary.to_csv('autometro_UK_simple_product.csv', index_label='SKU')

###  -----------------------------   AUTOMETRO_IT -----------------------   ###

df = pd.read_csv("input_files/autometro_IT.csv")

greater_than_zero = df[df['QTY'] > 0]

summary_gt_zero = greater_than_zero.groupby('SKU \ QTY').agg({'QTY': 'sum', 'Cost': 'min'})

less_than_or_equal_to_zero = df[df['QTY'] <= 0]

summary_lte_zero = less_than_or_equal_to_zero.groupby('SKU \ QTY').agg({'QTY': 'sum', 'Cost': 'min'})

summary = pd.concat([summary_gt_zero, summary_lte_zero])

summary.to_csv('autometro_IT_simple_product.csv', index_label='SKU')



###  -----------------------------   AUTOMETRO_DE -----------------------   ###

df = pd.read_csv("input_files/autometro_DE.csv")

greater_than_zero = df[df['QTY'] > 0]

summary_gt_zero = greater_than_zero.groupby('SKU \ QTY').agg({'QTY': 'sum', 'Cost': 'min'})

less_than_or_equal_to_zero = df[df['QTY'] <= 0]

summary_lte_zero = less_than_or_equal_to_zero.groupby('SKU \ QTY').agg({'QTY': 'sum', 'Cost': 'min'})

summary = pd.concat([summary_gt_zero, summary_lte_zero])

summary.to_csv('autometro_DE_simple_product.csv', index_label='SKU')
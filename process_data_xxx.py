import pandas as pd
import sys

print(sys.executable)

###  -----------------------------   AUTOMETRO_LV -----------------------   ###

# Read the CSV file into a Pandas DataFrame
df = pd.read_csv("autometro_LV.csv")

# Sum the 'Krasta QTY' and 'Remte QTY' columns into a new 'QTY' column
df['QTY'] = df['Krasta QTY'] + df['Remte QTY']

# Remove SKUs starting with 'MOP', 'VMO', or 'OEM'
df = df[~df['SKU \ QTY'].str.startswith(('MOP', 'VMO', 'OEM'))]

# Remove first three characters from the SKU column and add 'XXX' to the beginning
df['SKU \ QTY'] = 'XXX' + df['SKU \ QTY'].str[3:]

# Filter the data for SKUs with QTY > 0
greater_than_zero = df[df['QTY'] > 0]

# Group by SKU and get the lowest cost for each SKU where QTY > 0
summary_gt_zero = greater_than_zero.groupby('SKU \ QTY').agg({'QTY': 'sum', 'Cost': 'min'})

# Concatenate summaries
summary = pd.concat([summary_gt_zero])

# Export the result to a new CSV file
summary.to_csv('autometro_LV_xxx.csv', index_label='SKU')

# ###  -----------------------------   AUTOMETRO_UK -----------------------   ###
#
# df = pd.read_csv("autometro_UK.csv")
#
# df = df[~df['SKU \ QTY'].str.startswith(('MOP', 'VMO', 'OEM'))]
#
# df['SKU \ QTY'] = df['SKU \ QTY'].str[3:]
#
# greater_than_zero = df[df['QTY'] > 0]
#
# summary_gt_zero = greater_than_zero.groupby('SKU \ QTY').agg({'QTY': 'sum', 'Cost': 'min'})
#
# summary = pd.concat([summary_gt_zero])
#
# summary.to_csv('autometro_UK_xxx.csv', index_label='SKU')
#
# ###  -----------------------------   AUTOMETRO_IT -----------------------   ###
#
# df = pd.read_csv("autometro_IT.csv")
#
# df = df[~df['SKU \ QTY'].str.startswith(('MOP', 'VMO', 'OEM'))]
#
# df['SKU \ QTY'] = df['SKU \ QTY'].str[3:]
#
# greater_than_zero = df[df['QTY'] > 0]
#
# summary_gt_zero = greater_than_zero.groupby('SKU \ QTY').agg({'QTY': 'sum', 'Cost': 'min'})
#
# summary = pd.concat([summary_gt_zero])
#
# summary.to_csv('autometro_IT_xxx.csv', index_label='SKU')
#
# ###  -----------------------------   AUTOMETRO_DE -----------------------   ###
#
#
# df = pd.read_csv("autometro_DE.csv")
#
# df = df[~df['SKU \ QTY'].str.startswith(('MOP', 'VMO', 'OEM'))]
#
# df['SKU \ QTY'] = df['SKU \ QTY'].str[3:]
#
# greater_than_zero = df[df['QTY'] > 0]
#
# summary_gt_zero = greater_than_zero.groupby('SKU \ QTY').agg({'QTY': 'sum', 'Cost': 'min'})
#
# summary = pd.concat([summary_gt_zero])
#
# summary.to_csv('autometro_DE_xxx.csv', index_label='SKU')
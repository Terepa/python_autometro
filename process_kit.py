import pandas as pd

# Read the CSV files based on the SKU prefix
configurable_df = pd.read_csv('configurable_file.csv')
source_df = pd.read_csv('autometro_LV_simple_product.csv')
source_df_xxx = pd.read_csv('autometro_LV_xxx.csv')

# Initialize a dictionary to store the quantities and costs of each part
part_quantities = {}
part_costs = {}

# Iterate through each row in the source dataframe
for index, row in source_df.iterrows():
    part_sku = row['SKU']
    part_quantities[part_sku] = row['QTY']
    part_costs[part_sku] = row['Cost']

# Iterate through each row in the source dataframe with prefix 'XXX'
for index, row in source_df_xxx.iterrows():
    part_sku = row['SKU']
    part_quantities[part_sku] = row['QTY']
    part_costs[part_sku] = row['Cost']

# Initialize a dictionary to store the quantities and costs of each kit_sku
kit_quantities = {}
kit_costs = {}

# Iterate through each row in the configurable dataframe
for index, row in configurable_df.iterrows():
    kit_sku = row['kit_sku']
    kit_quantity = 999999999  # Set a large initial value
    kit_cost = 0
    for i in range(1, 6):
        part_sku = row[f'p{i}']
        if pd.isna(part_sku):
            break
        part_quantity_needed = row[f'p{i}q']
        if part_sku in part_quantities:
            available_quantity = part_quantities[part_sku]
            part_cost = part_costs[part_sku]
            kit_quantity = min(kit_quantity, available_quantity // part_quantity_needed)
            kit_cost += part_cost * part_quantity_needed
        else:
            kit_quantity = 0
            break
    kit_quantities[kit_sku] = kit_quantity
    kit_costs[kit_sku] = round(kit_cost, 2)  # Round the kit cost to two decimal places

# Create a dataframe from the dictionaries
result_df = pd.DataFrame({'kit_sku': list(kit_quantities.keys()), 'QTY': list(kit_quantities.values()), 'Cost': list(kit_costs.values())})

# Export the result to a new CSV file
result_df.to_csv('output_file.csv', index=False)

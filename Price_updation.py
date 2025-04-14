import pandas as pd

# Read product.csv and sales.csv, then merge them
def pricing_rules():
    product_df = pd.read_csv(r'C:\path\product.csv')
    sales_df = pd.read_csv(r'C:\path\sales.csv')

    # Merge both tables on 'sku' column
    merged_df = pd.merge(sales_df, product_df, on='sku')
    print(merged_df.head())  # Optional: print to check the merged data

    # Initialize the 'updated_price' column with the current price
    merged_df['updated_price'] = merged_df['current_price']

    # Rule 1 – Low Stock, High Demand (Increase by 15%)
    mask1 = (merged_df['stock'] < 20) & (merged_df['quantity_sold'] > 30)
    merged_df.loc[mask1, 'updated_price'] = merged_df.loc[mask1, 'current_price'] * 1.15

    # Rule 2 – Dead Stock (Decrease by 30%)
    mask2 = (merged_df['stock'] > 200) & (merged_df['quantity_sold'] == 0)
    merged_df.loc[mask2 & ~mask1, 'updated_price'] = merged_df.loc[mask2 & ~mask1, 'current_price'] * 0.70

    # Rule 3 – Overstocked Inventory (Decrease by 10%)
    mask3 = (merged_df['stock'] > 100) & (merged_df['quantity_sold'] < 20)
    merged_df.loc[mask3 & ~mask1 & ~mask2, 'updated_price'] = merged_df.loc[mask3 & ~mask1 & ~mask2, 'current_price'] * 0.90

    # Rule 4 – Minimum Profit Constraint (Ensure current price is at least 20% above cost price)
    merged_df['updated_price'] = merged_df[['updated_price', 'cost_price']].apply(
        lambda row: max(row['updated_price'], row['cost_price'] * 1.2), axis=1
    )

    # Round up
    merged_df['updated_price'] = merged_df['updated_price'].round(2)

    return merged_df

updated_df = pricing_rules()

output_df = updated_df.rename(columns={
    'current_price': 'old_price',
    'updated_price': 'new_price'
})

# Renamed columns and save csv
output_df[['sku', 'old_price', 'new_price']].to_csv(
    r'C:\path\output.csv', index=False
)



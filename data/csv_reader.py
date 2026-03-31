import pandas as pd

from domain.sale import Sale

def read_sales(filepath):
    df = pd.read_csv(filepath)
    for row in df.itertuples(index=False):
        yield Sale(
            region = row.Region,
            product_category = row.Product_Category,
            discount = float(row.Discount),
            revenue = float(row.Unit_Price) * int(row.Quantity_Sold) * (1 - float(row.Discount)),
            units_sold = int(row.Quantity_Sold),
            sales_rep = row.Sales_Rep
        )
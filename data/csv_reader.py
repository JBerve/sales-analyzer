import csv
from domain.sale import Sale

def read_sales(filepath):
    with open(filepath, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter=';')

        for row in reader:
            sale = Sale(
                region = row["Region"],
                product_category = row["Product_Category"],
                discount = float(row["Discount"]),
                revenue = float(row["Unit_Price"]) * int(row["Quantity_Sold"]) * (1-float(row["Discount"])),
                units_sold = int(row["Quantity_Sold"]),
                sales_rep = row["Sales_Rep"]
            )
            yield sale
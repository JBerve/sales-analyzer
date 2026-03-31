import csv
from domain.sale import Sale

def read_sales(filepath):
    with open(filepath, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)

        for row in reader:
            sale = Sale(
                region=row["region"],
                product_category=row["product_category"],
                discount=float(row["discount"]),
                revenue=float(row["revenue"]),
                units_sold=int(row["units_sold"]),
                sales_rep=row["sales_rep"]
            )
            yield sale
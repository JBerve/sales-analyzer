from dataclasses import dataclass

@dataclass
class Sale:
    region: str
    product_category: str
    discount: float
    revenue: float
    units_sold: int
    sales_rep: str

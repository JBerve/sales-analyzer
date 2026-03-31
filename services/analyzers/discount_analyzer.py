class DiscountAnalyzer:
    
    def __init__(self):
        self.total_discount = 0
        self.sales_count = 0
        self.average_discount = 0
    
    def process(self, sale):
        self.total_discount += sale.discount
        self.sales_count = self.sales_count  + 1

    def results(self):
        if self.sales_count:
            self.average_discount = self.total_discount / self.sales_count
            return {"average_discount": self.average_discount}
        else:
            return {"average_discount": 0}

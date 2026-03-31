class DiscountAnalyzer:
    
    def __init__(self):
        self.total_discount = 0
        self.amount_of_sales = 0
        self.average_discount = 0
    
    def process(self, sale):
        self.total_discount += sale.discount
        self.amount_of_sales = self.amount_of_sales  + 1

    def results(self):
        if self.amount_of_sales:
            self.average_discount = self.total_discount / self.amount_of_sales
            return {"average_discount": self.average_discount}
        else:
            return {"average_discount": 0}

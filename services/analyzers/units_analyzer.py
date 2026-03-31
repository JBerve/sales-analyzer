class UnitsAnalyzer:
    def __init__(self):
        self.total_units_sold = 0

    def process(self, sale):
        self.total_units_sold += sale.units_sold

    def results(self):
        return {"total_units": self.total_units_sold}
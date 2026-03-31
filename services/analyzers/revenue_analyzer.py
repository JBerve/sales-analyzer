class RevenueAnalyzer:
<<<<<<< feature/revenue-analyzer
    def __init__(self):
        self.total_revenue = 0
        self.revenue_by_region = {}
        self.total_sales_representatives = {}

    def process(self, sale):
        self.total_revenue += sale.revenue

        self.revenue_by_region[sale.region] = (self.revenue_by_region.get(sale.region, 0) + sale.revenue)
        
        self.total_sales_representatives[sale.sales_rep] = (self.total_sales_representatives.get(sale.sales_rep, 0) + sale.revenue)


    def results(self):
        top_sales_representatives = sorted(self.total_sales_representatives.items(), key=lambda item: item[1], reverse=True)
        top_sales_representatives = top_sales_representatives[:3]
        return {
            "total_revenue": self.total_revenue,
            "revenue_by_region": self.revenue_by_region,
            "top_sales": top_sales_representatives
        }
=======
    def process(self, sale):
        pass

    def results(self):
        return {
            "total_revenue": 0,
            "revenue_by_region": {},
            "revenue_by_category": {},
            "top_sales": []
        }
>>>>>>> develop

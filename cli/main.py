from data.csv_reader import read_sales
from services.analyzers.revenue_analyzer import RevenueAnalyzer
from services.analyzers.discount_analyzer import DiscountAnalyzer
from services.analyzers.units_analyzer import UnitsAnalyzer

def print_results(results):
    print("Sales analysis:\n")
    print(f"Total Revenue: {results['total_revenue']}")
    print(f"Revenue by region: {results['revenue_by_region']}")
    print(f"Top sales representatives: {results['top_sales']}")
    print(f"Total units sold: {results['total_units']}")
    print(f"Revenue by Product Category: {results['revenue_by_category']}")
    print(f"Average discount: {results['average_discount']}")

def main():
    filepath = input("Please, write the name of the file you want to analyze: ")

    revenue_analyzer = RevenueAnalyzer()
    discount_analyzer = DiscountAnalyzer()
    units_analyzer = UnitsAnalyzer()

    analyzers = [
        revenue_analyzer,
        discount_analyzer,
        units_analyzer
    ]

    try:
        for sale in read_sales(filepath):
            for analyzer in analyzers:
                analyzer.process(sale)
        results = {}

        for analyzer in analyzers:
            results.update(analyzer.results())

        print_results(results)
    
    except (FileNotFoundError, IsADirectoryError):
        print(f"Error: file '{filepath}' not found.")

if __name__ == "__main__":
    main()
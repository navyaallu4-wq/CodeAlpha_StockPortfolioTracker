import csv
from utils import load_portfolio
from stock_api import get_current_price


def export_to_csv():
    portfolio = load_portfolio()

    if not portfolio:
        print("\n📂 Portfolio is empty.\n")
        return

    with open("portfolio_report.csv", "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow([
            "Stock",
            "Quantity",
            "Buy Price",
            "Current Price",
            "Investment",
            "Current Value",
            "Profit/Loss"
        ])

        for stock, details in portfolio.items():
            quantity = details["quantity"]
            buy_price = details["buy_price"]

            current_price = get_current_price(stock)

            if current_price is None:
                current_price = 0

            investment = quantity * buy_price
            current_value = quantity * current_price
            profit = current_value - investment

            writer.writerow([
                stock,
                quantity,
                buy_price,
                current_price,
                investment,
                current_value,
                profit
            ])

    print("\n✅ Portfolio exported successfully!")
    print("📄 File Name : portfolio_report.csv")
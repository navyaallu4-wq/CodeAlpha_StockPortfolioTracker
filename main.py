from portfolio import add_stock, view_portfolio, sell_stock, view_history
from utils import load_portfolio
from stock_api import get_current_price
from reports import export_to_csv


def portfolio_value():
    portfolio = load_portfolio()

    if not portfolio:
        print("\n📂 Portfolio is empty.\n")
        return

    total_investment = 0
    total_current = 0

    print("\n" + "=" * 85)
    print(f"{'Stock':<10}{'Qty':<8}{'Buy Price':<12}{'Current':<12}{'Invested':<15}{'Profit/Loss'}")
    print("=" * 85)

    for stock, details in portfolio.items():
        current_price = get_current_price(stock)

        if current_price is None:
            print(f"{stock:<10} Live price not available")
            continue

        quantity = details["quantity"]
        buy_price = details["buy_price"]

        invested = quantity * buy_price
        current_value = quantity * current_price
        profit = current_value - invested

        total_investment += invested
        total_current += current_value

        print(
            f"{stock:<10}"
            f"{quantity:<8}"
            f"₹{buy_price:<11.2f}"
            f"₹{current_price:<11.2f}"
            f"₹{invested:<14.2f}"
            f"₹{profit:.2f}"
        )

    print("=" * 85)

    total_profit = total_current - total_investment
    percentage = (total_profit / total_investment * 100) if total_investment > 0 else 0

    print(f"\nTotal Investment : ₹{total_investment:.2f}")
    print(f"Current Value    : ₹{total_current:.2f}")
    print(f"Profit / Loss    : ₹{total_profit:.2f}")
    print(f"Return           : {percentage:.2f}%")


def main():
    while True:
        print("\n" + "=" * 50)
        print("        STOCK PORTFOLIO TRACKER")
        print("=" * 50)
        print("1. Add Stock")
        print("2. View Portfolio")
        print("3. Sell Stock")
        print("4. Portfolio Summary")
        print("5. Transaction History")
        print("6. Export Portfolio (CSV)")
        print("7. Exit")
        print("=" * 50)

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_stock()

        elif choice == "2":
            view_portfolio()

        elif choice == "3":
            sell_stock()

        elif choice == "4":
            portfolio_value()

        elif choice == "5":
            view_history()

        elif choice == "6":
            export_to_csv()

        elif choice == "7":
            print("\n👋 Thank you for using Stock Portfolio Tracker!")
            break

        else:
            print("\n❌ Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
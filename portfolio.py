from utils import (
    load_portfolio,
    save_portfolio,
    load_history,
    save_history
)
from datetime import datetime


def add_stock():
    portfolio = load_portfolio()

    stock = input("Enter Stock Symbol (e.g., AAPL): ").strip().upper()

    if not stock:
        print("\n❌ Stock symbol cannot be empty.\n")
        return

    try:
        quantity = int(input("Enter Quantity: "))
        buy_price = float(input("Enter Buy Price: "))

        if quantity <= 0:
            print("\n❌ Quantity must be greater than 0.\n")
            return

        if buy_price <= 0:
            print("\n❌ Buy price must be greater than 0.\n")
            return

    except ValueError:
        print("\n❌ Invalid input! Enter valid numbers.\n")
        return

    if stock in portfolio:
        print(f"\n⚠ {stock} already exists.")

        choice = input("Update existing stock? (Y/N): ").strip().upper()

        if choice != "Y":
            print("Operation cancelled.\n")
            return

    portfolio[stock] = {
        "quantity": quantity,
        "buy_price": buy_price
    }

    save_portfolio(portfolio)

    # Save BUY transaction
    history = load_history()
    history.append({
        "type": "BUY",
        "stock": stock,
        "quantity": quantity,
        "price": buy_price,
        "date": datetime.now().strftime("%d-%m-%Y %H:%M")
    })
    save_history(history)

    print(f"\n✅ {stock} saved successfully!\n")


def view_portfolio():
    portfolio = load_portfolio()

    if not portfolio:
        print("\n📂 Portfolio is empty.\n")
        return

    print("\n" + "=" * 55)
    print(f"{'Stock':<15}{'Quantity':<15}{'Buy Price':<15}")
    print("=" * 55)

    for stock, details in portfolio.items():
        print(f"{stock:<15}{details['quantity']:<15}₹{details['buy_price']:<10.2f}")

    print("=" * 55)


def sell_stock():
    portfolio = load_portfolio()

    if not portfolio:
        print("\n📂 Portfolio is empty.\n")
        return

    stock = input("Enter Stock Symbol to Sell: ").strip().upper()

    if stock not in portfolio:
        print("\n❌ Stock not found.\n")
        return

    owned = portfolio[stock]["quantity"]
    buy_price = portfolio[stock]["buy_price"]

    print(f"\nYou currently own {owned} shares.")

    try:
        sell_qty = int(input("Enter Quantity to Sell: "))

        if sell_qty <= 0:
            print("\n❌ Quantity must be greater than zero.\n")
            return

    except ValueError:
        print("\n❌ Invalid Quantity.\n")
        return

    if sell_qty > owned:
        print("\n❌ You don't own that many shares.\n")
        return

    # Save SELL transaction
    history = load_history()
    history.append({
        "type": "SELL",
        "stock": stock,
        "quantity": sell_qty,
        "price": buy_price,
        "date": datetime.now().strftime("%d-%m-%Y %H:%M")
    })
    save_history(history)

    remaining = owned - sell_qty

    if remaining == 0:
        del portfolio[stock]
        print(f"\n✅ Sold all shares of {stock}.")
    else:
        portfolio[stock]["quantity"] = remaining
        print(f"\n✅ Sold {sell_qty} shares.")
        print(f"Remaining Shares : {remaining}")

    save_portfolio(portfolio)


def view_history():
    history = load_history()

    if not history:
        print("\n📂 No transaction history found.\n")
        return

    print("\n" + "=" * 75)
    print(f"{'Type':<10}{'Stock':<10}{'Qty':<10}{'Price':<12}{'Date'}")
    print("=" * 75)

    for item in history:
        print(
            f"{item['type']:<10}"
            f"{item['stock']:<10}"
            f"{item['quantity']:<10}"
            f"₹{item['price']:<11.2f}"
            f"{item['date']}"
        )

    print("=" * 75)
import yfinance as yf


def get_current_price(symbol):
    """
    Returns the latest market price of the given stock symbol.
    """

    try:
        stock = yf.Ticker(symbol)
        data = stock.history(period="1d")

        if data.empty:
            return None

        return round(data["Close"].iloc[-1], 2)

    except Exception:
        return None
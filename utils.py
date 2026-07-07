import json
import os

FILE_NAME = "portfolio.json"


def load_portfolio():
    """Load portfolio data from JSON file."""
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return {}
    return {}


def save_portfolio(portfolio):
    """Save portfolio data to JSON file."""
    with open(FILE_NAME, "w") as file:
        json.dump(portfolio, file, indent=4)

HISTORY_FILE = "history.json"


def load_history():
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return []
    return []


def save_history(history):
    with open(HISTORY_FILE, "w") as file:
        json.dump(history, file, indent=4)
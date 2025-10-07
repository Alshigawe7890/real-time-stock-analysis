import pandas as pd
import os

DATA_DIR = "data"

def calculate_moving_average(df, window=20):
    df["SMA"] = df["Close"].rolling(window=window).mean()
    return df

def analyze_data(symbol):
    filename = os.path.join(DATA_DIR, f"{symbol}_data.csv")
    if not os.path.exists(filename):
        print(f"Error: Data file for {symbol} not found.")
        return

    df = pd.read_csv(filename)
    df["Timestamp"] = pd.to_datetime(df["Timestamp"])
    df = df.set_index("Timestamp")

    # Calculate Simple Moving Average (SMA)
    df = calculate_moving_average(df)

    print(f"\nAnalysis for {symbol}:")
    print(df.tail())

if __name__ == "__main__":
    stock_symbols = ["AAPL", "MSFT", "AMZN", "GOOGL", "TSLA"]
    for symbol in stock_symbols:
        analyze_data(symbol)


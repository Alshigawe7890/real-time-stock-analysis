import pandas as pd
import os

DATA_DIR = "data"
ANALYSIS_DIR = "analysis"

if not os.path.exists(ANALYSIS_DIR):
    os.makedirs(ANALYSIS_DIR)

def calculate_moving_average(df, window=5):
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

    output_filename = os.path.join(ANALYSIS_DIR, f"{symbol}_analysis.csv")
    df.to_csv(output_filename)
    print(f"Analysis for {symbol} saved to {output_filename}")

if __name__ == "__main__":
    stock_symbols = ["AAPL", "MSFT", "AMZN", "GOOGL", "TSLA"]
    for symbol in stock_symbols:
        analyze_data(symbol)


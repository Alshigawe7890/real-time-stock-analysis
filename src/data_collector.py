import yfinance as yf
import time
import os
import csv
from datetime import datetime

DATA_DIR = "data"
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

def save_to_csv(symbol, data):
    filename = os.path.join(DATA_DIR, f"{symbol}_data.csv")
    file_exists = os.path.isfile(filename)

    with open(filename, mode=\'a\', newline=\'\') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Timestamp", "Symbol", "Open", "High", "Low", "Close", "Volume"])
        writer.writerow([data["Timestamp"], symbol, data["Open"], data["High"], data["Low"], data["Close"], data["Volume"]])

def fetch_realtime_data(symbols):
    for symbol in symbols:
        try:
            ticker = yf.Ticker(symbol)
            # Get the most recent intraday data (e.g., 1-minute interval)
            # Note: Yahoo Finance API might have limitations on real-time intraday data for free users.
            # This will fetch the latest available data point.
            hist = ticker.history(period="1d", interval="1m")

            if not hist.empty:
                latest_data = hist.iloc[-1]
                timestamp = latest_data.name.strftime("%Y-%m-%d %H:%M:%S")
                data_to_save = {
                    "Timestamp": timestamp,
                    "Open": latest_data["Open"],
                    "High": latest_data["High"],
                    "Low": latest_data["Low"],
                    "Close": latest_data["Close"],
                    "Volume": latest_data["Volume"],
                }
                save_to_csv(symbol, data_to_save)
                print(f"Saved data for {symbol}: {data_to_save}")
            else:
                print(f"No data available for {symbol} at this interval.")
        except Exception as e:
            print(f"Error fetching data for {symbol}: {e}")

if __name__ == "__main__":
    # List of US stock symbols to track
    stock_symbols = ["AAPL", "MSFT", "AMZN", "GOOGL", "TSLA"]
    
    print("Starting real-time data collection using yfinance...")
    while True:
        fetch_realtime_data(stock_symbols)
        time.sleep(60) # Fetch data every 60 seconds (1 minute)


import websocket
import json
import os
import time
import csv
from datetime import datetime

# Replace with your Finnhub API key
FINNHUB_API_KEY = os.environ.get("FINNHUB_API_KEY")

if not FINNHUB_API_KEY:
    print("Error: FINNHUB_API_KEY environment variable not set.")
    exit()

DATA_DIR = "../data"
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

def save_to_csv(data):
    symbol = data["s"]
    price = data["p"]
    timestamp_ms = data["t"]
    volume = data["v"]
    conditions = ",".join(data["c"]) if "c" in data else ""

    # Convert UNIX milliseconds timestamp to readable datetime
    dt_object = datetime.fromtimestamp(timestamp_ms / 1000)
    formatted_timestamp = dt_object.strftime("%Y-%m-%d %H:%M:%S.%f")[:-3] # Remove last 3 digits for milliseconds

    filename = os.path.join(DATA_DIR, f"{symbol}_trades.csv")
    file_exists = os.path.isfile(filename)

    with open(filename, mode=\'a\', newline=\'\') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Timestamp", "Symbol", "Price", "Volume", "Conditions"])
        writer.writerow([formatted_timestamp, symbol, price, volume, conditions])

def on_message(ws, message):
    data = json.loads(message)
    if data[\'type\'] == \'trade\':
        for trade in data[\'data\']:
            save_to_csv(trade)
            print(f"Saved trade: Symbol: {trade[\'s\']}, Price: {trade[\'p\']}, Timestamp: {trade[\'t\']}, Volume: {trade[\'v\']}")

def on_error(ws, error):
    print(f"Error: {error}")

def on_close(ws, close_status_code, close_msg):
    print("### closed ###")

def on_open(ws):
    print("Opened connection")
    # Subscribe to a stock symbol, e.g., Apple (AAPL)
    ws.send(json.dumps({"type":"subscribe","symbol":"AAPL"}))
    ws.send(json.dumps({"type":"subscribe","symbol":"MSFT"}))
    ws.send(json.dumps({"type":"subscribe","symbol":"AMZN"}))

if __name__ == "__main__":
    # websocket.enableTrace(True) # Uncomment for debugging WebSocket traffic
    ws = websocket.WebSocketApp(f"wss://ws.finnhub.io?token={FINNHUB_API_KEY}",
                                on_open=on_open,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)

    ws.run_forever()


import websocket
import json
import os
import time

# Replace with your Finnhub API key
FINNHUB_API_KEY = os.environ.get("FINNHUB_API_KEY")

if not FINNHUB_API_KEY:
    print("Error: FINNHUB_API_KEY environment variable not set.")
    exit()

def on_message(ws, message):
    data = json.loads(message)
    if data['type'] == 'trade':
        for trade in data['data']:
            symbol = trade['s']
            price = trade['p']
            timestamp = trade['t']
            volume = trade['v']
            print(f"Symbol: {symbol}, Price: {price}, Timestamp: {timestamp}, Volume: {volume}")
            # Here you would typically save the data to a database or a file
            # For now, we just print it.

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
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp(f"wss://ws.finnhub.io?token={FINNHUB_API_KEY}",
                                on_open=on_open,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)

    ws.run_forever()


from binance.client import Client

def get_binance_price(api_key: str, api_secret: str, symbol: str):
    client = Client(api_key, api_secret)
    ticker = client.get_symbol_ticker(symbol=symbol)
    return float(ticker['price'])
from binance.client import Client


def get_binance_volume(api_key: str, api_secret: str, symbol: str):
    client = Client(api_key, api_secret)
    ticker_24h = client.get_ticker(symbol=symbol)
    return float(ticker_24h['quoteVolume'])
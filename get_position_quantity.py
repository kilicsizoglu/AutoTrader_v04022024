import list_trade
from binance.client import Client


def USDTQuantity(apikey, apisecret, coin_name):
    try:
        client = Client(apikey, apisecret)
        tickers = client.futures_get_open_orders()
        order_quantity = 0
        for ticker in tickers:
            if ticker["symbol"] == coin_name:
                if ticker["type"] != "STOP":
                    order_quantity += (abs((float(ticker["origQty"])) * float(ticker["price"])))
        tickers = list_trade.ListTrade(apikey, apisecret)
        for ticker in tickers:
            if ticker["symbol"] == coin_name:
                order_quantity += ((abs(float(ticker["positionAmt"])) * float(ticker["entryPrice"])))
                res = client.futures_account_balance()
                for r in res:
                    if r["asset"] == "USDT":
                        return abs(order_quantity)
    except Exception as e:
        return 0

    return 0
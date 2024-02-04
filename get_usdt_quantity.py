import list_trade
from binance.client import Client


def USDTQuantity(apikey, apisecret):
    try:
        client = Client(apikey, apisecret)
        tickers = client.futures_get_open_orders()
        order_quantity = 0
        for ticker in tickers:
                if ticker["type"] != "STOP":
                    order_quantity += (abs((float(ticker["origQty"])) * float(ticker["price"])) / 25)
        tickers = list_trade.ListTrade(apikey, apisecret)
        for ticker in tickers:
                order_quantity += ((abs(float(ticker["positionAmt"])) * float(ticker["entryPrice"])) / 25)
                res = client.futures_account_balance()
                for r in res:
                    if r["asset"] == "USDT":
                        return float(r["balance"]) - order_quantity
    except Exception as e:
        return 0

    return 0
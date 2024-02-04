import datetime

from binance import Client

import ta_api_request


def Sell(apikey, apisecretkey, coinname, quantity):
    try:
        client = Client(apikey, apisecretkey)
        client.futures_change_leverage(symbol=coinname, leverage=25)
        res = client.futures_create_order(symbol=coinname,
                                                              side='SELL',
                                                              type="MARKET",
                                                              quantity=quantity)
        if res['orderId'] is not None:
            return res
        else:
            return None
    except Exception as e:
        print(e)
        return None

def LossProtect(apikey, apisecretkey, coinname, quantity, price, stopPrice):
    try:
        client = Client(apikey, apisecretkey)
        res = client.futures_create_order(symbol=coinname,
                                          side='BUY',
                                          type=Client.FUTURE_ORDER_TYPE_STOP,
                                          quantity=quantity,
                                          timeinforce='GTC',
                                          stopPrice=stopPrice,
                                          price=price)
        if res['orderId'] is not None:
            return True
        else:
            return False
    except Exception as e:
        print(e)
        return False
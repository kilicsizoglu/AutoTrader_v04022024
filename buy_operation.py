from binance import Client

import list_trade

def Buy(apikey, apisecretkey, coinname, quantity):
    try:
        client = Client(apikey, apisecretkey)
        client.futures_change_leverage(symbol=coinname, leverage=25)
        res = client.futures_create_order(symbol=coinname,
                                                              side='BUY',
                                                              type="MARKET",
                                                              quantity=quantity)
        if res['orderId'] is not None:
            return True
        else:
            return False
    except Exception as e:
        print(e)
        return False

def LossProtect(apikey, apisecretkey, coinname, quantity, price, stopPrice):
    try:
        client = Client(apikey, apisecretkey)
        res = client.futures_create_order(symbol=coinname,
                                          side='SELL',
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
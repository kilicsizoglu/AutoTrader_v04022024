import datetime
import time

from binance import Client

def ListTrade(apikey, apisecretkey):

    try:
        client = Client(apikey, apisecretkey)
        res = client.futures_position_information()
        if res is not None:
            return res
        else:
            return None
    except Exception as e:
        print(e)
        return None
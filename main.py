import datetime
import time
import matplotlib.pyplot as plt
from mongoengine import connect, disconnect
import binance_price
import binance_volume
import arima_predict
import list_trade
import mongo_price_table
import prophet_predict
import ta_api_request
import get_api_credentials_binance
import get_api_credentials_ta_api
import get_position_quantity
import get_usdt_quantity
import sell_operation
import buy_operation
import mongo_position_info_table


def main():
    status = ""
    t = datetime.datetime.now()
    position_status = False
    position_operation = ""
    position_price = 0
    results = []
    prices = []
    score = 0.1  # Initialize score
    accuracy_threshold = 0.005  # Define a threshold for accuracy, e.g., 0.5%

    #"""
    # create an empty figure and axes
    plt.figure(figsize=(12, 6))
    ax = plt.gca()
    #"""
    pre_result = 0

    while True:
        binance_apikey, binance_secret = get_api_credentials_binance.get_api_credentials_binance("binance-api-key.txt")
        ta_apikey = get_api_credentials_ta_api.get_api_credentials_ta_api("ta-api-key.txt")

        dent = get_position_quantity.USDTQuantity(binance_apikey, binance_secret, "DENTUSDT")
        usdt = get_usdt_quantity.USDTQuantity(binance_apikey, binance_secret)

        pre_price = float(ta_api_request.get_price(ta_apikey, "DENTUSDT", "1m")["value"])
        volume = float(binance_volume.get_binance_volume(binance_apikey, binance_secret, "DENTUSDT"))
        macd_data = ta_api_request.get_macd(ta_apikey, "DENTUSDT", "1m")
        macd = float(macd_data["valueMACD"])
        signal = float(macd_data["valueMACDSignal"])
        rsi = float(ta_api_request.get_relative_strength_index(ta_apikey, "DENTUSDT", "1m")["value"])

        disconnect("default")
        connect(host='localhost', port=27017)

        t = datetime.datetime.now()
        print("Time : " + str(t))
        result = arima_predict.train_and_predict_price_arima("DENTUSDT", pre_price, volume, macd, signal, rsi)
        t = datetime.datetime.now()
        print("Time : " + str(t))
        price = float(ta_api_request.get_price(ta_apikey, "DENTUSDT", "1m")["value"])

        if result is not None:
            print("Try to buy or sell")
            result = round(result, 6)
            pre_result = round(pre_result, 6)
            price = round(price, 6)
            s = result - pre_result
            print("{:.15f}".format(s))
            if result is not None and status is not None:
                print("price : " + str(price) + " predict : " + str(result))
            if (pre_result - result) >= 0.0000001 and pre_result != 0:
                if position_status is False:
                    print("SHORT OPERATION")
                    price = float(ta_api_request.get_price(ta_apikey, "DENTUSDT", "1m")["value"])
                    position_price = price
                    position_operation = "SHORT"
                    position_status = True
                if float(usdt) > 6:
                    sell_operation.Sell(binance_apikey, binance_secret, "DENTUSDT", round((25 * 6) / price, 0))
            if (((result - pre_result) >= 0 and pre_result != 0)):
                if position_status is True and position_operation == "SHORT":
                    data = mongo_position_info_table.CryptoPositionInfoClass()
                    data.symbol = "DENTUSDT"
                    data.type = position_operation
                    data.price = position_price
                    price = float(ta_api_request.get_price(ta_apikey, "DENTUSDT", "1m")["value"])
                    data.price_sb = price
                    data.earning = (position_price - price)
                    if data.earning > 0.00000001:
                        data.earning_status = "WIN"
                    elif data.earning < 0.00000001:
                        data.earning_status = "LOSS"
                    else:
                        data.earning_status = "EQUAL"
                    data.save()
                    position_status = False
                    position_price = 0
                    position_operation = ""
                    print("SHORT OPERATION END")
                if float(dent) > 0:
                    buy_operation.Buy(binance_apikey, binance_secret, "DENTUSDT", round((dent) / price, 0))
            if (result - pre_result) >= 0.0000001 and pre_result != 0:
                if position_status is False:
                    print("LONG OPERATION")
                    price = float(ta_api_request.get_price(ta_apikey, "DENTUSDT", "1m")["value"])
                    position_price = price
                    position_operation = "LONG"
                    position_status = True
                if float(usdt) > 6:
                    dent = get_position_quantity.USDTQuantity(binance_apikey, binance_secret, "DENTUSDT")
                    buy_operation.Buy(binance_apikey, binance_secret, "DENTUSDT", round((25 * 6) / price, 0))
            if (((pre_result - result) >= 0.000001 and pre_result != 0)):
                if position_status is True and position_operation == "LONG":
                    data = mongo_position_info_table.CryptoPositionInfoClass()
                    data.symbol = "DENTUSDT"
                    data.type = position_operation
                    data.price = position_price
                    price = float(ta_api_request.get_price(ta_apikey, "DENTUSDT", "1m")["value"])
                    data.price_sb = price
                    data.earning = (price - position_price)
                    if data.earning > 0:
                        data.earning_status = "WIN"
                    elif data.earning < 0.00000001:
                        data.earning_status = "LOSS"
                    else:
                        data.earning_status = "EQUAL"
                    data.save()
                    position_status = False
                    position_price = 0
                    position_operation = ""
                    print("LONG OPERATION END")
                if float(dent) > 0:
                    dent = get_position_quantity.USDTQuantity(binance_apikey, binance_secret, "DENTUSDT")
                    sell_operation.Sell(binance_apikey, binance_secret, "DENTUSDT", round((dent) / price, 0))

            pre_result = result

            score = 0.05  # Initialize score
            list = mongo_position_info_table.CryptoPositionInfoClass.objects()
            count = mongo_position_info_table.CryptoPositionInfoClass.objects.count()
            if count > 0:
                for data in list:
                    if data.earning_status == "WIN":
                        score += data.earning.__float__() * 250000
                    if data.earning_status == "LOSS":
                        score -= abs(data.earning.__float__() * 250000)
                    if data.earning_status == "EQUAL":
                        score -= 0.05
            print("Score : " + str(score))

        # limit lists to the last 100 values
        results = results[-100:]
        prices = prices[-100:]


        print("Adding Data")

        time.sleep(10)

        second_price = float(ta_api_request.get_price(ta_apikey, "DENTUSDT", "1m")["value"])
        db_save = mongo_price_table.CryptoPriceClass()
        db_save.symbol = "DENTUSDT"
        db_save.volume = volume
        db_save.price = pre_price
        db_save.macd = float(macd)
        db_save.signal = float(signal)
        db_save.rsi = rsi
        db_save.predict_price = second_price
        db_save.save()

        # store results and values for plots
        results.append(result)
        prices.append(price)

        #"""
        ax.clear()
        ax.plot(results, label='Predicted Price')
        ax.plot(prices, label='Actual Price')
        # clear the current axes and plot the new data
        ax.set_xlabel("Time")
        ax.set_ylabel("Price")
        ax.legend()
        plt.pause(0.01)  # add a short pause to update the figure
        #"""

if __name__ == '__main__':
    main()
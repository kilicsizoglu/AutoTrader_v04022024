import pandas as pd
from prophet import Prophet

import mongo_price_table
import predict_pretect_model


def train_and_predict_price(coin_name, price, volume, macd, signal, rsi):
    data_query = list(mongo_price_table.CryptoPriceClass.objects)

    if len(data_query) == 0:
        return None

    data = []
    for item in data_query:
        data_dict = {
            'symbol': item.symbol,
            'time': item.time,
            'price': item.price,
            "volume": item.volume,
            "macd": item.macd,
            "signal": item.signal,
            "rsi": item.rsi,
            'predict_price': item.predict_price,
        }
        data.append(pd.DataFrame(data_dict, index=[0]))

    df = pd.concat(data, ignore_index=True)

    df["volume"] = df["volume"].astype(float)
    df["price"] = df["price"]
    df["macd"] = df["macd"].astype(float)
    df["signal"] = df["signal"].astype(float)
    df["rsi"] = df["rsi"].astype(float)

    if not {'time', 'predict_price', 'volume', 'price', 'macd', 'signal', 'rsi'}.issubset(df.columns):
        raise ValueError('Columns time, predict_price, volume, price, macd, signal, and/or rsi are not present in the data.')

    df = df[['time', 'predict_price', 'volume', 'price', 'macd', 'signal', 'rsi']].rename(columns={'time': 'ds', 'predict_price': 'y'})

    if len(df.dropna()) < 2:
        return None

    model = Prophet(changepoint_prior_scale=0.01, yearly_seasonality=False, weekly_seasonality=False, daily_seasonality=True)

    model.add_regressor('volume')
    model.add_regressor('price')
    model.add_regressor('macd')
    model.add_regressor('signal')
    model.add_regressor('rsi')

    model.fit(df)

    future = model.make_future_dataframe(periods=5, freq='30min')

    future["volume"] = volume
    future["price"] = price
    future["macd"] = macd
    future["signal"] = signal
    future["rsi"] = rsi

    forecast = model.predict(future)

    # Tüm tahmin edilen değerleri almak için
    # predicted_values = forecast['yhat']

    # Sadece son tahmin edilen değeri almak için
    predicted_value = forecast['yhat'].iloc[-1]

    return predicted_value

def train_and_predict_protect(coin_name, price, volume, macd, signal, rsi):
    data_query = list(predict_pretect_model.PredictProtectModel.objects)

    if len(data_query) == 0:
        return None

    data = []
    for item in data_query:
        data_dict = {
            'symbol': item.symbol,
            'time': item.time,
            'price': item.price,
            "volume": item.volume,
            "macd": item.macd,
            "signal": item.signal,
            "rsi": item.rsi,
            'end_status': item.end_status
        }
        data.append(pd.DataFrame(data_dict, index=[0]))

    df = pd.concat(data, ignore_index=True)

    status_mapping = {"EQUAL": 0, "BUY": 1, "SELL": -1}

    df['end_status'] = df['end_status'].map(status_mapping)

    df["volume"] = df["volume"].astype(float)
    df["price"] = df["price"]
    df["macd"] = df["macd"].astype(float)
    df["end_status"] = df["end_status"].astype(float)
    df["signal"] = df["signal"].astype(float)
    df["rsi"] = df["rsi"].astype(float)

    if not {'time', 'volume', 'price', 'macd', "end_status", 'signal', 'rsi'}.issubset(df.columns):
        raise ValueError('Columns time, volume, price, macd, signal, and/or rsi are not present in the data.')

    df = df[['time', 'volume', 'price', 'macd', "end_status", 'signal', 'rsi']].rename(columns={'time': 'ds', 'end_status': 'y'})

    if len(df.dropna()) < 2:
        return None

    model = Prophet(changepoint_prior_scale=0.01, yearly_seasonality=False, weekly_seasonality=False, daily_seasonality=True)

    model.add_regressor('volume')
    model.add_regressor('price')
    model.add_regressor('macd')
    model.add_regressor('signal')
    model.add_regressor('rsi')

    model.fit(df)

    future = model.make_future_dataframe(periods=5, freq='30min')

    future["volume"] = volume
    future["price"] = price
    future["macd"] = macd
    future["signal"] = signal
    future["rsi"] = rsi

    forecast = model.predict(future)

    # Tüm tahmin edilen değerleri almak için
    # predicted_values = forecast['yhat']

    # Sadece son tahmin edilen değeri almak için
    predicted_value = forecast['yhat'].iloc[-1]

    status = ""
    if -0.5 < predicted_value < 0.5:
        status = "EQUAL"
    elif predicted_value > 0.5:
        status = "BUY"
    elif predicted_value < -0.5:
        status = "SELL"
    else:
        status = "EQUAL"

    return status
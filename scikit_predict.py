import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from datetime import datetime, timedelta

import mongo_price_table

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
        data.append(data_dict)

    df = pd.DataFrame(data)

    df["volume"] = df["volume"].astype(float)
    df["price"] = df["price"]
    df["macd"] = df["macd"].astype(float)
    df["signal"] = df["signal"].astype(float)
    df["rsi"] = df["rsi"].astype(float)

    if not {'time', 'predict_price', 'volume', 'price', 'macd', 'signal', 'rsi'}.issubset(df.columns):
        raise ValueError('Columns time, predict_price, volume, price, macd, signal, and/or rsi are not present in the data.')

    df['time'] = pd.to_datetime(df['time'])
    df = df[['time', 'predict_price', 'volume', 'price', 'macd', 'signal', 'rsi']]

    if len(df.dropna()) < 2:
        return None

    # Create a lag feature for 'predict_price' to use as a target variable
    df['y'] = df['predict_price'].shift(-1)

    # Drop the last row since it has NaN for 'y'
    df = df.dropna()

    # Split the data into features and target
    X = df[['volume', 'price', 'macd', 'signal', 'rsi']]
    y = df['y']

    # Create and train the Linear Regression model
    model = LinearRegression()
    model.fit(X, y)

    # Create a feature vector for prediction using the provided inputs
    input_data = np.array([volume, price, macd, signal, rsi]).reshape(1, -1)

    # Predict the next 'predict_price'
    predicted_value = model.predict(input_data)

    return predicted_value[0]
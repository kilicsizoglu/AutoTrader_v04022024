import pandas as pd
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from datetime import datetime, timedelta

import mongo_price_table

def train_and_predict_price(coin_name, price, volume, macd, signal, rsi):
    data_query = list(mongo_price_table.CryptoPriceClass.objects.filter(symbol=coin_name)) # Only select the specific coin

    if len(data_query) == 0:
        return None

    data = [{'time': item.time, 'price': item.price, 'volume': item.volume, 'macd': item.macd, 'signal': item.signal, 'rsi': item.rsi, 'predict_price': item.predict_price} for item in data_query]

    df = pd.DataFrame(data)

    df["volume"] = df["volume"].astype(float)
    df["price"] = df["price"]
    df["macd"] = df["macd"].astype(float)
    df["signal"] = df["signal"].astype(float)
    df["rsi"] = df["rsi"].astype(float)

    # Adding missing columns check
    if not {'time', 'predict_price', 'volume', 'price', 'macd', 'signal', 'rsi'}.issubset(df.columns):
        raise ValueError('Columns time, predict_price, volume, price, macd, signal, and/or rsi are not present in the data.')

    df.sort_values("time", inplace=True)
    df.reset_index(drop=True, inplace=True)

    # Create labels by shifting the prediction price to the previous row
    df["y"] = df["predict_price"].shift(-1)
    df.dropna(inplace=True)

    # Split the data into features and target
    X = df[['volume', 'price', 'macd', 'signal', 'rsi']]
    y = df['y']

    # Create and train the neural network model
    model = Sequential()
    model.add(Dense(32, input_dim=5, activation='relu'))
    model.add(Dense(16, activation='relu'))
    model.add(Dense(1, activation='linear'))

    model.compile(loss='mean_squared_error', optimizer='adam')

    model.fit(X, y, epochs=50, batch_size=10, verbose=0)

    # Create a feature vector for prediction using the provided inputs
    input_data = np.array([volume, price, macd, signal, rsi]).reshape(1, -1)

    # Predict the next 'predict_price'
    predicted_value = model.predict(input_data)

    return predicted_value[0,0]  # As the output of model.predict is 2D, we need to pick only first element
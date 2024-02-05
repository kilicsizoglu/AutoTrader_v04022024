import pandas as pd
import pmdarima as pm

import mongo_price_table

def train_and_predict_price_arima(coin_name, price, volume, macd, signal, rsi):
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

    # Dönüştürme ve indeksleme
    df['time'] = pd.to_datetime(df['time'])
    df = df.set_index('time')
    df = df.sort_index()

    # Uygun veri türlerine dönüştürme
    df["volume"] = df["volume"].astype(float)
    df["price"] = df["price"].astype(float)
    df["macd"] = df["macd"].astype(float)
    df["signal"] = df["signal"].astype(float)
    df["rsi"] = df["rsi"].astype(float)

    # Gerekli sütunların kontrolü
    if not {'price', 'volume', 'macd', 'signal', 'rsi'}.issubset(df.columns):
        raise ValueError('Columns price, volume, macd, signal, and rsi are not present in the data.')

    # ARIMA modelini uygulama
    model = pm.auto_arima(df['price'], exogenous=df[['volume', 'macd', 'signal', 'rsi']],
                          seasonal=False, m=1, d=1, stepwise=True, suppress_warnings=True)

    # Gelecekteki veri noktaları için tahmin
    future_exog = pd.DataFrame({
        "volume": [volume],
        "price": [price],
        "macd": [macd],
        "signal": [signal],
        "rsi": [rsi],
    })
    predictions = model.predict(n_periods=5, exogenous=future_exog)

    # Son tahmin edilen değeri almak
    predictions = pd.Series(model.predict(n_periods=5, exogenous=future_exog))
    predicted_value = predictions.iloc[-1]

    return predicted_value

# Örnek kullanım:
# result = train_and_predict_price_arima("DENTUSDT", pre_price, volume, macd, signal, rsi)
# print(result)

import time

import pandas as pd
import requests
import json

def get_oscillator(api_key: str, symbol: str, interval: str):
    time.sleep(0.5)
    url = f"https://api.taapi.io/rsi?secret={api_key}&exchange=binancefutures&symbol={symbol}&interval={interval}"
    response = requests.get(url)
    data = response.json()
    return data

def get_price(api_key: str, symbol: str, interval: str):
    time.sleep(0.5)
    url = f"https://api.taapi.io/price?secret={api_key}&exchange=binancefutures&symbol={symbol}&interval={interval}"
    response = requests.get(url)
    data = response.json()
    return data

def get_choppiness_index(api_key: str, symbol: str, interval: str):
    time.sleep(0.5)
    url = f"https://api.taapi.io/chop?secret={api_key}&exchange=binancefutures&symbol={symbol}&interval={interval}"
    response = requests.get(url)
    data = response.json()
    return data

def get_coppock_curve(api_key: str, symbol: str, interval: str):
    time.sleep(0.5)
    url = f"https://api.taapi.io/coppockcurve?secret={api_key}&exchange=binancefutures&symbol={symbol}&interval={interval}"
    response = requests.get(url)
    data = response.json()
    return data

def get_detrended_price_oscillator(api_key: str, symbol: str, interval: str):
    time.sleep(0.5)
    url = f"https://api.taapi.io/dpo?secret={api_key}&exchange=binancefutures&symbol={symbol}&interval={interval}&period=50"
    response = requests.get(url)
    data = response.json()
    return data

def get_directional_movement_index_dx(api_key: str, symbol: str, interval: str):
    time.sleep(0.5)
    url = f"https://api.taapi.io/dx?secret={api_key}&exchange=binancefutures&symbol={symbol}&interval={interval}"
    response = requests.get(url)
    data = response.json()
    return data

def get_ease_of_movement(api_key: str, symbol: str, interval: str):
    time.sleep(0.5)
    url = f"https://api.taapi.io/eom?secret={api_key}&exchange=binancefutures&symbol={symbol}&interval={interval}"
    response = requests.get(url)
    data = response.json()
    return data

def get_forecast_oscillator(api_key: str, symbol: str, interval: str):
    time.sleep(0.5)
    url = f"https://api.taapi.io/fosc?secret={api_key}&exchange=binancefutures&symbol={symbol}&interval={interval}&period=50"
    response = requests.get(url)
    data = response.json()
    return data

def get_money_flow_index(api_key: str, symbol: str, interval: str):
    time.sleep(0.5)
    url = f"https://api.taapi.io/mfi?secret={api_key}&exchange=binancefutures&symbol={symbol}&interval={interval}"
    response = requests.get(url)
    data = response.json()
    return data

def get_percentage_price_oscillator(api_key: str, symbol: str, interval: str):
    time.sleep(0.5)
    url = f"https://api.taapi.io/ppo?secret={api_key}&exchange=binancefutures&symbol={symbol}&interval={interval}"
    response = requests.get(url)
    data = response.json()
    return data


def get_rate_of_change(api_key: str, symbol: str, interval: str):
    time.sleep(0.5)
    url = f"https://api.taapi.io/roc?secret={api_key}&exchange=binancefutures&symbol={symbol}&interval={interval}"
    response = requests.get(url)
    data = response.json()
    return data


def get_relative_strength_index(api_key: str, symbol: str, interval: str):
    time.sleep(0.5)
    url = f"https://api.taapi.io/rsi?secret={api_key}&exchange=binancefutures&symbol={symbol}&interval={interval}"
    response = requests.get(url)
    data = response.json()
    return data


def get_stochastic_oscillator(api_key: str, symbol: str, interval: str):
    time.sleep(0.5)
    url = f"https://api.taapi.io/stoch?secret={api_key}&exchange=binancefutures&symbol={symbol}&interval={interval}"
    response = requests.get(url)
    data = response.json()
    return data


def get_stochastic_fast(api_key: str, symbol: str, interval: str):
    time.sleep(0.5)
    url = f"https://api.taapi.io/stochf?secret={api_key}&exchange=binancefutures&symbol={symbol}&interval={interval}"
    response = requests.get(url)
    data = response.json()
    return data


def get_stoch_rsi(api_key: str, symbol: str, interval: str):
    time.sleep(0.5)
    url = f"https://api.taapi.io/stochrsi?secret={api_key}&exchange=binancefutures&symbol={symbol}&interval={interval}"
    response = requests.get(url)
    data = response.json()
    return data


def get_trix(api_key: str, symbol: str, interval: str):
    time.sleep(0.5)
    url = f"https://api.taapi.io/trix?secret={api_key}&exchange=binancefutures&symbol={symbol}&interval={interval}"
    response = requests.get(url)
    data = response.json()
    return data

def get_price_direction(api_key: str, symbol: str, interval: str):
    time.sleep(0.5)
    url = f"https://api.taapi.io/pd?secret={api_key}&exchange=binancefutures&symbol={symbol}&interval={interval}"
    response = requests.get(url)
    data = response.json()
    return data

def get_ease_of_movement(api_key: str, symbol: str, interval: str):
    time.sleep(0.5)
    url = f"https://api.taapi.io/eom?secret={api_key}&exchange=binancefutures&symbol={symbol}&interval={interval}"
    response = requests.get(url)
    data = response.json()
    return data

def get_directional_movement_index(api_key: str, symbol: str, interval: str):
    time.sleep(0.5)
    url = f"https://api.taapi.io/dmi?secret={api_key}&exchange=binancefutures&symbol={symbol}&interval={interval}"
    response = requests.get(url)
    data = response.json()
    return data

def get_volume_oscillator(api_key: str, symbol: str, interval: str):
    time.sleep(0.5)
    url = f"https://api.taapi.io/vosc?secret={api_key}&exchange=binancefutures&symbol={symbol}&interval={interval}"
    response = requests.get(url)
    data = response.json()
    return data

def get_moving_average(api_key: str, symbol: str, interval: str):
    time.sleep(0.5)
    url = f"https://api.taapi.io/ma?secret={api_key}&exchange=binancefutures&symbol={symbol}&interval={interval}"
    response = requests.get(url)
    data = response.json()
    return data

# Removing duplicates for get_directional_movement and get_ultimate_oscillator functions
def get_directional_movement(api_key: str, symbol: str, interval: str):
    time.sleep(0.5)
    url = f"https://api.taapi.io/dm?secret={api_key}&exchange=binancefutures&symbol={symbol}&interval={interval}&period=50"
    response = requests.get(url)
    data = response.json()
    return data


def get_macd(api_secret: str, symbol: str, interval: str):
    time.sleep(0.5)
    url = f"https://api.taapi.io/macd?secret={api_secret}&exchange=binance&symbol={symbol}&interval={interval}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        # İstek başarısız olduysa hata durumunu işle
        print(f"Hata kodu: {response.status_code}")
        return None

def get_ultimate_oscillator(api_key: str, symbol: str, interval: str):
    time.sleep(0.5)
    url = f"https://api.taapi.io/ultosc?secret={api_key}&exchange=binancefutures&symbol={symbol}&interval={interval}"
    response = requests.get(url)
    data = response.json()
    return data
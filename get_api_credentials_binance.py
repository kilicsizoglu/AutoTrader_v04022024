import json

def get_api_credentials_binance(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
        return data['apiKey'], data['secret']
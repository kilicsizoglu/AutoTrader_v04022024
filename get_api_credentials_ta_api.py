import json

def get_api_credentials_ta_api(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
        return data['apikey']
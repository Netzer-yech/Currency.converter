
import requests
import json

def get_rates():
    api_key = "caad6a6a74764f9caa9628e1c8c2fa4a"
    url = f"https://openexchangerates.org/api/latest.json?app_id={api_key}"
    response = requests.get(url)
    data = json.loads(response.text)
    return data

print(get_rates()["rates"])
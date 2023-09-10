
import requests
import json
import time

last_currency_rates = {}
last_update_time = 0
update_interval = 60 * 60  # 60 minutes

def update_currency_rates():

    global last_currency_rates, last_update_time

    current_time = time.time()

    # Check if the rates need to be updated
    if current_time - last_update_time >= update_interval:
        # Fetch new rates from the API
        new_rates = get_rates()

        # Update the cache and timestamp
        last_currency_rates = new_rates
        last_update_time = current_time
def get_rates():
    api_key = "caad6a6a74764f9caa9628e1c8c2fa4a"
    url = f"https://openexchangerates.org/api/latest.json?app_id={api_key}"
    response = requests.get(url)
    data = json.loads(response.text)
    return data

print(get_rates())
update_currency_rates()
print(last_currency_rates["rates"]["ILS"])
print(last_currency_rates["rates"]["EUR"])
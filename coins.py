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
    fetched_rates = json.loads(response.text)
    return fetched_rates


class ILS:
    def get_value(self):
        update_currency_rates()
        ils_rate = round(last_currency_rates["rates"]["ILS"], 4)
        # ["rates"] is to retrieve the value of the key "rates" from the "data" dictionary that return from get_rates() method
        # "rates" value is another dictionary
        # ["ILS"] is to retrieve the value of the key "ILS" from the "rates" dictionary
        return ils_rate

    def calculate(self, user_input):
        return round(user_input / self.get_value(), 4)

class USD:
    def get_value(self):
        update_currency_rates()
        ils_rate = round(last_currency_rates["rates"]["ILS"], 4)
        return ils_rate
    def calculate(self, user_input):
        return round(user_input * self.get_value(), 4)

class EUR:
    def get_value_1(self):
        update_currency_rates()
        eur_rate = round(last_currency_rates["rates"]["EUR"], 4)
        return eur_rate

    def get_value_2(self):
        update_currency_rates()
        ils_rate = round(last_currency_rates["rates"]["ILS"], 4)
        return ils_rate
    def calculate(self, user_input):
        return round(user_input / self.get_value_2() * self.get_value_1(), 4)

# creating classes for easy control on codes in program


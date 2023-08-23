import requests
import json

def get_rates():
    api_key = "caad6a6a74764f9caa9628e1c8c2fa4a"
    url = f"https://openexchangerates.org/api/latest.json?app_id={api_key}"
    response = requests.get(url)
    data = json.loads(response.text)
    return data


class ILS:
    def get_value(self):
        ils_rate = round(get_rates()["rates"]["ILS"], 4)
        return ils_rate

    def calculate(self, user_input):
        return round(user_input / self.get_value(), 2)

class USD:
    def get_value(self):
        ils_rate = round(get_rates()["rates"]["ILS"], 4)
        return ils_rate
    def calculate(self, user_input):
        return round(user_input * self.get_value(), 2)

class EUR:
    def get_value_1(self):
        eur_rate = round(get_rates()["rates"]["EUR"], 4)
        return eur_rate

    def get_value_2(self):
        ils_rate = round(get_rates()["rates"]["ILS"], 4)
        return ils_rate
    def calculate(self, user_input):
        return round(user_input / self.get_value_2() * self.get_value_1(), 2)

# creating classes for easy control on codes in program


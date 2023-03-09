
# import requests

# base_currency = "USD"
# target_currency = "ILS"
# api_key = "caad6a6a74764f9caa9628e1c8c2fa4a"

# api_url = f"https://openexchangerates.org/api/latest.json?app_id={api_key}&base={base_currency}&symbols={target_currency}"
# response = requests.get(api_url)

# if response.status_code == 200:
#     data = response.json()
#     rate = data["rates"][target_currency]
#     print(f"1 {base_currency} = {rate} {target_currency}")
# else:
#     print("Could not get rate from API using default rate...")
#     rate = 0.28
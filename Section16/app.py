import requests
import time
from libs.openexchange import OpenExchangeClient

APP_ID = "1c44f476665d44828bc4c6b72169f4ae"
# ENDPOINT = "https://openexchangerates.org/api/latest.json"
#
# response = requests.get(f"{ENDPOINT}?app_id={APP_ID}")
# exchange_rates = response.json()['rates']
client = OpenExchangeClient(APP_ID)


usd_amount = 1000
start = time.time()
gbp_amount = client.convert(usd_amount, "USD", "GBP")
end = time.time()

print(end - start)

usd_amount = 1000
start = time.time()
gbp_amount = client.convert(usd_amount, "USD", "GBP")
end = time.time()

print(end - start)

usd_amount = 1000
start = time.time()
gbp_amount = client.convert(usd_amount, "USD", "GBP")
end = time.time()

print(end - start)

print(f"USD {usd_amount} is GBP {gbp_amount:.2f}")

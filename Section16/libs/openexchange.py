# import functools
from cachetools import cached, TTLCache
import requests


class OpenExchangeClient:
    BASE_URL = "https://openexchangerates.org/api"

    def __init__(self, app_id):
        self.app_id = app_id

    # @property
    # @functools.lru_cache(maxsize=2)
    @cached(cache=TTLCache(maxsize=2, ttl=900))
    def latest(self):
        return requests.get(f"{self.BASE_URL}/latest.json?app_id={self.app_id}").json()

    def convert(self, from_amount, from_currncy, to_currency):
        rates = self.latest()["rates"]
        to_rate = rates[to_currency]

        if from_currncy == "USD":
            return from_amount * to_rate
        else:
            from_in_usd = from_amount / rates[from_currncy]
            return from_in_usd * to_rate

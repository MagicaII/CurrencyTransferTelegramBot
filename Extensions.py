import requests
import json
from config import keys


class APIException(Exception):
    pass


class CryptoConverter:
    @staticmethod
    def get_price(quote: str, base: str, amount: str):
        if quote == base:
            raise APIException('Невозможно конвертировать одинаковые валюты')

        try:
            quote_ticker = keys[quote]
        except:
            raise APIException(f'Такой валюты "{quote}" нет в доступном списке валют')
        try:
            base_ticker = keys[base]
        except:
            raise APIException(f'Такой валюты "{base}" нет в доступном списке валют')
        try:
            amount_ticker = float(amount)
        except:
            raise APIException('Количество валюты не записано в виде числа')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        total_base = float(json.loads(r.content)[base_ticker]) * amount_ticker

        return total_base

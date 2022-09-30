import json
import requests

from config import currencies

# функция возвращает float(val) или False в случае, если val не число
def get_number(val):
    try:
        return float(val)
    except ValueError:
        return False


# исключения для функций и классов конвертации
class ConvertionException(Exception):
    pass


# класс с методом get_price для конвертации
class CryptoConverter:
    @staticmethod
    def get_price(base: str, quote: str, amount: str):

        try:
            base_ticker = currencies[base]
        except KeyError:
            raise ConvertionException('Неизвестный тип валюты: ' + base)

        try:
            quote_ticker = currencies[quote]
        except KeyError:
            raise ConvertionException('Неизвестный тип валюты: ' + quote)

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException('Неверно указано количество переводимой валюты')  # + amount

# запрос к API cryptocompare.com на конвертацию из quote_ticker в base_ticker
        req = requests.get(f"https://min-api.cryptocompare.com/data/price?fsym={base_ticker}&tsyms={quote_ticker}")
        content_json = json.loads(req.content)
#        print(content_json)

# получаем итоговую сумму перевода в указанную валюту
        total_quote = float(content_json[quote_ticker]) * float(amount)

        return total_quote



# токен созданного в телеграм бота
TELEBOT_TOKEN = "5513163029:AAHRc98CHlZbs9p7QbRtenBT-3Ove4iiRjk"

# валюты с тикетами
currencies = {
    'рубль': 'RUB',
    'доллар': 'USD',
    'евро': 'EUR',
    'фунт': 'GBP',
    'юань': 'CNY',
    'йена': 'JPY',
    'биткоин': 'BTC',
}

MSG_HELP = "Чтобы узнать стоимость одной валюты в единицах другой валюты, \
введите команду в формате:\n\n\
<имя валюты> <в какую валюту перевести (по умолчанию - рубль)> <количество переводимой валюты (по умолчанию - 1)>\n\n\
Примеры:\nбиткоин доллар 0.1\nдоллар 10\nевро доллар\nюань\n\n\
\
Узнать доступные валюты - команда /values\n\
Вывести справочную информацию - команда /help"

MSG_ERR_CURRENCY_NOT_SPECIFIED = "Не указан тип валюты"
MSG_ERR_UNKNOWN_CURRENCY_TYPE = "Неизвестный тип валюты"
MSG_ERR_INVALID_AMOUNT = "Неверно указано количество переводимой валюты"
MSG_ERR_INTERNAL_ERROR = "Произошла внутренняя ошибка при выполнении конвертации"

import telebot

from config import TELEBOT_TOKEN, currencies
from extensions import get_number, ConvertionException, CryptoConverter


# получаем ссылку на бот
bot = telebot.TeleBot(TELEBOT_TOKEN)


# обработчик для команд start и help
@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    bot.send_message(message.chat.id, "Чтобы начать работу, введите команду боту в формате:\n\
<имя валюты> <в какую валюту перевести (по умолчанию - рубль)> <количество переводимой валюты (по умолчанию - 1)>.\n\n\
Примеры: \nбиткоин доллар 0.1\nдоллар 10\nевро доллар\nюань\n\n\
Чтобы узнать доступные валюты, используйте команду /values")


# обработчик для команды values
@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:\n'
    for key in currencies.keys():
        text = text + "\n" + key

    bot.send_message(message.chat.id, text)


# обработчик для конвертации
@bot.message_handler(content_types=['text',])
def convert(message: telebot.types.Message):

    # обработка данных пользователя и связанных с ними ошибок (немного изменено, по сравнению с заданием)

    # перевод из одинаковой валюты можно не считать ошибкой
    # если параметров более чем 3, то ошибка не возникает, лишние параметры просто игнорируются
    # по умолчанию тип итоговой валюты - рубль, а количество валюты - 1, т.е. эти параметры можно не указывать
    # если вторым параметром идет число, то воспринимаем его как количество
    try:
        params = message.text.split(' ') # base quote amount

        if not len(params):
            raise ConvertionException('Не указан тип валюты')

        base = params[0]  # валюта из которой нужно конвертировать
        quote = 'рубль'  # валюта в которую нужно конвертировать
        amount = 1  # количечтво конвертируемой валюты

        # если всего 2 параметра, то второй параметр может быть как валютой, так и количеством
        if len(params) == 2:
            if get_number(params[1]) is False:
                quote = params[1]
            else:
                amount = params[1]

        if len(params) >= 3:
            quote = params[1]
            amount = params[2]

        total_quote = CryptoConverter.get_price(base, quote, amount)

# исключения наших обработциков
    except ConvertionException as error:
        bot.send_message(message.chat.id, str(error))

# остальные исключения
    except Exception as error:
        bot.send_message(message.chat.id, 'Произошла внутренняя ошибка при выполнении конвертации! ' + error)

    else:
        total_quote = round(total_quote, 2)

        text = f"{amount} {base} = {total_quote} {quote}"
        bot.send_message(message.chat.id, text)


# запускаем созданные обработчики для бота
bot.polling(none_stop=True)

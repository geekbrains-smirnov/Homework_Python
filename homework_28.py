from telegram import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler



bot = Bot(token='5983595001:AAEtJeQFlSpBTE4RBEGBben9kjzaJYVUEc0')
updater = Updater(token='5983595001:AAEtJeQFlSpBTE4RBEGBben9kjzaJYVUEc0')
dispahather = updater.dispatcher

A = 0
# B = 1



def start(update, context):
    logger(update, context)
    context.bot.send_message(update.effective_chat.id, 'Привет! Я ваш личный калькулятор😊 \nВведите данные для подсчета в формате "2+2, 2*2, 2/2"')
    # return A


def result(update, context):
    logger(update, context)
    text = update.message.text
    f = parse(text)
    g = calculate(f)
    context.bot.send_message(update.effective_chat.id, f'{text} = {g}')

    # return ConversationHandler.END

def parse(s):
    result = []
    digit = ""
    for symbol in s:
        if symbol.isdigit():
            digit += symbol
        else:
            result.append(float(digit))
            digit = ""
            result.append(symbol) 
    else:
        if digit:
            result.append(float(digit))
    return result


def calculate(lst):
    result = 0.0
    for s in lst:  
        if s == '*' or s == '/':
            if s == '*':
                index = lst.index(s)
                result = lst[index - 1] * lst[index + 1]
                lst = lst[:index - 1] + [result] + lst[index + 2:]
            else:
                index = lst.index(s)
                result = lst[index - 1] / lst[index + 1]
                lst = lst[:index - 1] + [result] + lst[index + 2:]
    for s in lst:  
        if s == '+' or s == '-':
            if s == '+':
                index = lst.index(s)
                result = lst[index - 1] + lst[index + 1]
                lst = lst[:index - 1] + [result] + lst[index + 2:]
            else:
                index = lst.index(s)
                result = lst[index - 1] - lst[index + 1]
                lst = lst[:index - 1] + [result] + lst[index + 2:]
    return result 


def logger(update, context):
    file = open('log.csv', 'a', encoding='utf_8')
    file.write(f'{update.effective_user.first_name}, {update.effective_user.id}, {update.message.text}\n')
    file.close()

    
def cancel(update, context):
    logger(update, context)
    context.bot.send_message(update.effective_chat.id, 'Прощай!')



start_handler = CommandHandler('start', start)
message_handler = MessageHandler(Filters.text, result)
# message_weather_handler = MessageHandler(Filters.text, weather)
message_cancel_handler = MessageHandler(Filters.text, cancel)


# conv_handler = ConversationHandler(entry_points=[start_handler],
                                #    states={A: [message_handler]},
                                #     fallbacks=[message_cancel_handler])


dispahather.add_handler(start_handler)
# dispahather.add_handler(conv_handler)
dispahather.add_handler(message_handler)
# dispahather.add_handler(message_weather_handler)
dispahather.add_handler(message_cancel_handler)


updater.start_polling()
updater.idle()
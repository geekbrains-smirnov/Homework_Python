from telegram import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler



bot = Bot(token='5983595001:AAEtJeQFlSpBTE4RBEGBben9kjzaJYVUEc0')
updater = Updater(token='5983595001:AAEtJeQFlSpBTE4RBEGBben9kjzaJYVUEc0')
dispahather = updater.dispatcher

A = 0
# B = 1



def start(update, context):
    context.bot.send_message(update.effective_chat.id, 'Введите текст для форматирования')
    return A


def filter_text(update, context):
    text = update.message.text
    f = list(text.split())
    print(type(text))
    n = 'абв'
    value = ' '.join(filter(lambda x: n not in x, f))
    context.bot.send_message(update.effective_chat.id, f'Готовый текст: {value}')

    return ConversationHandler.END
    
    
def cancel(update, context):
    context.bot.send_message(update.effective_chat.id, 'Прощай!')



start_handler = CommandHandler('start', start)
message_handler = MessageHandler(Filters.text, filter_text)
# message_weather_handler = MessageHandler(Filters.text, weather)
message_cancel_handler = MessageHandler(Filters.text, cancel)


conv_handler = ConversationHandler(entry_points=[start_handler],
                                   states={A: [message_handler]},
                                    fallbacks=[message_cancel_handler])


# dispahather.add_handler(start_handler)
dispahather.add_handler(conv_handler)
# dispahather.add_handler(message_handler)
# dispahather.add_handler(message_weather_handler)
# dispahather.add_handler(message_cancel_handler)


updater.start_polling()
updater.idle()


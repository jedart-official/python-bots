from config import*
from telegram import Update
from telegram import Bot
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler
from telegram.ext import Filters


def start(bot: Bot, update: Update):
    bot.send_message(
        chat_id = update.message.chat_id,
        text = "Привет",
    )

def send_text(bot: Bot, update: Update):
    text = update.message.text,
    bot.send_message(
        chat_id = update.message.chat_id,
        text = text,
    )


def main():
    bot = Bot(
        token = TOKEN,
    )
    updater = Updater(
        bot = bot, 
    )

    start_handler = CommandHandler("new", start)
    send_handler = MessageHandler(Filters.text, send_text)


    updater.dispatcher.add_handler(start_handler)
    updater.dispatcher.add_handler(send_handler)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()


#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This program is dedicated to the public domain under the CC0 license.

#Roundone: the basic conversation
#methods: the conversation involving api,sql and Natural

import logging
from coulsontoken import mytoken

from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters,
                          ConversationHandler)
from telegram import chat

import telegram
import Responses
import api_method

response, phrase = {}, {}


# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

Roundone, Destination, Wrap = range(3)

bot = telegram.Bot(mytoken)


def start(update, context):

    update.message.reply_text('Hi bro, Anything I can help you?')
    return Roundone


def conone(update, context):
    user = update.message.from_user
    Onefinish = Responses.check_end(update.message.text)
    if Onefinish or update.message.text == "What can you do?":
        update.message.reply_text("Let's get start the real one!")
        return Destination
    response = Responses.match_reply(update.message.text)
    update.message.reply_text(response)
    return Roundone




def contwo(update, context):
    user = update.message.from_user
    update.message.reply_text("https://bit.ly/2ZAq7nj ")


    #bot.send_message(chat_id='1283099852',text="Sorry, but I don't get your destination")
    # update.message.reply_text('Under nowadays circumstances, this is my duty to remind you that ')
    # update.message.reply_text(api_method.covid_19info(des, 'confirmed'))
    # update.message.reply_text(api_method.covid_19info(des, 'recovered'))
    # update.message.text("Safety is the priority")

    bot.send_photo(chat_id='1283099852', photo=('https://www.thecocktaildb.com/images/media/drink/5noda61589575158.jpg'))

    bot.send_photo(chat_id='1283099852', photo=open("/Users/coulson/Desktop/Travel_bot/weather.png", 'rb'))
    return Destination



def cancel(update, context):
    user = update.message.from_user
    logger.info("User %s canceled the conversation.", user.first_name)
    update.message.reply_text('Looking forward to help you again!',
                              reply_markup=ReplyKeyboardRemove())

    return ConversationHandler.END


def main():
    updater = Updater(mytoken, use_context=True)
    dp = updater.dispatcher
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],

        states={
            Roundone: [MessageHandler(Filters.text, conone)],

            Destination: [MessageHandler(Filters.text, contwo)],

            Wrap: [MessageHandler(Filters.text, contwo)]
        },

        fallbacks=[CommandHandler('end', cancel)]
    )

    dp.add_handler(conv_handler)

    # Start the Bot
    updater.start_polling()
    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

if __name__ == '__main__':
    main()
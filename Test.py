

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

Roundone, Methods, Wrap = range(3)

bot = telegram.Bot(mytoken)


def start(update, context):

    update.message.reply_text('Hi bro, Anything I can help you?')
    bot.send_photo
    return Roundone


def conone(update, context):
    user = update.message.from_user
    Onefinish = Responses.check_end(update.message.text)
    if Onefinish or update.message.text == "What can you do?":
        update.message.reply_text("Let's get start the real one!")
        return Methods
    response = Responses.match_reply(update.message.text)
    update.message.reply_text(response)
    return Roundone




def contwo(update, context):
    user = update.message.from_user
    update.message.reply_text("I'm now your private travel advisor and I"
                              " can offer you infomation about weather of "
                              "the detination, Covid_19 uptodate info "
                              "and the hotel search for you! \n"
                              "Can you tell me where are you heading? ")
    update.message.reply_text(api_method.covid_19info('US','deaths'))
    bot.send_photo(chat_id='1283099852', photo=open("/Users/coulson/Desktop/Travel_bot/weather.png", 'rb'))
    return Methods



def cancel(update, context):
    user = update.message.from_user
    logger.info("User %s canceled the conversation.", user.first_name)
    update.message.reply_text('Looking forward to help you again!',
                              reply_markup=ReplyKeyboardRemove())

    return ConversationHandler.END


def main():
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater(mytoken, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Add conversation handler with the states GENDER, PHOTO, LOCATION and BIO
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],

        states={
            Roundone: [MessageHandler(Filters.text, conone)],

            Methods: [MessageHandler(Filters.text, contwo)],

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
import Responses
import api_method
import Natural
import sql_method
import os
from PIL import Image
import time
finished = False
not_first = False
response, phrase = {}, {}
destination = ''
city = ''
INIT=0
AUTHED=1
DONE = 2

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

Roundone, Roundtwo, Roundthree, Roundfour, Roundfive, flight, near_city, air_info, airticket, \
    weather_info, check_new, Last = range(12)

bot = telegram.Bot(mytoken)

print("ready")
def start(update, context):

    update.message.reply_text('Hi bro, Anything I can help you?')
    return Roundone


def conone(update, context):
    user = update.message.text
    Onefinish = Responses.check_end(user)
    if Onefinish or update.message.text == "What can you do?":
        update.message.reply_text("Can you tell me which country you are heading?")
        return Roundtwo
    response = Responses.match_reply(user)
    update.message.reply_text(response)
    return Roundone



# country record
def country(update, context):
    destination = Responses.check_country(update.message.text)
    if destination != None:
        update.message.reply_text("sure, I get it")
        update.message.reply_text('And the name of the city you are heading?')
        # print('The value of destination =: ', end="")
        # print(destination)
        return Roundthree
    update.message.reply_text("Sorry, I do not get this country")
    return Roundtwo

def city(update, context):
    user = update.message.text
    if Responses.check_city(user):
        country = 'CN'
        print('country variable is: ', end="")
        print(country)
        update.message.reply_text("ok, I have it")
        update.message.reply_text('Under nowadays circumstances, this is my duty to remind you that ')
        update.message.reply_text(api_method.covid_19info(country, 'confirmed'))
        update.message.reply_text("Safety is always the priority")
        return Roundfour
    else:
        update.message.reply_text("Sorry, I do not find the city. Can you please check your spelling?")
        return Roundthree
def part3(update, context):
    message = update.message.text
    if message == "done":
        update.message.reply_text("Sure, I'm your drinking advisor now")
        return Roundfive
    if Natural.intent_identify(message) == "thankyou":
        update.message.reply_text("My pleasure")
        return Roundfour

    elif Natural.intent_identify(message) == 'flatter':
        update.message.reply_text("I'm flattered")
        return Roundfour

    elif Natural.intent_identify(message) == 'ask_function':
        update.message.reply_text("I can check the flight related info")
        update.message.reply_text("Show you the weather temperature forecast")
        update.message.reply_text("And a wine commendation for you")
        return Roundfour

    elif Natural.intent_identify(message) == 'search_flight':
        update.message.reply_text("Sure")
        for i in Responses.show_flight():
            update.message.reply_text(i)
        return flight

    elif Natural.intent_identify(message) == 'weather_search':
        update.message.reply_text('Just to make sure, you want to check the weather of your destination city, right?')
        return weather_info

    elif Natural.intent_identify(message) == 'wine_search':
        update.message.reply_text("Sure, I'm your drinking advisor now")
        return Roundfive

    else:
        update.message.reply_text("Any thing else I can do for you?")

def weather_forecast(update, context):
    msg = update.message.text
    if Natural.intent_identify(msg) == 'affirm':
        bot.send_photo(chat_id='1283099852', photo=open("/Users/coulson/Desktop/Travel_bot/weather.png", 'rb'))
        return Roundfour
    else:
        update.message.reply_text("Please tell me the name of city you want to check")
        return check_new

def new_city(update, context):
    newcity = update.message.text
    if Responses.check_city(newcity):
        api_method.weather2table(newcity)
        bot.send_photo(chat_id='1283099852', photo=open("/Users/coulson/Desktop/Travel_bot/weather.png", 'rb'))
        return Roundfour
    else:
        update.message.reply_text('Sorry, but I do not find a city based on the name you entered, another try?')
        return check_new

def flight_search(update, context):
    print('The flight search function entered')
    message = update.message.text
    if message == 'done':
        update.message.reply_text("I can help you with flight, weather or drink!")
        return Roundfour
    if 'city' in message:
        update.message.reply_text("Sure, please tell me the city you're looking for:")
        return near_city

    if 'information' in message:
        update.message.reply_text("No problem, please tell me the code of the airport you want to check!")
        return air_info

    if 'flight' in message:
        update.message.reply_text("I handle it, tell me where you are heading and the date(MM-DD) of your departure, as well as departure location")
        return airticket

    else:
        update.message.reply_text("Sorry, I do not get your intention. Can you repharse it?")
        return flight

def city_search(update, context):
    print('Enter the city search function')
    msg = update.message.text
    result = api_method.airport_finder(msg)
    update.message.reply_text(result)
    return flight

def info_search(update, context):
    print('Enter the information function')
    aircode = update.message.text
    result = api_method.airport_info(aircode)
    update.message.reply_text(result)
    return flight

def ticket_search(update, context):
    print('Enter the ticket search function')
    raw_message = update.message.text
    print('The raw message is:')
    print(raw_message)
    print(Responses.code_date(raw_message))
    if len(Responses.code_date(raw_message)) != 3:
        update.message.reply_text("I need the code of both airport and your departure date(MM-DD) to find ticket for you")
    else:
        info = Responses.code_date(raw_message)
        update.message.reply_text("One sec")
        result = api_method.flight_price(info[0], info[1], info[2])
        update.message.reply_text(result)
    return flight



def wine(update, context):
    msg = update.message.text
    params = {}
    neg_params = {}
    result = sql_method.search_wine(msg, params, neg_params)
    if msg == "get it":
        return Last
    update.message.reply_text(result)
    return Roundfive


def finalone(update, context):
    update.message.reply_text("You have a good one! Looking forward to help you again! It's really my pleasure")
    return ConversationHandler.END


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

            Roundtwo: [MessageHandler(Filters.text, country)],

            Roundthree: [MessageHandler(Filters.text, city)],

            Roundfour: [MessageHandler(Filters.text, part3)],

            flight: [MessageHandler(Filters.text, flight_search)],
            near_city: [MessageHandler(Filters.text, city_search)],
            air_info: [MessageHandler(Filters.text, info_search)],
            airticket: [MessageHandler(Filters.text, ticket_search)],

            weather_info: [MessageHandler(Filters.text, weather_forecast)],
            check_new: [MessageHandler(Filters.text, new_city)],

            Roundfive: [MessageHandler(Filters.text, wine)],

            Last: [MessageHandler(Filters.text, finalone)],
        },
#near_city, air_info, airticket
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
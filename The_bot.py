import Responses
import api_method
import Natural
import sql_method
import os
from PIL import Image

finished = False
not_first = False
response, phrase = {}, {}
destination = None
city = ''
INIT=0
AUTHED=1
DONE = 2


##part one: the basic conversation

#While loop take charge of basic/first round question and answers
while (True):
    if not_first:
        finished, message = Responses.receive_input("Any thing else I can do for you?")
        if finished:
            break
        print(Responses.user_word(message))
    else:
        finished, message = Responses.receive_input("Hi bro. Any thing to help you?")
        print(Responses.user_word(message))
      #initial response & phrase for the match_reply works
    if message == "What can you do?":
        break

    response = Responses.match_reply(message)
    print(Responses.bot_res(response))

    not_first = True if not_first == False else True #test the 2nd and future greeting words

## part two: higher level conversation
print(Responses.bot_res("I can chose the suitable flight ticket for you. \n "))

## certain the country and city detination
while(True):
    message = input("Can you tell me which country you are heading? \n")
    destination = Responses.check_country(message)
    if destination != None:
        print(Responses.bot_res('Sure, I get it \n'))
        break
    print(Responses.bot_res("Sorry, I do not get it. Can you rephase it?"))
while(True):
    message = input("And the name of city you are heading? \n")
    if Responses.check_city(message):
        city = message
        print(Responses.bot_res("Good place to go!"))
        break
    print(Responses.bot_res('Sorry, I do not find this city. Can you please check your spell?'))


print(Responses.bot_res('To remind and for your safety'))
print(Responses.bot_res(api_method.covid_19info(destination.upper(), 'confirmed')))
print(Responses.bot_res('For the safety priority \n'))

# weather, flight and wine recommendation
#part3
while(True):
    message = input()
    if message == "done":
        break
    if Natural.intent_identify(message) == 'thankyou':
        print(Responses.bot_res('My pleasure'))
    elif Natural.intent_identify(message) == 'flatter':
        print(Responses.bot_res("I'm flattered"))
    elif Natural.intent_identify(message) == 'ask_function':
        print(Responses.bot_res('I can check the flight related info\n'
                                'Show you the weather temperature forecast\n'
                                'And a wine commendation for you'))

    elif Natural.intent_identify(message) == 'search_flight':
        print(Responses.bot_res("sure"))
        for i in Responses.show_flight():
            print(Responses.bot_res(i))
            while(True):
                message = input()
                if message == "done":
                    print(Responses.bot_res("I can help you with flight, weather or drink!"))
                    break
                if "city" in message.lower():
                    city_name = input(Responses.bot_res("Sure, please tell me the city you're looking for:\n"))
                    result = api_method.airport_finder(city_name)
                    print(Responses.bot_res(result))
                if "information" in message.lower():
                    air_code = input(Responses.bot_res('No problem, please tell me the code of airport you want to check\n'))
                    result = api_method.airport_info(air_code)
                    print(Responses.bot_res(result))
                if 'flight' in message.lower():
                    raw_message = input("I handle it, tell me where you are heading and the date(MM-DD) of your departure, as well as"
                                        "departure location\n")
                    if len(Responses.code_date(raw_message)) != 3:
                        print(Responses.bot_res("I need the code of both airport and your departure date(MM-DD) to find ticket for you\n"))
                    else:
                        info = Responses.code_date(raw_message)
                        print(api_method.flight_price(info[0], info[1], info[2]))
                else:
                    print(Responses.bot_res("Sorry, I do not get your intention. Can you repharse it?\n"))

    elif Natural.intent_identify(message) == 'weather_search':
        print(Responses.bot_res('Just to make sure, you want to check the weather '
                                'temperature forecast in ' + city + "?"))
        if Natural.intent_identify(input()) == 'affirm':
            #return 图片
            print('Show picture:')
            f = Image.open('weather.png')
            f.show()

        else:
            while(True):
                print(Responses.bot_res("Please tell me the name of city you "
                                        "want to check\n"))
                newcity = input()
                if Responses.check_city(newcity):
                    api_method.weather2table(newcity)
                    print('Show picture:')
                    f = Image.open('weather.png')
                    f.show()
                    break
                print(Responses.bot_res('Sorry, but I do not find a city based'
                                        'on the name you entered\n'))

    elif Natural.intent_identify(message) == 'wine_search':
        break
    else:
        print(Responses.bot_res("Any thing else I can do for you?"))

##part4: the wine menu recommendation
print(Responses.bot_res("I'm your wine advisor now\n What can I get for you?"))
status = INIT
param = {}
neg_param = {}
while(True):
    message = input()
    intent = sql_method.interpret(message)
    ## reset the condition to find another wine
    if message == "reset":
        param = {}
        neg_param = {}
    status = sql_method.wine_mes(status, intent)
    if intent == "done":
        break
    if status == AUTHED:
        while(True):
            mes = input()
            # enter get to get out of the one_wine search
            if mes == "get":
                print(Responses.bot_res('Finish order'))
                break
            print(Responses.bot_res(sql_method.search_wine(mes, param, neg_param)))
print("get out of the loop")


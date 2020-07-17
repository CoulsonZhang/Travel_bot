import Responses
import api_method
import Natural

finished = False
not_first = False
response, phrase = {}, {}
destination = None
city = 'champaign'
#todo: initilize the city for debuging


#Status one: the basic conversation

#While loop take charge of basic/first round question and answers
# while (True):
#     if not_first:
#         finished, message = Responses.receive_input("Any thing else I can do for you?")
#         if finished:
#             break
#         print(Responses.user_word(message))
#     else:
#         finished, message = Responses.receive_input("Hi bro. Any thing to help you?")
#         print(Responses.user_word(message))
#       #initial response & phrase for the match_reply works
#     if message == "What can you do?":
#         break
#
#     response = Responses.match_reply(message)
#     print(Responses.bot_res(response))
#
#     not_first = True if not_first == False else True #test the 2nd and future greeting words


print(Responses.bot_res("I can chose the suitable flight ticket for you. \n "))


# while(True):
#     message = input("Can you tell me which country you are heading? \n")
#     destination = Responses.check_country(message)
#     if destination != None:
#         print(Responses.bot_res('Sure, I get it \n'))
#         break
#     print(Responses.bot_res("Sorry, I do not get it. Can you rephase it?"))
# while(True):
#     message = input("And the name of city you are heading? \n")
#     if Responses.check_city(message):
#         city = message
#         print(Responses.bot_res("Good place to go!"))
#         break
#     print(Responses.bot_res('Sorry, I do not find this city. Can you please check your spell?'))
#
#
# print(Responses.bot_res('To remind and for your safety'))
# print(Responses.bot_res(api_method.covid_19info(destination.upper(), 'confirmed')))
# print(Responses.bot_res('For the safety priority \n'))

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
            #todo: the api flight function implement
    elif Natural.intent_identify(message) == 'weather_search':
        print(Responses.bot_res('Just to make sure, you want to check the weather'
                                'temperature forecast in ' + city + "?"))
        if Natural.intent_identify(input()) == 'affirm':
            #return 图片
            print('老图片')
        else:
            while(True):
                print(Responses.bot_res("Please tell me the name of city you "
                                        "want to check"))
                newcity = input()
                if Responses.check_city(newcity):
                    api_method.weather2table(newcity)
                    print('新图片')
                    break
                print(Responses.bot_res('Sorry, but I do not find a city based'
                                        'on the name you entered'))

    elif Natural.intent_identify(message) == 'wine_search':
        break
    else:
        print(Responses.bot_res("Any thing else I can do for you?"))

message = input(Responses.bot_res("Please tell me what kind of drink you want"))



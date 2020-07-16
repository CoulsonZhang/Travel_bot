import Responses
import api_method

finished = False
not_first = False
response, phrase = {}, {}
destination = None
city = None


#Status one: the basic conversation

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


print(Responses.bot_res("I can chose the suitable flight ticket for you. \n "))


while(True):
    message = input("Can you tell me which country you are heading? \n")
    destination = Responses.check_country(message)
    if destination != None:
        print(Responses.bot_res('Sure, I get it \n'))
        break
    print(Responses.bot_res("Sorry, I do not get it. Can you rephase it?"))
while(True):
    message = input("And the name of city you are heading?")
    if Responses.check_city(message):
        city = message
        print(Responses.bot_res("Good place to go!"))
        break
    print(Responses.bot_res('Sorry, I do not find this city. Can you please check your spell?'))


# print(Responses.bot_res('To remind and for your safety'))
# print(Responses.bot_res(api_method.covid_19info(destination.upper(), 'confirmed')))
# print(Responses.bot_res('For the safety priority \n'))







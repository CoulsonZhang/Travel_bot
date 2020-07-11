from Responses import reply
import Responses


message = input(Responses.bot_res("Hi bro. Any thing to help you? \n"))
print(Responses.user_word(message))


not_first = False
while (True):
    if not_first:
        message = input(Responses.bot_res("Anything else I can do for you ? \n"))
        if Responses.check_end(message):
            break
        print(Responses.user_word(message))
    response, phrase = Responses.match_reponse(reply, message)



    print(Responses.bot_res(response))

    message = input(Responses.bot_res("Ready for your words \n"))
    print(Responses.user_word(message))
    response, phrase = Responses.match_reponse(reply, message)
    print(Responses.bot_res(response))

    not_first = True if not_first == False else True
    print(Responses.bot_res('One round done'))

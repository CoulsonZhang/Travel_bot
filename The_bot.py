from Responses import reply
import Responses


message = input(Responses.bot_res("Hi bro. Any thing to help you? \n"))
print(Responses.user_word(message))

finished = False
not_first = False
while (True):
    if not_first:
        finished, message = Responses.receive_input("Any thing else I can do for you?")
        if finished:
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

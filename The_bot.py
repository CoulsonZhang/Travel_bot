import Responses
import Natural

finished = False
not_first = False
response, phrase = {}, {}

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
    response = Responses.match_reply(message)
    print(Responses.bot_res(response))

    not_first = True if not_first == False else True #test the 2nd and future greeting words


# 7.11 finished basic conversation loop
# memo: substitution need a more advanced function for the 'me'
#       'you' changes.


# To do: using the spacy to process the language
# To do: search the info through the rapid API

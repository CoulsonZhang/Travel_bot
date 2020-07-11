#This is the first round Q&A part
#Take charge of basic reply, matching of regex and default reply

import re
import random

bot_template = "BOT : {0}"
user_template = "USER : {0}"

finish_word = {"That's it", "Good to go", "Thanks for your help", "I'm done", "end"}

default = ["I didn't get that. Can you say it again?",
                  "I missed what you said. What was that?",
                  "Sorry, could you say that again?",
                  "Sorry, I didn't get that. Can you rephrase?",
                  "Sorry, what was that?",
                  "One more time?",
                  "Say that one more time?",
                  "I didn't get that. Can you repeat?",
                  "I missed that, say that again?",
                  ]

reply = {'I need(.*)': ['Any assitance I can do to help you get{0}?',
                           'How can I do to help you get{0}?',
                           "What's stopping you from getting{0}?"],
           'can you tell (.*) (hotel|airport|flight)(.*)': ['I can definitely search that for you',
                                    "Sure I can do that",
                                    'No problem',
                                    'Sure!'],
           'How are you(.*)': ['Great!',
                                "I'm doing great as a chat bot"],
           '^(Hi|hi|Hello|hello)': ['Hello my friend, how can I help you',
                            "Hi, how are doing today?",
                            'Greeting! Any assiantance I can offer you?'
                          ]
           }

def receive_input(promp):
    message = input(bot_res(promp + "\n"))
    if check_end(message):
        print(bot_res("Looking forward to help you again"))
        return True, message
    else:
        return False, message

def check_end(message):
    for msg in finish_word:
        if msg in message:
            return True
    return False

def bot_res(message):
    return bot_template.format(message)

def user_word(message):
    return user_template.format(message)

def replace_pron(message):
    message = message.lower()
    if ' me' in message:
         message = re.sub(' me', ' you', message)
    if ' my ' in message:
         message = re.sub(' my ', ' your ', message)
    return message
def match_reponse(rules, message):
    response, phrase = random.choice(default), None
    for key in rules:
        match = re.search(key, message)
        if match is not None:
            response = random.choice(rules[key])
            if '{0}' in response:
                phrase = re.search(key, message).group(1)
    return response, phrase

def match_reply(message):
    response, phrase = match_reponse(reply, message)
    if '{0}' in response:
        phrase = replace_pron(phrase)
        response = response.format(phrase)
    return response

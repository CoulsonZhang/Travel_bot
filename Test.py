import re
import Responses
INIT=0
AUTHED=1
DONE = 2

category = ['Ordinary Drink', 'Cocktail', 'Milk / Float / Shake', 'Other/Unknown', 'Cocoa',
            'Shot', 'Coffee / Tea', 'Homemade Liqueur', 'Punch / Party Drink',
            'Beer', 'Soft Drink / Soda']

alcoho = ['Alcoholic', 'Non alcoholic', 'Optional alcohol']

glass = ['Highball glass', 'Cocktail glass', 'Old-fashioned glass', 'Collins glass',
         'Pousse cafe glass', 'Champagne flute', 'Whiskey sour glass', 'Brandy snifter',
         'White wine glass', 'Nick and Nora Glass', 'Hurricane glass', 'Coffee mug', 'Shot glass',
         'Jar', 'Irish coffee cup', 'Punch bowl', 'Pitcher', 'Pint glass', 'Copper Mug', 'Wine Glass',
         'Cordial glass', 'Beer mug', 'Margarita/Coupette glass', 'Beer pilsner', 'Beer Glass', 'Parfait glass',
         'Mason jar', 'Margarita glass', 'Martini Glass', 'Balloon Glass', 'Coupe Glass']

wine_pattern = {
    (INIT, 'ask_duty'): (INIT, "I know more than 550+ drinks and I believe there are few for you!"),
    (INIT, 'ask_cate'): (INIT, 'I have but not limited to cocktail, shot, coffee, party drink, beer and'
                               'soda menu for you to choose'),
    (INIT, 'ask_alco'): (INIT, "I have alcoholic, non_alcoholic, and optional alcoholic drinks"),
    (INIT, 'ask_glass'): (INIT, "I have but not limited to Highball glass, Pint glass, champagne glass, Whiskey sour glass"
                                " Punch bowl, Beer mug, Mason jar, etc."),
    (INIT, 'authorized'): (AUTHED, "You can now tell me what you expect and not"),
    (INIT, 'not_authorized'): (INIT, "Sorry, you have to show your legality of drink to unlock the wine menu"),
    (AUTHED, 'detail'): (AUTHED, "No problem"),
    #todo: check the individual information of the drink
    (AUTHED, 'done'): (INIT, "Don't forget to leave a feedback for me!"),
    (AUTHED, 'no_info'): (AUTHED, "Say that again? "),
    (AUTHED, 'another'): (INIT, "No problem, tell me your request"),
    (INIT, 'no_info'): (INIT, "Sorry, can you rephrase?"),
    (INIT, 'done'): (INIT, "See you next time.")
}

def interpret(message):
    msg = message.lower()
    if "do you have" in msg:
        return 'ask_duty'
    if 'category' in msg:
        return 'ask_cate'
    if 'alcohol' in msg:
        return 'ask_alco'
    if 'glass' in msg:
        return 'ask_glass'
    if re.search('\d\d', msg):
        if int(re.findall('\d\d',msg)[0]) >= 21:
            return 'authorized'
        else:
            return 'not_authorized'
    if 'information' in msg:
        return 'detail'
    if 'done' in msg:
        return 'done'
    if 'another' in msg:
        return 'another'
    return "no_info"

def wine_mes(status, message):
    new_status, response = wine_pattern[(status, message)]
    print(Responses.bot_res(response))
    return  new_status

print('Go')
status = INIT
while(True):
    intent = interpret(input())
    status = wine_mes(status, intent)
    if intent == "done":
        break
print("get out of the loop")
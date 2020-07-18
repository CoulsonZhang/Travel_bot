import sqlite3
import random
import api_method
import re
import Responses
INIT=0
AUTHED=1
DONE = 2


wishes = [
    'Hope you have a good day',
    'Enjoy your day ',
    'Wish you have a good night',
    "Enjoy your drink!",
    "That's it"
]

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
    (INIT, 'ask_duty'): (INIT, "I know more than 550+ drinks and I believe there are few for you!\n"),
    (INIT, 'ask_cate'): (INIT, 'I have but not limited to cocktail, shot, coffee, party drink, beer and'
                               'soda menu for you to choose\n'),
    (INIT, 'ask_alco'): (INIT, "I have alcoholic, non_alcoholic, and optional alcoholic drinks\n"),
    (INIT, 'ask_glass'): (INIT, "I have but not limited to Highball glass, Pint glass, champagne glass, Whiskey sour glass"
                                " Punch bowl, Beer mug, Mason jar, etc.\n"),
    (INIT, 'not_authorized'): (INIT, "Sorry, you have to show your legality of drink to unlock the wine menu\n"),
    (INIT, 'authorized'): (AUTHED, "You can now tell me what you expect and not\n"),
    (AUTHED, 'detail'): (AUTHED, "No problem\n"),
    (AUTHED, 'done'): (INIT, "Don't forget to leave a feedback for me!\n"),
    (AUTHED, 'no_info'): (AUTHED, "Say that again?\n"),
    (AUTHED, 'another'): (INIT, "No problem, tell me your request\n"),
    (INIT, 'no_info'): (INIT, "Sorry, can you rephrase?\n"),
    (INIT, 'done'): (INIT, "See you next time.\n")
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

def find_ID(name):
    conn = sqlite3.connect("Winetable.db")
    c = conn.cursor()
    c.execute("SELECT ID FROM Winetable WHERE Name = '" + name + "'")
    return c.fetchall()[0][0]

def find_wine(params, neg_params):
    query = 'SELECT * FROM Winetable'
    if len(params) > 0 and len(neg_params) > 0:
        filters = ["{}=?".format(k) for k in params] + ["{}!=?".format(k) for k in neg_params]
        query += " where " + " and ".join(filters)
    elif len(params) > 0:
        filters = ["{}=?".format(k) for k in params]
        query += " where " + " and ".join(filters)
    elif len(neg_params) > 0:
        filters = ["{}!=?".format(k) for k in neg_params]
        query += " where " + " and ".join(filters)
    #t = tuple(dict(list(params.items()) + list(neg_params.items())).values())
    t = tuple(params.values()) + tuple(neg_params.values())
    # print(params)
    # print(neg_params)
    # print('The value of t: ', end="")
    # print(t)
    # print('The value of query: ', end="")
    # print(query)
    conn = sqlite3.connect("Winetable.db")
    c = conn.cursor()
    c.execute(query, t)
    return c.fetchall()



def search_wine(message, params, neg_params):
    negate = ("not" or "n't") in message
    for i in category:
        if i.lower() in message.lower():
            if negate:
                neg_params['Categories'] = i
            else:
                params['Categories'] = i

    for j in alcoho:
        if j.lower() in message.lower():
            if negate:
                neg_params['Alcoholic'] = j
            else:
                params['Alcoholic'] = j

    for x in glass:
        if x.lower() in message.lower():
            if negate:
                neg_params['Glass'] = x
            else:
                params['Glass'] = x
    result_wine = find_wine(params, neg_params)
    # print(len(result_wine))
    if len(result_wine) == 0:
        return "Your requirement is really special, I do not have something like that"

    if len(result_wine) == 1:
        ins, url = api_method.wine_detail(find_ID(result_wine[0][1]))
        return '{} is the only option for your unique request\n'.format(result_wine[0][1]) + url + '\n' +"I suggest you enjoy with following steps: \n"+ ins
    else:
        result = random.choice(result_wine)[1]
        ins, url = api_method.wine_detail(find_ID(result))
        return "Have a try with {}! \n".format(result) + random.choice(wishes) + "\n" + url + '\n'+"I suggest you enjoy with following steps: \n" + ins



# param = {}
# no = {}
# print(search_wine('I want an alcoholic', param, no))
# print(search_wine('not ordinary drink', param, no))

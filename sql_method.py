import sqlite3
import random

conn = sqlite3.connect('Winetable.db')
c = conn.cursor()

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
    print(params)
    print(neg_params)
    print('The value of t: ', end="")
    print(t)
    print('The value of query: ', end="")
    print(query)
    conn = sqlite3.connect("Winetable.db")
    c = conn.cursor()
    c.execute(query, t)
    return c.fetchall()



def search_wine(message, params, neg_params):
    negate =  ("not"  or "n't") in message
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
    print(len(result_wine))
    if len(result_wine) == 0:
        return "Your requirement is really special, I do not have something like that"
    if len(result_wine) == 1:
        return '{} is the only option for your unique request'.format(result_wine[0][1])
    else:
        result = random.choice(result_wine)[1]
        return "Have a try with {}! \n".format(result) + random.choice(wishes)


param = {}
no = {}
print(search_wine('I want an alcoholic', param, no))
print(search_wine('not ordinary drink', param, no))
# print(search_wine('not  glass', param, no))

#todo: negation
#todo: status
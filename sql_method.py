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

def find_wine(params):
    query = 'SELECT * FROM Winetable'
    if len(params) > 0:
        filters = ["{}=?".format(k) for k in params]
        query += " where " + " and ".join(filters)
    t = tuple(params.values())
    conn = sqlite3.connect("Winetable.db")
    c = conn.cursor()
    c.execute(query, t)
    return c.fetchall()

def search_wine(message, params):
    for i in category:
        if i.lower() in message.lower():
            params['Categories'] = i
    for j in alcoho:
        if j.lower() in message.lower():
            params['Alcoholic'] = j
    for x in glass:
        if x.lower() in message.lower():
            params['Glass'] = x
    result_wine = find_wine(params)
    print(len(result_wine))
    if len(result_wine) == 0:
        return "Your requirement is really special, I do not have something like that"
    if len(result_wine) == 1:
        return '{} is the only option for your unique request'.format(result_wine[0][1])
    else:
        result = random.choice(result_wine)[1]

        return "Have a try with {}! \n".format(result) + random.choice(wishes)


param = {}
print(search_wine('I want an non alcoholic cocktail in  glass', param))

#todo: negation
#todo: status
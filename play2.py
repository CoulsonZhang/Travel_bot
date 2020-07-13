list = [{'ID': '11391', 'Name': 'Frozen Pineapple Daiquiri', 'Categories': 'Ordinary Drink', 'Alcoholic': 'Alcoholic', 'Glass': 'Cocktail Glass', 'Ingredient': 'Light rum, Light rum, Pineapple, Lime juice'},
{'ID': '11987', 'Name': 'Queen Bee', 'Categories': 'Ordinary Drink', 'Alcoholic': 'Alcoholic', 'Glass': 'Cocktail glass', 'Ingredient': 'Coffee brandy, Coffee brandy, Lime vodka'},
{'ID': '17833', 'Name': 'A. J.', 'Categories': 'Ordinary Drink', 'Alcoholic': 'Alcoholic', 'Glass': 'Cocktail glass', 'Ingredient': 'Applejack, Applejack'},
]

idlist = []
new_list = []
for lst in list:
    if lst["ID"] not in idlist:
        idlist.append(lst["ID"])
        new_list.append(lst)


for i in new_list:
    print(i)

print('There are ' + str(len(new_list)) + ' out of ' + str(len(list)) + ' items')

for j in new_list:
    old = "'" + str(j['ID']) + "'"
    wanted = "c.execute(\"INSERT INTO Winetable(ID, Name, Categories, Alcoholic, Glass, Ingredient) VALUES (" \
             + str(j.values())[13:-2].replace(old, j['ID']) + ")\""
    print(wanted)
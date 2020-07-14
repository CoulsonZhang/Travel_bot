import http.client
import json
conn = http.client.HTTPSConnection("the-cocktail-db.p.rapidapi.com")
dic = {}
list = []
for i in range(2000):

    headers = {
        'x-rapidapi-host': "the-cocktail-db.p.rapidapi.com",
        'x-rapidapi-key': "acb7b42f91msh89c86e1c983ae20p16617fjsn5f8e27b3cbdb"
        }

    conn.request("GET", "/random.php", headers=headers)

    res = conn.getresponse()
    data = res.read().decode("utf-8")
    test = json.loads(data)
    #print(test)
    dic['ID'] = test['drinks'][0]['idDrink']
    dic['Name'] = test['drinks'][0]['strDrink']
    dic['Categories'] = test['drinks'][0]['strCategory']
    dic['Alcoholic'] = test['drinks'][0]['strAlcoholic']
    dic['Glass'] = test['drinks'][0]['strGlass']
    dic['Ingredient'] = test['drinks'][0]['strIngredient1']
    for i in range(14):
        if test['drinks'][0]['strIngredient' + str(i+2)] != None:
            dic['Ingredient'] += ((', ') + test['drinks'][0]['strIngredient' + str(i+1)])

    print(dic, end="")
    print(",")
    #print()

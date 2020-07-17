import http.client
import json

conn = http.client.HTTPSConnection("the-cocktail-db.p.rapidapi.com")

headers = {
    'x-rapidapi-host': "the-cocktail-db.p.rapidapi.com",
    'x-rapidapi-key': "acb7b42f91msh89c86e1c983ae20p16617fjsn5f8e27b3cbdb"
    }

conn.request("GET", "/list.php?g=list", headers=headers)

res = conn.getresponse()
data = res.read()
test = json.loads(data)
for i in test["drinks"]:
    print("'" + i['strGlass'] + "', ", end="")
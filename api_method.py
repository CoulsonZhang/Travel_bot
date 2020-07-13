import http.client
import json


def Covid_19info(country, type):
    conn = http.client.HTTPSConnection("covid-19-data.p.rapidapi.com")

    headers = {
        'x-rapidapi-host': "covid-19-data.p.rapidapi.com",
        'x-rapidapi-key': "acb7b42f91msh89c86e1c983ae20p16617fjsn5f8e27b3cbdb"
    }

    conn.request("GET", "/country/code?format=json&code=" + country, headers=headers)

    res = conn.getresponse()
    data = res.read().decode("utf-8")
    test = json.loads(data)
    print('The value of ' + type + ' in '+ country+' is: ')
    print(test[0][type])


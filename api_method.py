import http.client
import json
import matplotlib.pyplot as plt
import time

def wine_detail(ID):
    conn = http.client.HTTPSConnection("the-cocktail-db.p.rapidapi.com")

    headers = {
        'x-rapidapi-host': "the-cocktail-db.p.rapidapi.com",
        'x-rapidapi-key': "acb7b42f91msh89c86e1c983ae20p16617fjsn5f8e27b3cbdb"
        }

    conn.request("GET", "/lookup.php?i=" + str(ID), headers=headers)

    res = conn.getresponse()
    data = res.read()
    test = json.loads(data)
    return test['drinks'][0]['strInstructions'], test['drinks'][0]['strDrinkThumb']


def covid_19info(country, type):
    conn = http.client.HTTPSConnection("covid-19-data.p.rapidapi.com")

    headers = {
        'x-rapidapi-host': "covid-19-data.p.rapidapi.com",
        'x-rapidapi-key': "acb7b42f91msh89c86e1c983ae20p16617fjsn5f8e27b3cbdb"
    }

    conn.request("GET", "/country/code?format=json&code=" + country, headers=headers)

    res = conn.getresponse()
    data = res.read().decode("utf-8")
    test = json.loads(data)
    result = 'The number of ' + type + ' in '+ country+' is: ' + str(test[0][type])
    return result


def weather2table(cityname):
    conn = http.client.HTTPSConnection("community-open-weather-map.p.rapidapi.com")

    headers = {
        'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
        'x-rapidapi-key': "acb7b42f91msh89c86e1c983ae20p16617fjsn5f8e27b3cbdb"
    }

    conn.request("GET", "/forecast?q=" + cityname, headers=headers)

    res = conn.getresponse()
    data = res.read().decode("utf-8")
    test = json.loads(data)


    #initialize the data set
    tem = []
    date = []
    if test["cod"] == '404':
        return False
        print('please check the name of city')
    else:
        for i in range(40):
            # print("Feeling templature:", end="")
            num = round(test["list"][i]['main']['feels_like'] - 273.15, 2)
            # print(num)
            # print("The date & time of the temperature: ", end="")
            time = test["list"][i]['dt_txt'].replace('00:00', '00').replace('2020-', '')
            # print(time)
            tem.append(num)
            date.append(time)
            # print()

        fig = plt.figure(figsize=(15, 6))
        plt.plot(date,tem,color = "black", linestyle=':')
        plt.plot(date[:8], tem[:8],label='Day one')
        plt.plot(date[8:16], tem[8:16],label='Day Two')
        plt.plot(date[16:24], tem[16:24],label='Day Three')
        plt.plot(date[24:32], tem[24:32],label='Day Four')
        plt.plot(date[32:40], tem[32:40],label='Day Five')
        plt.legend()
        plt.title('The Forecast of Temperature in 5 Days in ' + cityname.capitalize())
        plt.xlabel('Date & Time')
        plt.ylabel('Temperature ℃ ')
        fig.autofmt_xdate(rotation=45)
        plt.savefig("/Users/coulson/Desktop/Travel_bot/weather.png")
        return True


def airport_finder(cityname):
    conn = http.client.HTTPSConnection("tripadvisor1.p.rapidapi.com")

    headers = {
        'x-rapidapi-host': "tripadvisor1.p.rapidapi.com",
        'x-rapidapi-key': "acb7b42f91msh89c86e1c983ae20p16617fjsn5f8e27b3cbdb"
        }

    conn.request("GET", "/airports/search?query=" + cityname, headers=headers)

    res = conn.getresponse()
    data = res.read().decode("utf-8")
    test = json.loads(data)
    if len(test) == 0:
        return "Sorry, I do not find this city. Please check the spelling"
    tem = 'I have found ' + str(len(test)) + ' airport in this city and those are: \n'
    strr = ""
    for i in test:
        strr +=((i['name'] + " with code: "))
        strr += (i['code'] + "\n")
    return(tem + strr)


def airport_info(airport_code):
    import http.client

    conn = http.client.HTTPSConnection("airport-info.p.rapidapi.com")

    headers = {
        'x-rapidapi-host': "airport-info.p.rapidapi.com",
        'x-rapidapi-key': "acb7b42f91msh89c86e1c983ae20p16617fjsn5f8e27b3cbdb"
    }

    conn.request("GET", "/airport?iata=" + airport_code, headers=headers)

    res = conn.getresponse()
    data = res.read().decode("utf-8")
    test = json.loads(data)
    if len(test) == 1:
        return "Sorry, but I don't find the airport based on the code you entered"
    result = test['name'] + " in " + "No." + test['street_number'] + " "+ test['street'] + " street with the phone# " + test['phone']
    return (result)


def flight_price(departure_code, detination_code, date_MM_DD):
    conn = http.client.HTTPSConnection("compare-flight-prices.p.rapidapi.com")

    headers = {
        'x-rapidapi-host': "compare-flight-prices.p.rapidapi.com",
        'x-rapidapi-key': "acb7b42f91msh89c86e1c983ae20p16617fjsn5f8e27b3cbdb"
        }

    conn.request("GET", "/GetPricesAPI/StartFlightSearch.aspx?date2=2022-01-02&lapinfant=0&child=0&city2="+detination_code+"&date1=2020-"+date_MM_DD+"&youth=0&flightType=1&adults=1&cabin=1&infant=0&city1="+departure_code+"&seniors=0&islive=true", headers=headers)

    res = conn.getresponse()
    data = res.read()
    test = json.loads(data)
    time.sleep(1)
    conn.request("GET", "/GetPricesAPI/GetPrices.aspx?SearchID=" + test['SearchID'], headers=headers)
    res = conn.getresponse()
    data = res.read()
    test = json.loads(data)
    if len(test) == 0:
        return "Sorry, I have found any ticket based on the info you offer."
    result = ("I found the great tickets in Expedia for you to choose:\n")
    result += (test[0]['url'])
    return result
#print(flight_price("ORD", "LAX","08-01"))


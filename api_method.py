import http.client
import json
import matplotlib.pyplot as plt



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




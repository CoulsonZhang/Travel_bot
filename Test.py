import http.client
import json


conn = http.client.HTTPSConnection("community-open-weather-map.p.rapidapi.com")

headers = {
    'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
    'x-rapidapi-key': "acb7b42f91msh89c86e1c983ae20p16617fjsn5f8e27b3cbdb"
    }

conn.request("GET", "/forecast?q=shanghai", headers=headers)

res = conn.getresponse()
data = res.read().decode("utf-8")
test = json.loads(data)

print(data)
print(test)

tem = []
date = []

for i in range(40):
    print("Feeling templature:",end="" )
    num = round(test["list"][i]['main']['feels_like'] - 273.15, 2)
    print(num)
    print("The date & time of the temperature: ",end="" )
    time = test["list"][i]['dt_txt'].replace('00:00', '00').replace('2020-','')
    print(time)
    tem.append(num)
    date.append(time)
    print()

print(tem)
print(date)

import matplotlib.pyplot as plt
fig = plt.figure(figsize=(15,6))
plt.plot(date[:8], tem[:8], color = 'black')
plt.plot(date[8:16], tem[8:16], color = 'black')
plt.plot(date[16:24], tem[16:24], color = 'black')
plt.plot(date[24:32], tem[24:32], color = 'black')
plt.plot(date[32:40], tem[32:40], color = 'black')


plt.title('The Forecast of Temperature in 5 Days')
plt.xlabel('Date & Time')
plt.ylabel('Temperature ℃ ')
fig.autofmt_xdate(rotation = 45)
plt.show()

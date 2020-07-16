import http.client

conn = http.client.HTTPSConnection("compare-flight-prices.p.rapidapi.com")

headers = {
    'x-rapidapi-host': "compare-flight-prices.p.rapidapi.com",
    'x-rapidapi-key': "acb7b42f91msh89c86e1c983ae20p16617fjsn5f8e27b3cbdb"
    }

conn.request("GET", "/GetPricesAPI/StartFlightSearch.aspx?date2=2021-01-02&lapinfant=0&child=0&city2=NYC&date1=2020-08-01&youth=0&flightType=1&adults=1&cabin=1&infant=0&city1=ORD&seniors=0&islive=true", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
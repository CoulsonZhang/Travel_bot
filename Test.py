import http.client

conn = http.client.HTTPSConnection("tripadvisor1.p.rapidapi.com")

headers = {
    'x-rapidapi-host': "tripadvisor1.p.rapidapi.com",
    'x-rapidapi-key': "acb7b42f91msh89c86e1c983ae20p16617fjsn5f8e27b3cbdb"
    }

conn.request("GET", "/hotels/list?offset=0&currency=USD&limit=30&order=asc&lang=en_US&sort=recommended&location_id=293919&adults=1&checkin=2020-09-15&rooms=1&nights=2", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))

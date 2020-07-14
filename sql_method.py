import sqlite3

conn = sqlite3.connect('Winetable.db')
c = conn.cursor()

# Execute the query
# c.execute('SELECT * FROM Winetable WHERE ID=12388')
#
# # Print the results
#
# for i in c.fetchall():
#     print(i)
#     print(i[1])

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

params = {'Categories' : 'Ordinary Drink', 'Glass' : 'Wine Glass'}
for i in find_wine(params):
    print(i)

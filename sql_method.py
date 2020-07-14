import sqlite3

# Open connection to DB
conn = sqlite3.connect('Winetable.db')

# Create a cursor
c = conn.cursor()

# Define area and price
ID = '12388'
t = (ID)

# Execute the query
c.execute('SELECT * FROM Winetable WHERE ID=12388')

# Print the results

for i in c.fetchall():
    print(i)
    print(i[2])
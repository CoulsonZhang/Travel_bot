# Import sqlite3
import sqlite3


conn = sqlite3.connect('Winetable.db')
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS Winetable(ID int, Name text, Categories text, Alcoholic text, Glass text, Ingredient text)")
c.execute("INSERT INTO Winetable(ID, Name, Categories, Alcoholic, Glass, Ingredient) VALUES (11338,'English Highball','Ordinary Drink','Alcoholic','Highball glass','Brandy, Gin, Sweet Vermouth, Carbonated water, Lemon peel')")
c.execute('commit')
c.execute('SELECT * FROM Winetable')
print(c.fetchall())
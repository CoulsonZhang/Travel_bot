# Import sqlite3
import sqlite3


con = sqlite3.connect('Winetable.db')
w = con.cursor()
w.execute("CREATE TABLE IF NOT EXISTS Winetable(ID int, Name text, Categories text, Alcoholic text, Glass text, Ingredient text)")
w.execute("INSERT INTO Winetable(ID, Name, Categories, Alcoholic, Glass, Ingredient) VALUES (11338,'English Highball','Ordinary Drink','Alcoholic','Highball glass','Brandy, Gin, Sweet Vermouth, Carbonated water, Lemon peel')")
w.execute('commit')
w.execute('SELECT * FROM Winetable')
print(w.fetchall())
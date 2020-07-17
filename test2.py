one = {'Categories': 'Shot', 'Alcoholic': 'Non alcoholic'}
two = {'Categories': 'Ordinary Drink'}
print(one.values())
print(two.values())
fin = tuple(one.values())
f2 = tuple(two.values())
ddd = fin + f2
print(fin)
print(f2)
print(ddd)
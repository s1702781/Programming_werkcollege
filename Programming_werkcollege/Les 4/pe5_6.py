def wijzig(letterlijst):
    del letterlijst[:]
    letterlijst.extend(('d','e','f'))
letters = ['a','b','c']
print(letters)
wijzig(letters)
print(letters)
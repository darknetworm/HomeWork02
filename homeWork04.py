i = 1

userStr = input('Веведите строку: ')

listOfWords = userStr.split(sep=' ')
for word in listOfWords:
    print(f'{i}. {word[0:10]}')
    i += 1

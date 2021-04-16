dateTypes = [34, 23.6, 'Hello', b'World!', [1, 2, 3], {'name': 'John', 'age': 10}, (1, 2, 3), {'a', 'b', 'c'}, True,
             None, type(123)]
classTypes = {'int': 'целым числом',
              'float': 'числом с плавающей точкой',
              'str': 'строковым типом',
              'bytes': 'байтовым типом',
              'list': 'списком',
              'dict': 'словарём',
              'tuple': 'кортежем',
              'set': 'множеством',
              'bool': 'логическим типом',
              'NoneType': 'пустым типом',
              'type': 'типом переменной'}

for dateType in dateTypes:
    for classType in classTypes:
        if (str(type(dateType))[8:-2]) == classType:
            print('{} является {} ({})'.format(dateType, classTypes.get(str(type(dateType))[8:-2]), type(dateType)))

firstList = []
j = 0

while True:
    listAdd = input('Введите значение (для окончания ввведите "пробел + Enter"): ')
    if listAdd == ' ':
        break
    firstList.append(listAdd)
print(f'Первоначальный список: {firstList}')

for i in range(len(firstList) // 2):
    firstList[j], firstList[j + 1] = firstList[j + 1], firstList[j]
    j += 2
print(f'Видоизменённый список: {firstList}')

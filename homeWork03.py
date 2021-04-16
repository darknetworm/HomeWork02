monthList = ['Зимой', 'Весной', 'Летом', 'Осенью', 'Зимой']
monthDict = {0: 'Зимой', 1: 'Весной', 2: 'Летом', 3: 'Осенью', 4: 'Зимой'}

monthInput = int(input('Введите месяц от 1 до 12: '))
if monthInput > 12:
    print('В григорианском календаре 12 месяцев!')
    quit()
print(f'Решение с использованием списка:  {monthInput}-й месяц {monthList[monthInput // 3]}')
print(f'Решение с использованием словаря: {monthInput}-й месяц {monthDict.get(monthInput // 3)}')

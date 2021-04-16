name = []
price = []
pcs = []
unit = []
listOfProduct = []
i = 1

while True:
    try:
        userName = str(input('Введите название товара (для выхода нажмите "пробел + Enter"): '))
        if userName == ' ':
            break
        userItem = (i, {'название': userName, 'цена': int(input('Введите цену товара: ')),
                        'количество': int(input('Введите количество товаров: ')),
                        'ед': str(input('Ведите единицу измерения товара: '))})
        i += 1
    except ValueError:
        print('Неверное значение!')
    listOfProduct.append(userItem)

print('-------------------------------------------------------')
print('Проверим списки товаров')
for item in listOfProduct:
    print(item)

print('-------------------------------------------------------')
print('собираем аналитику о товарах')
for product in listOfProduct:
    name.append((product[1]).get('название'))
    price.append((product[1]).get('цена'))
    pcs.append((product[1]).get('количество'))
    unit.append((product[1]).get('ед'))

productAnalise = {'название': name, 'цена': price, 'количество': pcs, 'ед': unit}
print(productAnalise)

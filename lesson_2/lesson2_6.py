goods = []
features = {'название': '', 'цена': '', 'количество': '', 'единица': ''}
analytics = {'название': [], 'цена': [], 'количество': [], 'единица': []}
number = 0
while True:
    control = input('Для выхода из программы нажмите "Q" или Enter для продолжения').upper()
    if control == 'Q':
        break

    number += 1
    features = features.copy()

    for i in features.keys():
        item = input(f'Введите параметры товара "{i}": ')
        features[i] = int(item) if i == 'цена' or i == 'количество' else item
        analytics [i].append (features[i])
    goods.append ((number, features))
    print(f"\nСтруктура товаров\n {goods}")
    print(f"\nАналитика товаров: \n {'-'* 30}")

    for key, value in analytics.items():
        print(f"{key:>30}: {value}")
    print("-" * 30)


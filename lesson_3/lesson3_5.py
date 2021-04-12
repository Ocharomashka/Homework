def my_sum():
    sum_res = 0
    while True:
        print(f'Текущая сумма = {sum_res}')
        number = input('Введите строку чисел разделенных пробелами или нажмите Q для выхода: ')
        for el in number:
            if el == 'q' or el == 'Q':
                print(f'Сумма введенных значений = {sum_res}')
                break
            try:
                sum_res += float(el)
            except ValueError:
                print(f'Значение {el} имеет неверный тип')
        else:
            continue
        break
    return f'Сумма введенных значений = {sum_res}'

my_sum()
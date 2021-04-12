def my_f(s_1,s_2):
    try:
        s_1 = int(s_1)
        s_2 = int(s_2)
        div = s_1 / s_2
    except ValueError:
        return "Ошибка"
    except ZeroDivisionError:
        return "На ноль делить нельзя!"
    return(div)

print(my_f(int(input('Введите число 1: ')), int(input('Введите число 2: '))))




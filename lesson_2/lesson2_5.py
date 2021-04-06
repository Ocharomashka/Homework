my_list = [7,6,5,5,4,2]
print(my_list)
number = int(input("Введите число: "))
for el in range(len(my_list)):
    if my_list[el] == number:
        my_list.insert(el, number)
    elif my_list[0] < number:
        my_list.insert(0, number)
    elif my_list[-1] > number:
        my_list.append(number)
    elif my_list[el] > number and my_list[el + 1] < number:
        my_list.insert(el + 1, number)
print("текущий список", my_list)


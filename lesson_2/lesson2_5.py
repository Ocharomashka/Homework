my_list = [7, 6, 5, 5, 4, 2]
print(my_list)
number = int(input("Введите число: "))
i = 0
for el in my_list:
    if number <= el:
        i += 1
my_list.insert(i, number)
print("текущий список", my_list)


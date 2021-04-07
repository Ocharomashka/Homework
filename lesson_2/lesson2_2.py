my_list = int(input("Введите количество элементов списка "))

i = 0
new_list = []

while i < my_list:
    new_list.append(input("Введите следующее значение списка "))
    i += 1
print(new_list)
number = 0

for x in range(1, len(new_list), 2):
        new_list[number], new_list[number + 1] = new_list [number + 1], new_list[number]
        number += 2
print(new_list)

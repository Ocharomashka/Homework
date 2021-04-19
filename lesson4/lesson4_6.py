from itertools import count,cycle

print("Итератор, генерирующий целые числа, начиная с указанного")
n = int(input("Введите целое число до 500:"))

for i in count(n):
    if i == 501:
        break
    print(i, end=' ')

my_list = ["не", "за", "цик", "ли","вай", "ся"]

for i in cycle(my_list):
    print(i, end=' ') #бесконечный цикл



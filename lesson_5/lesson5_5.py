from random import randint

with open('text.txt','w', encoding='utf-8') as file:
    list = [randint(150, 200) for _ in range(10)]
    file.write(' '.join(map(str, list)))
print(list)
print(f'Сумма элементов: {sum(list)}')
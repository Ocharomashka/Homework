my_file = open("my_poem.txt", 'r')
content = my_file.readlines()
print(f'Содержимое файла:\n{content}')
print(f'Количество строк в файле: {len(content)}')

for i, value in enumerate(content, 1):
    words = len(value.split())
    print(f'В строке {i} содержится {words} слов')

my_file.close()
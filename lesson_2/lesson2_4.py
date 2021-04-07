
word = list(input("Введите предложение из нескольких слов: ").split())

for ind, i in enumerate(word):
    if len(i) > 10:
        print(ind, i[:10])
    else:
        print(ind, i)






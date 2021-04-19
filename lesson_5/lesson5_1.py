#вариант с существующим текстом и возможностью дописать.
# Просто интересно было как сделать, получилось криво как-то)
poem = ["Мишка косолапый", "По лесу идет,", "Шишки собирает,", "Песенки поет."]
with open('my_poem.txt', "w") as file:
    for line in poem:
        file.write(line + '\n')

action = open("my_poem.txt", "r")
content = action.read()
print(content)
action.close()

with open('my_poem.txt', 'a') as file:
    while True:
        text = input("Допишите свой текст или не пишите: ")
        if not text:
            break
        print(text, file=file)
print()

action = open("my_poem.txt", "r")
content = action.read()
print(content)
action.close()




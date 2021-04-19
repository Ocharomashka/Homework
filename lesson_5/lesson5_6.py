schedule = {}
with open('text_6.txt', encoding='utf-8') as dict:
    for line in dict:
        name, stat = line.split(':')
        n_sum = sum(map(int, ''.join([i for i in stat if i == ' ' or '0' <= i <= '9']).split()))
        schedule[name] = n_sum

print(schedule)


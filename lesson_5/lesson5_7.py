from json import dump

with open('text_7.txt', 'r', encoding='utf-8') as file:
    with open('text_77.json', 'w', encoding='utf-8') as j_file:
        profit = {string.split()[0]:int(string.split()[2]) - int(string.split()[3]) for string in file}
        av_profit =[]
        for i in profit.values():
            if i > 0:
                av_profit.append(i)

            dump([profit,{'av_profit':sum(av_profit)/len(av_profit)}],
                j_file, ensure_ascii=False, indent = 4)


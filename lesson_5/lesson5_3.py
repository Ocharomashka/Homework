with open("text_3.txt", 'r',encoding='utf-8') as file:
    poor_emp = {line.split()[0]: float(line.split()[1]) for line in file}
    print(f"Оклад меньше 20 000 тыс. евро получают: {[i[0] for i in poor_emp.items() if i[1]<20000]}")
    print(f'Средняя зарплата = {round(sum(poor_emp.values()) / len(poor_emp), 3)}')

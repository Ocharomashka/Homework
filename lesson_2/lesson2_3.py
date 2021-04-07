month = int(input("Забыли какие бывают сезоны? Не беда, введите номер месяца: "))
month_dic = {1: "январь", 2: "февраль", 3: "март", 4: "апрель", 5: "май", 6: "июнь", 7: "июль", 8: "август", 9: "сентябрь", 10: "октябрь", 11: "ноябрь", 12: "декабрь"}
season_list = ['winter','spring','summer','autumn']
season = {1: 'зима', 2: "весна", 3: 'лето', 4: 'осень'}

if month == 1 or month == 2 or month == 12 and month in month_dic:
    print(f"{month_dic[month]}",'is a', season_list[0])
    print(f"{month_dic[month]}",'- это', season.get(1))

elif month >= 3 and month < 6:
    print(f"{month_dic[month]}",'is a', season_list[1])
    print(f"{month_dic[month]}",'- это', season.get(2))
elif month > 5 and month < 9:
    print(f"{month_dic[month]}",'is a', season_list[2])
    print(f"{month_dic[month]}",'- это', season.get(3))
else:
    print(f"{month_dic[month]}",'is a', season_list[3])
    print(f"{month_dic[month]}",'- это', season.get(4))



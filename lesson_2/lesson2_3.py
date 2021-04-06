month = int(input("Забыли какие бывают сезоны? Не беда, введите номер месяца: "))
season_list = ['winter','spring','summer','autumn']
season = {1: 'зима', 2: "весна", 3: 'лето', 4: 'осень'}

if month == 1 or month == 2 or month == 12:
    print('it is a', season_list[0])
    print('Это', season.get(1))

elif month >= 3 and month < 6:
    print('it is a', season_list[1])
    print('Это', season.get(2))
elif month > 5 and month < 9:
    print('it is a', season_list[2])
    print('Это', season.get(3))
else:
    print('it is a', season_list[3])
    print('Это', season.get(4))



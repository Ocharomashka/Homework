def person():
    #вводим данные
    name = str(input('Введите имя: '))
    surname =str(input('Введите фамилию: '))
    year = int(input('Введите год рождения: '))
    city = str(input('Введите город проживания: '))
    email = str(input('Введите email: '))
    phone = int(input('Введите телефон: '))
    print(f'Имя: {name} Фамилия: {surname} Год рождения: {year} Город проживания: {city} Эл_почта: {email} Телефон: {phone}')

person()



class Worker:
    def __init__(self, position, name, surname, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}

class Position(Worker):
    def get_full_name(self):
        return print('{} {} {}'.format(self.position, self.name, self.surname), 'зарабатывает ')

    def get_total_income(self):
        return self._income['wage']+self._income['bonus']

result = Position('director','fedor','ivanov', wage=100, bonus=500)
result.get_full_name()
print(result.get_total_income(), 'K EUR')


class Cell:
    def __init__(self, amount):
        self.amount = int(amount)

    def make_order(self, rows):
        return '\n'.join(['*' * rows for _ in range(self.amount // rows)]) + '\n' + '*' * (self.amount % rows)

    def __str__(self):
        return f'{self.amount}'

    def __add__(self, other):
        return f'Общее количество клеток {self.amount + other.amount}'

    def __sub__(self, other):
        sub = self.amount - other.amount
        if sub <= 0:
            print('Клеток больше нет')
        else:
            print(f'Количество клеток сократилось на {sub}')

    def __mul__(self, other):
        return print(f'Клетки размножились. Их теперь {self.amount*other.amount}')

    def __truediv__(self, other):
        div = self.amount // other.amount
        if div == 0:
            print('Клетки исчезли')
        else:
            print(f'Количество клеток сократилось. Их теперь: {div}')
        return Cell(div)

c1 = Cell(int(input('Введите исходное количество клеток: ')))
c2 = Cell(int(input('Введите количество клеток после эксперимента: ')))
print(c1 + c2)
print(c1 - c2)
print(c1 * c2)
print(c1/c2)
print(c2.make_order(7))
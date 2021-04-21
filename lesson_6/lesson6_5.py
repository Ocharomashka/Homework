class Stationery:
    def __init__(self, title='draw it'):
        self.title = title

    def draw(self):
        print(f'Начинаем рисовать!')

class Pen(Stationery):
    def draw(self):
        print(f'Начинаем рисовать {self.title} ручкой')

class Pencil(Stationery):
    def draw(self):
        print(f'Начинаем рисовать {self.title} карандашом')

class Marker(Stationery):
    def draw(self):
        print(f'Начинаем рисовать {self.title} маркером')

st = Stationery()
st.draw()

pen = Pen('красной')
pen.draw()

pencil = Pencil('жёлтым')
pencil.draw()

marker = Marker('синим')
marker.draw()
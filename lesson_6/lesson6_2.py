
class Road:
    def __init__(self, length, width, weight, height):
        self._length = length
        self._width = width
        self.weight = weight
        self.height = height

    def calc(self):
        result = (self._length * self._width * self.weight * self.height) / 1000
        return print(f"Масса асфальта:\n {self._length} м * {self._width} м * {self.weight} кг * {self.height} м = ", result, 'т')

a = int(input('Input length: '))
b = int(input('Input width: '))
road = Road(a, b, 25, 0.05)
road.calc()

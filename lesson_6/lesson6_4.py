import random

class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.name} - Go')

    def stop(self):
        print(f'{self.name} - Stop')

    def turn(self, direction):
        print(f'{self.name} go {"left" if direction == 0 else "right"}')

    def show_speed(self):
        print(f'Car speed {self.name} is {self.speed} км/ч')

class TownCar(Car):

    def show_speed(self):
        return f'Current speed {self.name}: {self.speed} км/ч'\
            if self.speed < 60 else f'Reduce speed! {self.name}: Speed car {self.speed}'

class SportCar(Car):
    """SportCar"""


class WorkCar(Car):
    """WorkCar"""

    def show_speed(self):
        return f'Current speed {self.name}: {self.speed} км/ч' \
            if self.speed < 40 else f'Reduce speed! {self.name}: Speed car {self.speed}'

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police)



tc = TownCar(random.randint(0, 150),'green','Kia')
tc.go()
print(tc.show_speed())
tc.turn(0)
tc.stop()

print()

sc = SportCar (random.randint(0, 400),'yellow','Lombargini')
sc.go()
print(sc.show_speed())
sc.turn(1)
sc.stop()

print()

wc = WorkCar(random.randint(0, 100), 'white','Isuzu')
wc.go()
print(wc.show_speed())
wc.turn(1)
wc.stop()

print()

pc = PoliceCar(f'{random.randint(0, 200)}', 'white/blue', 'Ford')
pc.go()
print(pc.show_speed())
pc.turn(0)
pc.stop()

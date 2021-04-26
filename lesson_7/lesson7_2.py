from abc import ABC, abstractmethod


class Clothes(ABC):

    def __init__(self):
        pass

    @property
    @abstractmethod

    def consumption(self):
        pass

    def __add__(self, other):
        return self.consumption + other.consumption


class Coat(Clothes):
    def __init__(self,size):
        super().__init__()
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if size < 38:
            print('Выкроек данного размера нет')
            self.__size = 38
        elif size > 54:
            print("Слишком большой размер. Максимум шьем на 54. ")
            self.__size = 54
        else:
            self.__size = size

    @property
    def consumption(self):
        return self.__size / 6.5+0.5

class Costume(Clothes):
        def __init__(self, height):
            super().__init__()
            self.height = height

        @property
        def height(self):
            return self.__height

        @height.setter
        def height(self, height):
            if height < 150:
                print('Выкроек данного размера нет')
                self.__height = 150
            elif height > 200:
                print("Требуется индивидуальный пошив. ")
                self.__height = 200
            else:
                self.__height = height

        @property
        def consumption(self):
            return self.__height/100 * 2 + 0.3

coat = Coat(int(input('Введите размер (EU): ')))
print(f'Вам потребуется {coat.consumption:.2f} м ткани чтобы пошить пальто {coat.size} размера')

costume = Costume(int(input('Введите рост, см: ')))
print(f'Вам потребуется {costume.consumption:.2f} м ткани чтобы пошить костюм на рост {costume.height}')



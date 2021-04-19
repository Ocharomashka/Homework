from math import factorial

def factor(n):
    for el in range(n):
        print(el, end='! = ')
        yield factorial(el)

print("Вычислим факториал, друзья!")
for el in factor(10):
    print(el)
def my_func(x,y):
    x = float(x)
    y = int(y)
    if y > 0:
        print("Введите целое отрицательное число")
    if x < 0:
        print("Введите действительное положительное число")
    else:
        result = x ** y
        return result

print(my_func(input("Введите действительное положительное число: "), input("Введите целое отрицательное число: ")))


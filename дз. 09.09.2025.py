# 1 задание
num_1 = int(input("Введите первое число: "))
num_2 = int(input("Введите второе число: "))
num_3 = int(input("Введите третье число: "))
num_4 = int(input("Выберите: 1 или 2, (сложение или умножение) "))

if num_4 == 1:
    result = num_1 + num_2 + num_3
    print("Результат сложения:", result)
elif num_4 == 2:
    result = num_1 * num_2 * num_3
    print("Результат умножения:", result)
else:
    print("Ошибка: нужно было ввести 1 или 2")
# 2 задание
num_1 = int(input("Введите первое число: "))
num_2 = int(input("Введите второе число: "))
num_3 = int(input("Введите третье число: "))
num_4 = int(input("Выберите: 1,2,3 ,(Максимум из 3 чисел, 2 минимум из 3 чисел, среднее арифмитическое.)"))
if num_4 == 1:
    maximum = max(num_1, num_2, num_3)
    print("Максимальное число:", maximum)
elif num_4 == 2:
    minimum = min(num_1, num_2, num_3)
    print("Минимальное число:", minimum)
elif num_4 == 3:
    average = (num_1 + num_2 + num_3) / 3
    print("Среденее арифмитическое число: ",  average)
else:
    print("Ошибка: нужно было ввести 1 или 2 или 3")
# 3 Задание
m = int(input("Введите количество метров: "))

num_4 = int(input("Выберите: 1,2,3 (перевод в мили, дюймы, ярды): "))
if num_4 == 1:
    miles = m / 1609.344
    print("Метры в мили:", miles)
elif num_4 == 2:
    inches = m * 39.370079
    print("Метры в дюймы:", inches)
elif num_4 == 3:
    yards = m * 1.093613
    print("Метры в ярды:", yards)
else:
    print("Ошибка: нужно было ввести 1, 2 или 3")
# Циклы
# for i in range(0, 10):
#     print("*", end=" ")
# print()
# 1 задание
# n = int(input("Enter number 1-100: "))
#
# if n < 1 or n > 100:
#     print("error: число должно быть в диапозон от 1 до 100")
# else:
#     if n % 3 == 0 and n % 5 == 0:
#         print("Fizz Buzz")
#     elif n % 3 == 0:
#         print("Fizz")
#     elif n % 5 ==0:
#         print("Buzz")
#     else:
#         print(n)
# # 2 Zadanie
# number = float(input("Введите число: "))
#
# print("Выберите степень для возведения:")
# print("0 - Нулевая степень")
# print("1 - Первая степень")
# print("2 - Вторая степень")
# print("3 - Третья степень")
# print("4 - Четвертая степень")
# print("5 - Пятая степень")
# print("6 - Шестая степень")
# print("7 - Седьмая степень")
#
# choicе = int(input("Ваш выбор (0-7): "))
#
# if choicе == 0:
#     result = number ** 0
#     print(f"{number} в степени 0 = {result}")
# elif choicе == 1:
#     result = number ** 1
#     print(f"{number} в степени 1 = {result}")
# elif choicе == 2:
#     result = number ** 2
#     print(f"{number} в степени 2 = {result}")
# elif choicе == 3:
#     result = number ** 3
#     print(f"{number} в степени 3 = {result}")
# elif choicе == 4:
#     result = number ** 4
#     print(f"{number} в степени 4 = {result}")
# elif choicе == 5:
#     result = number ** 5
#     print(f"{number} в степени 5 = {result}")
# elif choicе == 6:
#     result = number ** 6
#     print(f"{number} в степени 6 = {result}")
# elif choicе == 7:
#     result = number ** 7
#     print(f"{number} в степени 7 = {result}")
# else:
#     print("Ошибка: выберите степень от 0 до 7")
# o = int(input("Введите стоимость разговора: "))
#
# # 3 Zadanie
#
# c = float(input("Введите базовую стоимость разговора (рубли): "))
#
# print("\nВыберите оператор для исходящего звонка:")
# print("1. МТС")
# print("2. Билайн")
# print("3. МегаФон")
# print("4. Теле2")
# oc = int(input("Введите номер (1-4): "))
#
# print("\nВыберите оператор для получения звонка:")
# print("1. МТС")
# print("2. Билайн")
# print("3. МегаФон")
# print("4. Теле2")
# op = int(input("Введите номер (1-4): "))
#
#
# if oc == op:
#
#     ap = 0.9
# elif (oc == 1 and op == 2) or (oc == 2 and op == 1):
#
#     ap = 1.1
# elif (oc == 3 and op == 4) or (oc == 4 and op == 3):
#
#     ap = 0.8
# else:
#
#     ap = 1.0
#
# t = c * ap
#
# print(f"\nИтоговая стоимость разговора: {t:.2f} рублей")
# # 4 Zadanie
# def z(sasalele):
#     base_s = 200
#     if sasalele < 500:
#         procent = 0.03
#     elif 500 <= sasalele < 1000:
#         procent = 0.05
#
#     else:
#         procent = 0.08
#
#     bonus = sasalele * procent
#     t = base_s + bonus
#     return t
# print("Расчет зп менеджеров")
# print("=" * 30)
# manager = []
# for i in range(3):
#     sasalele = float(input(f"Введите уровень продаж для менеджера {i+1} ($): "))
# manager.append(sasalele)
# print("\nРезультаты расчета зп: ")
# print("-" * 40)
#
# for i, z in enumerate(manager, 1):
#     sasalele = z
#     print(f"Менеджер {i}: ")
#     print(f"  Продажи: ${sasalele.2f}")
#     print(f"  Зарплата: ${sasalele.2f}")
#     print(f"  (Базовая ставка: 200$ + bonus: ${sasalele-200:.2f}")
#     print()

#16.09.2025
# for i in range(5):
#     print(i)
# login = input("Enter login: ")
# password = input("Enter password: ")
#
# while login != "Dungen Master" and password != "Oral cumshot":
#     print("Incorrect logint or password")
#     login = input("Enter login: ")
#     password = input("Enter password: ")
# print("Welcom, Dungen Master")
# Задание на циклы по for i in range
# for c in range(0, 101, 2):
#     print(c)
# print("-" * 30)
# for c in range(100, 0 -2, -2):
#     print(c)
# print("-" * 30)
# for h in range(0, 1001, 60):
#     print(h)
# print("-" * 30)
# num_1 = int(input("Введите начало диапазона: "))
# num_2 = int(input("Введите конец диапазона: "))
# for k in range(num_1, num_2 +1, 2):
#     print(k)
# print("-" * 30)
# num_1 =int(input("Enter number: "))
# for l in range(1, 10 + 1):
#     print(f"{num_1} * {l} = {num_1*l}")
# print("-" * 30)
# #___Цикл While___
# # 1
# x = 0
# while x < 6:
#     print(x)
#     x += 1
# # 2
# i = 1
# sum = 0
# while i <=10:
#     sum +=i
#     i += 1
# print("-" * 30)
# print(f"Сумма чисел от 1 до 10: {sum}")
# print("-" * 30)
# x =int(input("enter number 1: "))
# y =int(input("Enter number 2: "))
# while x and y >= 0:
#     print(f"{x} + {y} = {x + y}")
#     x = int(input("enter number 1: "))
#     y = int(input("Enter number 2: "))
#     print("-" * 30)
# print("-" * 30)
# x =int(input("Возраст 1: "))
# y =int(input("Рост 2: "))
# while x >= 18 or y >= 185 and y >200:
#      print("Вы нам не подходите")
#      x = int(input("Возраст 1: "))
#      y = int(input("Рост 2: "))
# print("Вы нам подходите")







# num = 15  # приклад значення для num

# if num > 10:
#     print("num більше за 10")
# else:
#     print("num не більше за 10")
# # ----------------------------------

# x = int(input('Введіть число: '))

# if x % 2 == 0:
#     print("Число x є парним.")
# else:
#     print("Число x є непарним.")
# # ----------------------------------
# a = input('Введіть число')
# a = int(a)
# if a > 0:
#     print('Число додатне')
# elif a < 0:
#     print("Число від'ємне")
# else:
#     print('Це число - нуль')
# # ----------------------------------

# result = None
# if result:
#     print(result)
# else:
#     print("Result is None, do something")
# # -----------------------------------

# user_name = input("Enter your name: \n")

# if user_name:
#     print(f"Hello {user_name} \n")
# else:
#     print("Hi Anonym! \n")
# # -------------------------------------
# money = 0
# if money:
#     print(f"You have {money} on your bank account \n")
# else:
#     print("You have no money and no debts \n ")
# # -------------------------------------

# a = [1, 2, 3]
# b = a
# c = [1, 2, 3]

# print("This is a is b ->", a is b)  # True
# print("This is a is c -> :", a is c)  # False
# # -------------------------------------

# # Bool algebra

# name = input("Enter Your name: \n")
# age = int(input("How old are You: \n"))
# has_driver_licence = True

# if name and age >= 18 and has_driver_licence:
#     print(f"User {name} can rent a car")
# # -------------------------------------

# num = int(input("Введіть число: "))

# length = len(str(num))

# if length == 2 and num % 2 == 0:
#     print("Парне двозначне число")
# else:
#     print("Ні, це не парне двозначне число")
# # -------------------------------------

# x = int(input("X: "))
# y = int(input("Y: "))

# if x == 0:
#     print("X can`t be equal to zero")
#     x = int(input("X: "))

# result = y / x
# print(result)
# # -------------------------------------

# x = int(input("X: "))
# y = int(input("Y: "))

# if x >= 0:
#     if y >= 0:  # x > 0, y > 0
#         print("Перша чверть")
#     else:  # x > 0, y < 0
#         print("Четверта чверть")
# else:
#     if y >= 0:  # x < 0, y > 0
#         print("Друга чверть")
#     else:  # x < 0, y < 0
#         print("Третя чверть")
# # -------------------------------------
# # Тернарні оператори
# is_nice = True
# state = "nice" if is_nice else "not nice"
# print(state)
# # -------------------------------------
# # match

# fruit = "qqq"

# match fruit:
#     case "apple":
#         print("This is an apple.")
#     case "banana":
#         print("This is a banana.")
#     case "orange":
#         print("This is an orange.")
#     case _:
#         print("Unknown fruit.")

# # -------------------------------------

# point = (1, 0)

# match point:
#     case (0, 0):
#         print("Точка в центрі координат")
#     case (0, y):
#         print(f"Точка лежить на осі Y: y={y}")
#     case (x, 0):
#         print(f"Точка лежить на осі X: x={x}")
#     case (x, y):
#         print(f"Точка має координати:  x={x}, y={y}")
#     case _:
#         print("Це не точка")

# # -------------------------------------

# pets = ["dog", "fish", "cat"]

# match pets:
#     case ["dog", "cat", _]:
#         # Випадок, коли є і собака, і кіт
#         print("There's a dog and a cat.")
#     case ["dog", _, _]:
#         # Випадок, коли є тільки собака
#         print("There's a dog.")
#     case _:
#         # Випадок для інших комбінацій
#         print("No dogs.")
# # -------------------------------------
# # Цикл FOR
# name_of_thing = "banana"

# for char in name_of_thing:
#     print(char, end="")
# print()
# # -------------------------------------
# alphabet = "abcdefghijklmnopqrstuvwxyz"
# for char in alphabet:
#     print(char, end=" ")
# # -------------------------------------
# # Зчитування рядка від користувача
# user_input = input("Введіть рядок: ")

# # Ініціалізація змінних для підрахунку символів та пробілів
# total_chars = len(user_input)  # загальна кількість символів у рядку
# space_count = 0  # кількість пробілів

# # Підрахунок кількості пробілів
# for char in user_input:
#     if char == " ":
#         space_count += 1

# # Виведення результатів
# print(f"Загальна кількість символів у рядку: {total_chars}")
# print(f"Кількість пробілів у рядку: {space_count}")
# # -----------------------------------------------------

# # кількість букв та пробілів у реченні 2 варіант

# user_input = input("Enter the sentence: \n")

# letter_count = 0
# space_count = 0

# for mark in user_input:
#     if mark.isalpha():
#         letter_count += 1
#     if mark == " ":
#         space_count += 1


# print(f"Final count of letter are equal: {letter_count}")
# print(f"Final space_cout are equal: {space_count}")
# # -----------------------------------------------------

# # while

# k = 0

# while k < 10:
#     k += 1
#     print(k)
# # -----------------------------------------------------

# # continue
# a = 0

# while a < 6:
#     a += 1
#     if not a % 3:
#         continue
#     print(a)
# # -----------------------------------------------------

# for i in range(1, 10):
#     if i % 2 == 0:
#         print(f"This is pare number {i}")
#     else:
#         print(f"This is not pare number {i}")
# # -----------------------------------------------------

# # while True:
# #     number = input("Enter the number: ")
# #     number = int(number)

# #     while True:
# #         print(number)
# #         number += 1
# #         if number < 0:
# #             break
# # ------------------------------------------------------

# list_1 = ["first: ", "second: ", "third: "]
# list_2 = ["nishang", "Metasploit", "Antak"]

# for index, name in zip(list_1, list_2):
#     print(index, name)
# print()
# # ------------------------------------------------------
# list_3 = ["first: ", "second: ", "third: ", "fourth"]
# list_4 = ["nishang", "Metasploit", "Antak", "BurpSuite", "gobuster"]

# for index, name in zip(list_3, list_4):
#     print(index, name)
# # ------------------------------------------------------


# print(len(list_1))
# print(len(list_2))
# print(len(list_3))
# print(len(list_4))
# # ------------------------------------------------------

# # dict_1 = {
# #     1: ": one",
# #     2: ": two",
# #     int("a"): ": three",
# # } це викличе помилку на рівні шнтерпритатора - ValueError.
# # -------------------------------------------------------

# dict_1 = {
#     1: ": one",
#     2: ": two",
#     3: ": three",
# }

# for key in dict_1:
#     print(key)

# print()

# for i in dict_1.keys():  # для перебору по ключах у словнику
#     print(i)

# for val in dict_1.values():  # для перебору по значеннях у словнику
#     print(val)
# # ------------------------------------------------------

# for key, value in dict_1.items():  # для перебору словника по ключ:значення
#     print(key, value)
# # ------------------------------------------------------


# age = input("How old are you? \n")

# try:
#     age = int(age)
#     if age >= 18:
#         print("Please enter the doore!!!")
#     else:
#         print("Sorry, but you can enter :(")

# except ValueError:
#     print(f"{age} is not a nummber ")
# # ------------------------------------------------------

# def print_max(a, b):
#     if a > b:
#         print(f"a 'max' ")
#     elif a == b:
#         print(f"a 'equal' b")
#     else:
#         print(f"b 'max'")


# print_max(3, 4)
# print_max(6, 4)
# print_max(7, 7)
# # ------------------------------------------------------
# x = 10
# y = 10
# print_max(x, y)
# # ------------------------------------------------------


# def my_function(a, b):
#     res = a + b
#     return float(res)  # можна вказувати тип який треба повернути


# result = my_function(8, 2.4)
# print(f"This is result from function:{result}")
# # ------------------------------------------------------


# def my_second_funk(a: int, b: int) -> int:
#     sum = a + b
#     return sum


# result_2 = my_second_funk(3, 6)
# print(f"This is my_second_func: {result_2}")
# # ------------------------------------------------------


# def greetings(name: str) -> str:
#     res = f"Hello {name}"
#     return res


# greeting = greetings("Petro")
# print(greeting)
# # ------------------------------------------------------


# def bool_func(number: int) -> bool:
#     return number % 2 == 0


# res_3 = bool_func(7)
# print(f"This is boolian function: {res_3}")
# # ------------------------------------------------------

# # imutable and immutable object

# # immutable


# def modify_string(original: str) -> str:
#     original = "CHANGE"
#     return original


# str_original = "original"
# print(modify_string(str_original))
# print(str_original)
# # ------------------------------------------------------

# # mutable


# def modify_list(lst: list) -> None:
#     lst.append(4)


# my_list = [1, 2, 3]
# modify_list(my_list)
# print(f"This is modify my_list: {my_list}")

# # ------------------------------------------------------


# def not_modify_list(lst: list) -> None:
#     lst = lst.copy() # для того щоб не модифікувалися дані робиться копія
#     lst.append(4)


# not_modify_my_list = [1, 2, 3]
# # not_modify_list(not_modify_my_list)
# print(f"This is not_modify_my_list: {not_modify_my_list}")
# # ------------------------------------------------------

# # LEGB

# def func_outer():
#     x = 2

#     def func_inner():
#         nonlocal x
#         x = 5

#     func_inner()
#     return x

# result = func_outer()
# print(f"This is func_outer: {result}")
# # ------------------------------------------------------

# def func_keys(a, b=5, c=10):
#     print(f"'a equal a: {a}', 'b equal b: {b}', 'c equal c: {c}'")

# func_keys(3,7)
# func_keys(25, c=24)
# func_keys(c=50, a=100)
# func_keys(a=333,b=555, c=777)
# # ------------------------------------------------------
# # Змінна кількість параметрів

# def all_args(*args):
#     for arg in args:
#         print(arg)
#         print(type(arg))


# x = all_args(1, '1', True, 'Hello', False, "name")
# # ------------------------------------------------------


# def concat_func(*args):
#     res = " "
#     for arg in args:
#         res += arg
#     return res


# at_end_res = concat_func("Hello ", "my ", "Friends!")

# print(f"Result of function concat_func: \n{at_end_res}")
# # -----------------------------------------

# def concatenate(*strings) -> str:
#     result = ""
#     for arg in strings:
#         result += arg
#     return result

# print(concatenate("Hello", " ", "world", "!"))
# # -----------------------------------------
# def greet(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")


# greet(name="Petro", age=41, city="Dnipro")
# print(type(greet))
# # -----------------------------------------


# def full_function(*args, **kwargs):
#     print("Position arguments", args)
#     print("Kye position arguments", kwargs)


# full_function(1, False, 3, 4, True, name="John", age=21)
# # -----------------------------------------

# my_list = [1, 2, 3]
# a, b, c = my_list

# print("My list: ", a, b, c)


# my_list_1 = [4, 5, 6]
# d, _, f = my_list_1
# print("My list 1 : ", d, f)


# my_list_2 = [7, 8, 9]
# a, *rest = my_list_2
# print("*Rest: ", *rest)
# # ---------------------------------------


# def greeet(name, age, city):
#     print(f"Your name {name}, your age {age}, your city {city}")


# person_info = {"name": "Alice", "age": 41, "city": "Kyiv"}
# person_info_2 = {"name": "John", "age": 60, "city": "Dnipro"}
# greeet(**person_info)
# greeet(**person_info_2)
# # ---------------------------------------

# # Recursion

# def factorial_num(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial_num(n-1)


# result = factorial_num(10)
# print(result)

# print(1*2*3*4*5*6*7*8*9*10)
# # ---------------------------------------


# def fibonacci(n):
#     if n <= 1:
#         return n
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)


# print(fibonacci(20))
# # ---------------------------------------

# def factorial(n):
#     print("Виклик функції factorial з n = ", n)
#     if n == 1:
#         print("Базовий випадок, n = 1, повернення 1")
#         return 1
#     else:
#         result = n * factorial(n-1)
#         print("Повернення результату для n = ", n, ": ", result)
#         return result

# print(factorial(5))
# # ---------------------------------------

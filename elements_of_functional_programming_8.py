from functools import wraps
from typing import Callable, Dict
from typing import Callable


# def add(a: int, b: int) -> int:
#     return a + b


# def multiply(a: int, b: int) -> int:
#     return a * b


# def apply_operation(a: int, b: int, operation: Callable[[int, int], int]) -> int:
#     return operation(a, b)


# # Використання
# result_add = apply_operation(5, 3, add)
# result_multiply = apply_operation(5, 3, multiply)

# print(result_add, result_multiply)
# # --------------------------

# # функцію, яка генерує іншу функцію для підняття числа
# # до заданого степеня


# def power(exponent: int) -> Callable[[int], int]:
#     def inner(base: int) -> int:
#         return base ** exponent
#     return inner


# # Використання
# square = power(2)  # степінь до якої підосимо число
# cube = power(3)  # степінь до якої підосимо число
# res = power(3)  # степінь до якої підосимо число

# print(square(4))  # число яке будемо піднсити до степеня
# print(cube(4))  # 64
# print(res(5))  # 125

# # ----------------------------

# # це зберігання функцій у структурах даних


# # Визначення функцій

# def add(a: int, b: int) -> int:
#     return a + b


# def multiply(a: int, b: int) -> int:
#     return a * b


# def power(exponent: int) -> Callable[[int], int]:
#     def inner(base: int) -> int:
#         return base ** exponent
#     return inner


# # Використання power для створення функцій square та cube
# square = power(2)
# cube = power(3)

# # Словник операцій
# operations: Dict[str, Callable] = {
#     'add': add,
#     'multiply': multiply,
#     'square': square,
#     'cube': cube
# }

# # Використання операцій
# result_add = operations['add'](10, 20)  # 30
# result_square = operations['square'](5)  # 25

# print(result_add)
# print(result_square)
# # --------------------


# def outer_function(msg):
#     message = msg

#     def inner_function():
#         print(message)

#     return inner_function


# # Створення замикання
# my_func = outer_function("Hello, world!")
# my_func()
# # ------------------------

# # замикання, яке зберігає інформацію
# # про кількість разів виклику функції.


# def counter() -> Callable[[], int]:
#     count = 0

#     def increment() -> int:
#         # використовуємо nonlocal, щоб змінити змінну в замиканні
#         nonlocal count
#         count += 1
#         return count

#     return increment


# # Створення лічильника
# count_calls = counter()

# # Виклики лічильника
# print(count_calls())  # Виведе 1
# print(count_calls())  # Виведе 2
# print(count_calls())  # Виведе 3
# # ---------------

# # Перетворимо функцію apply_discount,
# # використовуючи каррінг. Це дозволить нам створити
# # "замовлені" функції для різних рівнів знижок,
# # кожна з яких буде приймати тільки ціну товару.


# def discount(discount_percentage: int) -> Callable[[float], float]:
#     def apply_discount(price: float) -> float:
#         return price * (1 - discount_percentage / 100)
#     return apply_discount


# # Каррінг в дії
# ten_percent_discount = discount(10)
# twenty_percent_discount = discount(20)

# # Застосування знижок
# discounted_price = ten_percent_discount(500)  # 450.0
# print(discounted_price)

# discounted_price = twenty_percent_discount(500)  # 400.0
# print(discounted_price)
# # --------------------

# # Створення словника та використання каррінгу


# def discount(discount_percentage: int) -> Callable[[float], float]:
#     def apply_discount(price: float) -> float:
#         return price * (1 - discount_percentage / 100)
#     return apply_discount


# # Створення словника з функціями знижок
# discount_functions: Dict[str, Callable] = {
#     "10%": discount(10),
#     "20%": discount(20),
#     "30%": discount(30)
# }

# # Використання функції зі словника
# price = 500
# discount_type = "20%"

# discounted_price = discount_functions[discount_type](price)
# print(f"Ціна зі знижкою {discount_type}: {discounted_price}")
# # -----------------------

# # DECORATORS


# def complicated(x: int, y: int) -> int:
#     return x + y


# def logger(func):
#     def inner(x: int, y: int) -> int:
#         print(f"Викликається функція: {func.__name__}: {x}, {y}")
#         result = func(x, y)
#         print(f"Функція {func.__name__} завершила виконання: {result}")
#         return result

#     return inner


# complicated_ = logger(complicated)
# print(complicated_(2, 3))
# # -------------------------

# # using symbol logger "@" in code


# def logger(func):
#     def inner(x: int, y: int) -> int:
#         print(f"Викликається функція: {func.__name__}: {x}, {y}")
#         result = func(x, y)
#         print(f"Функція {func.__name__} завершила виконання: {result}")
#         return result

#     return inner


# @logger
# def complicated(x: int, y: int) -> int:
#     return x + y


# print(complicated(2, 3))
# # -------------

# # Using module functools and functools.wraps(func)


# def logger(func):
#     @wraps(func)
#     def inner(x: int, y: int) -> int:
#         print(f"Викликається функція: {func.__name__}: {x}, {y}")
#         result = func(x, y)
#         print(f"Функція {func.__name__} завершила виконання: {result}")
#         return result

#     return inner


# @logger
# def complicated(x: int, y: int) -> int:
#     return x + y


# print(complicated(2, 3))
# print(complicated.__name__)
# -----------------------

# Comprehensions

# List Comprehensions
# [new_item for item in iterable if condition]

# sq = [x**2 for x in range(1, 6)]
# print(f"This is using list Comprehension: {sq}")
# # ---
# # список квадратів парних чисел від 1 до 9.

# even_squares = [x**2 for x in range(1, 10) if x % 2 == 0]
# print(f"Cписок квадратів парних чисел: {even_squares}")
# ---

# Set Comprehensions
# {new_item for item in iterable if condition}

# numbers = [1, 4, 1, 3, 2, 5, 2, 6]
# sq = {i ** 2 for i in numbers}
# print(f"Множини квадратів чисел зі списку: {sq}")
# # ---
# odd_squares = {x**2 for x in range(1, 10) if x % 2 != 0}
# print(f"Множина квадратів непарних чисел від 1 до 9: {odd_squares}")
# ---

# Dictionary Comprehensions
# {key: value for item in iterable if condition}

# словник, де ключ - число, а значення - його квадрат.

# sq = {x: x**2 for x in range(1, 10)}
# print(f"Cловник, ключ-число, а значення-його квадрат: {sq}")

# # ключами будуть числа, а значеннями — їх квадрати,
# # але тільки для чисел, що більші за 5

# sq_dict = {x: x**2 for x in range(1, 10) if x > 5}
# print(f"""ключами будуть числа, а значеннями — їх квадрати,
# але тільки для чисел, що більші за 5: {sq_dict}""")
# ---------------------------------------------------------
# Функціональне програмування в Python

# Lambda Функції

# Наприклад зворотне сортування списку для sorted():
# nums = [1, 2, 3, 4, 5]
# nums_sorted = sorted(nums, key=lambda x: -x)
# print(f"Зворотне сортування списку для sorted(): {nums_sorted}")
# # ----------------------

# # Функція map

# # генератор, який підносить числа із списку numbers до квадрату

# numbers = [2, 4, 6, 8, 10]

# for i in map(lambda i: i**2, numbers):
#     print(f"Using map function: {i}")
# # --------------------------------------

# # Якщо отримати список, а не генератор

# numbers_list = [1, 3, 5, 7, 9]

# res_map_list = list(map(lambda x: x**3, numbers_list))
# print(f"Result if want list after using map: {res_map_list}")
# # -------------------------

# # Можна застосувати map до декількох списків:

# sum_num_map = map(lambda x, y: x + y, numbers, numbers_list)
# print(f"This is sum of numbers & numbers_list: {list(sum_num_map)}")
# # ------------------------

# # We can use List Comprehension

# nums_list_compr = [2, 4, 6, 7, 8, 9]

# res_use_list_compr = [x * x for x in nums_list_compr]
# print(f"Use list comprehension: {res_use_list_compr}")
# # -------------------------
# # list comprehension for 2 lists

# num_comp_1 = [1, 3, 5, 7, 9]
# num_comp_2 = [2, 4, 6, 8, 11]

# sum_for_2_list_compr = [x + y for x, y in zip(num_comp_1, num_comp_2)]
# print(f"Using zip & List comprehension: {sum_for_2_list_compr}")
# # --------------------------------------------

# # Функція filter

# filter_result = filter(lambda x: x % 2 == 0, range(1, 11))
# print(f"Using filter function x%2==0: {list(filter_result)}")
# # --------------------


# def is_positive(num):
#     return num > 0


# num_filter = [2, 4, 6, 8, 11, -3, -4, 0]
# positive_num = filter(is_positive, num_filter)
# print(f"Without list(): {positive_num}")
# print(f"Using function, without lambda: {list(positive_num)}")
# # -------------------
# # Фільтрація букв

# some_str = 'Видавництво А-БА-БА-ГА-ЛА-МА-ГА'

# new_str = ''.join(list(filter(lambda x: x.islower(), some_str)))
# print(f"Filtered use islower(): {new_str}")

# # --- 2 варіант

# new_str_1 = ''.join(list(filter(lambda x: x.isupper(), some_str)))
# print(f"Filtered use isupper(): {new_str_1}")
# # ----------------------


# # Заміна filter() на list comprehension

# nums = [1, 2, 3, 4, 5, 6]
# even_nums = [x for x in nums if x % 2 == 0]
# print(f"Use list comprehension insted of filter(): {even_nums}")
# # ------------------------------

# # some_str = 'Видавництво А-БА-БА-ГА-ЛА-МА-ГА'

# new_str = ''.join([x for x in some_str if x.islower()])
# print(f"Use list comprehension for letter: {new_str}")
# ------------

# any() function

nums = [0, False, 5, 0]
result = any(nums)
print(f"If even 1 elem return True: {result}")
# ----------

nums = [1, 3, 5, 7, 9]
result = any(x % 2 == 0 for x in nums)
print(f"any(x % 2 == 0 for x in nums): {result}")
# ---------

# all( function)

num_all = [1, 2, 3, 4, 5, 6, 7, 8, 9]
res_all_func = all(num_all)
print(f"Check nums with all() function: {res_all_func}")
# ---

is_all_even = all(x % 2 == 0 for x in num_all) 
print(f"Check with condition: {is_all_even}")
# ----------------------------------

# Чи всі слова у списку мають велику початкову букву?

words = ["Hello", "World", "Python"]
is_all_title_case = all(word.istitle() for word in words)
print(f"Чи всі слова у списку мають велику початкову букву: {is_all_title_case}")


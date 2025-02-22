# Введення (отримання даних)
user_name = input("Введіть ваше ім'я: ")

# Перетворення (обробка даних)
greeting = f"Привіт, {user_name}!"

# Виведення (виведення даних)
print(greeting)
print(f"Hello, {user_name}!")
# --------------------------------

import math
int_number = 3
float_number = 4.5
complex_number = 3.2 + 7j
print(type(int_number))
print(type(float_number))
print(type(complex_number))
# --------------------------------
# зробити перші букви в реченні маленькими
message = "Hello World"
split_words = message.split()
lower_msg = [split_word[0].lower() + split_word[1:]
             for split_word in split_words]
lower_mes_res = " ".join(lower_msg)
print('This is message: ', message)
print('This is message: ', lower_mes_res)
# --------------------------------

first_word = "Hello Everybody, Hello Big "
second_word = "World!"
result_words = f"{first_word} {second_word}"
print('This is first and Second words: \n', result_words)
# --------------------------------

side_a = 5
side_b = 10

formula = math.sqrt(side_a**2 + side_b**2)  # обчислення гіпотенузи
# обчислення гіпотенузи, до 4 цифри
formula_round_4 = round(math.sqrt(side_a**2 + side_b**2), 4)
square = side_a * side_b / 2  # площа трикутника, відповідь типу float
square_without_trace = side_a * side_b // 2  # площа трикутника без остатку
print("обчислення гіпотенузи: \n", formula)
print("обчислення гіпотенузи, до 4 цифри: \n", formula_round_4)
print("площа трикутника, відповідь типу float: \n", square)
print("площа трикутника без остатку: \n", square_without_trace)
# ------------------------------------------

ratio = 10
result = 8 * (ratio + 5) - ratio ** 2
print('This is ratio example: \n', result)
# ------------------------------------------

print((-3)**2)
print("Not right result, becouse of prioritize \n", -3**2)
# ------------------------------------------

x1 = 10
y1 = 10
x2 = 25
y2 = 25

d = round(math.sqrt((x2-x1)**2 + (y2-y1)**2), 2)
print("Now talk about Euclid formula. And count 2 mark after comma: \n", d)
# --------------------------------------------

word = "Hello World, Peoples!!!"
print(f"This is word: \n {word}")
# --------------------------------------------
input_text = input("Enter yourname:")
print("Hello ", input_text, "!")
# --------------------------------------------
P = 4
b = 3
input_number = int(input("Enter the number: "))
result = ((P * input_number / (3 + b)))
print(f"This is result: \n {result}")
# --------------------------------------------

list_of_fruits = ["cucamber", "bananas", "apple", "melown",  "charry"]
list_of_fruits.sort(key=len)
print(list_of_fruits)
# --------------------------------------------

array_of_numbers = [2, 4, 5, 4, 0, 7, 6, 23, 4, 5, 66, 79, 123, 7]
array_of_numbers.sort()
print(array_of_numbers)
array_of_numbers.sort(reverse=True)
print(array_of_numbers)
array_of_numbers.sort()
array_of_numbers.pop(2)
print(array_of_numbers)
#------------------------------------------

array_of_numbers = [2, 4, 5, 4, 0, 7, 6, 23, 4, 5, 66, 79, 123, 7]
array_b = [0, 23, 45, 67, 89, 12, 34,]
array_of_numbers_sorted = sorted(array_of_numbers)
print(array_of_numbers_sorted)
array_of_numbers_sorted = sorted(array_of_numbers, reverse=True)
print(array_of_numbers_sorted)
print(len(array_of_numbers))
array_of_numbers.extend(array_b)
print("This is extend: \n", array_of_numbers)
# --------------------------------------------

# Dictionary

my_dict = {"name": "Alice", "age": 25, "city": "New York"}
print(my_dict["name"], my_dict["age"], my_dict["city"])
# --------------------------------------------

my_dict["city"] = "Canada"
my_dict["email"] = "canada@gmail.com"
# del my_dict["name"]
print(my_dict)
# --------------------------------------------

# Sets

empty_word = set("Hello")
print(empty_word)

exmp_num = {1, 2, 3, 4, 5, 1, 3, 5, 7}
print(exmp_num)
# --------------------------------------------

exmp_num = [1, 2, 3, 4, 5, 1, 3, 5, 7]
print("Exmp_num: \n", exmp_num)
uniq_num = set(exmp_num)
print("Uniq_num: \n", uniq_num)
uniq_num_to_new_list = list(uniq_num)
print("This is new list after fitered use set: \n", uniq_num_to_new_list)
# --------------------------------------------

exmp_same_1 = {1, 2, 3, 4, 5, 1, 13, 15, 7}
exmp_same_2 = {1, 2, 3, 4, 5, 6, 7, 8, 9}

print("Intersection: \n",  exmp_same_1.intersection(exmp_same_2))
print("Use & insted of intersection: \n",  exmp_same_1 & exmp_same_2)
# --------------------------------------------

print("Difference: \n",  exmp_same_2.difference(exmp_same_1))
print("Use - insted of difference: \n",  exmp_same_2 - exmp_same_1)
# --------------------------------------------

print("Symmetric_dsfference: \n",  exmp_same_1.symmetric_difference(exmp_same_2))
print("Use ^ insted of symmetric_difference: \n",  exmp_same_1 ^ exmp_same_2)
# --------------------------------------------

print("Union: \n",  exmp_same_1.union(exmp_same_2))
print("Use | insted of union: \n",  exmp_same_1 | exmp_same_2)
# --------------------------------------------

frozen_set_1 = frozenset([1, 2, 3, 4, 5, 6, 7])
frozen_set_2 = frozenset([5, 6, 7, 8, 9, 12, 22])

frozen_union = frozen_set_1.union(frozen_set_2)
print("FrozenSet_Union: \n", frozen_union)
frozen_intersection = frozen_set_1 & frozen_set_2
print("Frozen_Set_intersection: \n", frozen_intersection)
frozen_difference = frozen_set_1.difference(frozen_set_2)
print("Frozen_Set_difference: \n", frozen_difference)
frozen_symmeytric_difference = frozen_set_1 ^ frozen_set_2
print("Frozen_Set_symmetric_difference: \n", frozen_symmeytric_difference)
# --------------------------------------------

my_tuple = tuple([1,"Hello", 3.14])
print(my_tuple[1])
# --------------------------------------------

answer = "Hello World!"
print(answer[2])
# print(answer[0] = "q") # SyntaxError
# --------------------------------------------

# Просте форматування рядка
name = 'John'
print('Hello, {}!'.format(name))

# Форматування з декількома аргументами
age = 25
print('Hello, {}. You are {} years old.'.format(name, age))

# Використання іменованих аргументів
print('Hello, {name}. You are {age} years old.'.format(name='Jane', age=30))

# Використання індексів для вказівки порядку аргументів
print('Hello, {1}. You are {0} years old.'.format(age, name))

# -----------------------------------------------

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_numbers = numbers[0:10:2]
even_numbers = numbers[1:10:2]
three_numbers = numbers[2:10:3]
summ_1 = len(odd_numbers)
summ_2 = len(even_numbers)
summ_3 = len(three_numbers)
print(odd_numbers)
print(even_numbers)
print("This is three_numbers: \n", three_numbers)

print(summ_1)
print(summ_2)
print(summ_3)
# -----------------------------------------------

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
copy_numbers = numbers[:]
print("This is copy_numbers: \n", copy_numbers)
# -----------------------------------------------


num = 15  # приклад значення для num

if num > 10:
    print("num більше за 10")
else:
    print("num не більше за 10")
# ----------------------------------

x = int(input('Введіть число: '))

if x % 2 == 0:
    print("Число x є парним.")
else:
    print("Число x є непарним.")
# ----------------------------------
a = input('Введіть число')
a = int(a)
if a > 0:
    print('Число додатне')
elif a < 0:
    print("Число від'ємне")
else:
    print('Це число - нуль')
# ----------------------------------

result = None
if result:
    print(result)
else:
    print("Result is None, do something")
# -----------------------------------

user_name = input("Enter your name: \n")

if user_name:
    print(f"Hello {user_name} \n")
else:
    print("Hi Anonym! \n")
# -------------------------------------
money = 0
if money:
    print(f"You have {money} on your bank account \n")
else:
    print("You have no money and no debts \n ")
# -------------------------------------

a = [1, 2, 3]
b = a
c = [1, 2, 3]

print("This is a is b ->", a is b)  # True
print("This is a is c -> :", a is c)  # False
# -------------------------------------

# Bool algebra

name = input("Enter Your ndme: \n")
age = int(input("How old are Your: \n"))
has_driver_licence = True

if name and age >= 18 and has_driver_licence:
    print(f"User {name} can rent a car")
# -------------------------------------

num = int(input("Введіть число: "))

length = len(str(num))

if length == 2 and num % 2 == 0:
    print("Парне двозначне число")
else:
    print("Ні, це не парне двозначне число")
# -------------------------------------

x = int(input("X: "))
y = int(input("Y: "))

if x == 0:
    print("X can`t be equal to zero")
    x = int(input("X: "))

result = y / x
print(result)
# -------------------------------------

x = int(input("X: "))
y = int(input("Y: "))

if x >= 0:
    if y >= 0:  # x > 0, y > 0
        print("Перша чверть")
    else:  # x > 0, y < 0
        print("Четверта чверть")
else:
    if y >= 0:  # x < 0, y > 0
        print("Друга чверть")
    else:  # x < 0, y < 0
        print("Третя чверть")
# -------------------------------------
# Тернарні оператори
is_nice = True
state = "nice" if is_nice else "not nice"
print(state)
# -------------------------------------
# match

fruit = "qqq"

match fruit:
    case "apple":
        print("This is an apple.")
    case "banana":
        print("This is a banana.")
    case "orange":
        print("This is an orange.")
    case _:
        print("Unknown fruit.")

# -------------------------------------

point = (1, 0)

match point:
    case (0, 0):
        print("Точка в центрі координат")
    case (0, y):
        print(f"Точка лежить на осі Y: y={y}")
    case (x, 0):
        print(f"Точка лежить на осі X: x={x}")
    case (x, y):
        print(f"Точка має координати:  x={x}, y={y}")
    case _:
        print("Це не точка")

# -------------------------------------

pets = ["dog", "fish", "cat"]

match pets:
    case ["dog", "cat", _]:
        # Випадок, коли є і собака, і кіт
        print("There's a dog and a cat.")
    case ["dog", _, _]:
        # Випадок, коли є тільки собака
        print("There's a dog.")
    case _:
        # Випадок для інших комбінацій
        print("No dogs.")
# -------------------------------------
# Цикл FOR
name_of_thing = "banana"

for char in name_of_thing:
    print(char, end="")
print()
# -------------------------------------
alphabet = "abcdefghijklmnopqrstuvwxyz"
for char in alphabet:
    print(char, end=" ")
# -------------------------------------
# Зчитування рядка від користувача
user_input = input("Введіть рядок: ")

# Ініціалізація змінних для підрахунку символів та пробілів
total_chars = len(user_input)  # загальна кількість символів у рядку
space_count = 0  # кількість пробілів

# Підрахунок кількості пробілів
for char in user_input:
    if char == " ":
        space_count += 1

# Виведення результатів
print(f"Загальна кількість символів у рядку: {total_chars}")
print(f"Кількість пробілів у рядку: {space_count}")
# -----------------------------------------------------

# кількість букв та пробілів у реченні 2 варіант

user_input = input("Enter the sentence: \n")

letter_count = 0
space_count = 0

for mark in user_input:
    if mark.isalpha():
        letter_count += 1
    if mark == " ":
        space_count += 1


print(f"Final count of letter are equal: {letter_count}")
print(f"Final space_cout are equal: {space_count}")
# -----------------------------------------------------

# while

k = 0

while k < 10:
    k += 1
    print(k)
# -----------------------------------------------------

# continue
a = 0

while a < 6:
    a += 1
    if not a % 3:
        continue
    print(a)
# -----------------------------------------------------

for i in range(1, 10):
    if i % 2 == 0:
        print(f"This is pare number {i}")
    else:
        print(f"This is not pare number {i}")
# -----------------------------------------------------

while True:
    number = input("Enter the number: ")
    number = int(number)

    while True:
        print(number)
        number += 1
        if number < 0:
            break

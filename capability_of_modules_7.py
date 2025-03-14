import decimal
from decimal import Decimal, ROUND_DOWN
from decimal import Decimal
from collections import Counter
import collections
from collections import namedtuple, defaultdict

# Point = namedtuple('Point', ['x', 'y'])
# print(f"This is using function namedtuple: {Point}")

# p = Point(11, y=45)
# print(f"This is instance of Point: {p}")
# print(f"This is p.x: {p.x}")
# print(f"This is p.y: {p.y}")
# # ----------------

# Person = collections.namedtuple(
#     # створення іменованого кортежу
#     'Person', ['first_name', 'last_name', 'age', 'birth_place', 'post_index'])

# print(f"This is create Person: {Person}")

# person = Person('Mick', 'Nitch', 35, 'Boston', '01146')

# print(f"This is person.first_name: {person.first_name}")
# print(f"This is person.post_index: {person.post_index}")
# print(f"This is  person.age: {person.age}")
# print(f"This is person birth_place by index - person[3]: {person[3]}")
# -------------------------

# # tuple for Cat

# Cat = collections.namedtuple('Cat', ['nickname', 'age', 'owner'])

# cat = Cat('Simon', 4, 'Krabat')

# print(cat)
# print(
#     f"This is cat {cat.nickname}, he is {cat.age}-year-old. His owner is {cat.owner}.")
# # ------------------------

# # Counter

# student_marks = [4, 2, 4, 6, 7, 4, 2, 3, 4, 5, 6, 6, 7, 1, 1, 1, 3, 5]
# mark_counts = collections.Counter(student_marks)
# print(f"This is use Counter():\n {mark_counts}")
# # --------------

# # most_common()

# student_marks = [4, 2, 4, 6, 7, 4, 2, 3, 4, 5, 6, 6, 7, 1, 1, 1, 3, 5]
# mark_counts = collections.Counter(student_marks)

# print(mark_counts.most_common())
# print(mark_counts.most_common(1))
# print(mark_counts.most_common(2))
# print(mark_counts.most_common(3))
# # ---------------------

# # letter counts

# letter_count = collections.Counter("banana")

# print(f"This is use Counter for count letter in word banana: {letter_count}")
# # -------------------

# # підрахунок слів в тексті

# sentence = "the quick brown fox jumps over the lazy dog"
# words = sentence.split()
# word_count = Counter(words)

# # Виведення слова та його частоти
# for word, count in word_count.items():
#     print(f"{word}: {count}")
# ----------------------
# defaultdict using list

# d = defaultdict(list)

# d['a'].append(1)
# d['a'].append(2)
# d['b'].append(2)

# print(f"This is defaultdict with list, and use append(): {d}")
# # ----------------------

# # defaultdict using int

# d = defaultdict(int)

# # Збільшення значення для кожного ключа
# d['a'] += 1
# d['b'] += 1
# d['a'] += 1

# print(f"This is using int and +=1 : {d}")
# # ------------

# # список слів який розбити на декілька списків, залежно від першої літери слова.

# words = ['apple', 'zoo', 'lion', 'lama', 'bear', 'bet', 'wolf', 'appendix']
# grouped_words = {}

# for word in words:
#     char = word[0]
#     # чи створили ми для ключа char в словнику grouped_words
#     # пустий список:
#     if char not in grouped_words:
#         grouped_words[char] = []
#     grouped_words[char].append(word)

# print(f"If split list of words, depend of first letter: {grouped_words}")
# # ------------------

# words = ['apple', 'zoo', 'lion', 'lama', 'bear', 'bet', 'wolf', 'appendix']
# grouped_words = defaultdict(list)

# for word in words:
#     char = word[0]
#     grouped_words[char].append(word)

# print(f"This is check: \n {dict(grouped_words)}")
# -----------------

# # Stack

# # Створення стеку
# def create_stack():
#     return []


# # Перевірка на порожнечу
# def is_empty(stack):
#     return len(stack) == 0

# # Додавання елементу
# def push(stack, item):
#     stack.append(item)

# # Вилучення елементу
# def pop(stack):
#     if not is_empty(stack):
#         return stack.pop()
#     else:
#         print("Стек порожній")

# # Перегляд верхнього елемента
# def peek(stack):
#     if not is_empty(stack):
#         return stack[-1]
#     else:
#         print("Стек порожній")

# stack = create_stack()
# # push(stack, 'a')
# # push(stack, 'b')
# # push(stack, 'c')

# print(peek(stack))  # Виведе 'c'
# print(f" Is EMPTY: {is_empty(stack)}")  # Виведе 'c'

# print(pop(stack))  # Виведе 'c'

# ----------------------

# queue
#  deque з модуля collections в якості черги.

# from collections import deque

# # Створення черги
# queue = deque()

# # Enqueue: Додавання елементів
# queue.append('a')
# queue.append('b')
# queue.append('c')

# print("Черга після додавання елементів:", list(queue))

# # Dequeue: Видалення елемента
# print("Видалений елемент:", queue.popleft())

# print("Черга після видалення елемента:", list(queue))

# # Peek: Перегляд першого елемента
# print("Перший елемент у черзі:", queue[0])

# # IsEmpty: Перевірка на порожнечу
# print("Чи черга порожня:", len(queue) == 0)

# # Size: Розмір черги
# print("Розмір черги:", len(queue))
# # ----------------------------------

# # ДВОСТОРОННЯ ЧЕРГА
# print("\n")

# # Створення пустої двосторонньої черги
# d = deque()

# # Додаємо елементи в чергу
# d.append('middle')  # Додаємо 'middle' в кінець черги
# d.append('last')    # Додаємо 'last' в кінець черги
# d.appendleft('first')  # Додаємо 'first' на початок черги

# # Виведення поточного стану черги
# print("Черга після додавання елементів:", list(d))

# # Видалення та виведення останнього елемента (з правого кінця)
# print("Видалений останній елемент using pop():", d.pop())

# # Видалення та виведення першого елемента (з лівого кінця)
# print("Видалений перший елемент using popleft():", d.popleft())

# # Виведення поточного стану черги після видалення елементів
# print("Черга після видалення елементів:", list(d))
# # ----------

# # в deque є можливість обмежити розмір Deque:


# d = deque(maxlen=5)
# for i in range(10):
#     d.append(i)

# print(f"This is using maxlen=5: {d}")
# # --------------------------

# # як можна використовувати двосторонню чергу
# # для контролю пріоритету завдань.


# # Список завдань, де кожне завдання - це словник
# tasks = [
#     {"type": "fast", "name": "Помити посуд"},
#     {"type": "slow", "name": "Подивитись серіал"},
#     {"type": "fast", "name": "Вигуляти собаку"},
#     {"type": "slow", "name": "Почитати книгу"}
# ]

# # Ініціалізація черги завдань
# task_queue = deque()

# # Розподіл завдань у чергу відповідно до їх пріоритету
# for task in tasks:
#     if task["type"] == "fast":
#         task_queue.appendleft(task)  # Додавання на високий пріоритет
#         print(f"Додано швидке завдання: {task['name']}")
#     else:
#         task_queue.append(task)  # Додавання на низький пріоритет
#         print(f"Додано повільне завдання: {task['name']}")

# # Виконання завдань
# while task_queue:
#     task = task_queue.popleft()
#     print(f"Виконується завдання: {task['name']}")

# # Ініціалізація черги завдань
# task_queue = deque()
# # -----------------------

# Decimal

# print(Decimal("0.1") + Decimal("0.2") == Decimal("0.3"))
# print(Decimal("0.1") + Decimal("0.2"))
# # ---------------

# #  округлити число до двох знаків після коми


# # Вихідне число Decimal
# number = Decimal('3.14159')

# # Встановлення точності до двох знаків після коми
# rounded_number = number.quantize(Decimal('0.00'), rounding=ROUND_DOWN)

# print(f"Using quantize(Decimal('0.00)): {rounded_number}")
# # ---------------

# # Приклад різних констант


# number = Decimal("1.45")
# number1 = Decimal("300.675")

# # Округлення за замовчуванням до одного десяткового знаку
# print("Округлення за замовчуванням ROUND_HALF_EVEN:",
#       number.quantize(Decimal("0.0")))

# # Округлення вверх при нічиї (ROUND_HALF_UP)
# print("Округлення вгору ROUND_HALF_UP:", number.quantize(
#     Decimal("0.0"), rounding=decimal.ROUND_HALF_UP))

# # Округлення вниз (ROUND_FLOOR)
# print("Округлення вниз ROUND_FLOOR:", number.quantize(
#     Decimal("0.0"), rounding=decimal.ROUND_FLOOR))

# # Округлення вверх (ROUND_CEILING)
# print("Округлення вгору ROUND_CEILING:", number.quantize(
#     Decimal("0.0"), rounding=decimal.ROUND_CEILING))

# # Округлення до трьох десяткових знаків за замовчуванням
# print("Округлення до трьох десяткових знаків:",
#       Decimal("3.14159").quantize(Decimal("0.000")))
# ---
# print(Decimal("5.1235097564").quantize(Decimal('0.0000')))
# print(number1.quantize(Decimal("0.00"), rounding=decimal.ROUND_HALF_UP))

# ---------------------------

# Створення та робота з ГЕНЕРАТОРАМИ

# def my_generator():
#     yield 1
#     yield 2
#     yield 3


# gen = my_generator()

# # Використання next()
# print(next(gen))  # Виведе 1
# print(next(gen))  # Виведе 2
# print(next(gen))  # Виведе 3
# --------------

def count_down(start):
    while start > 0:
        yield start
        start -= 1

for number in count_down(5):
    print(number)
# ------------------------

# Ітерація по файлу

def read_lines(file_path):
    with open(file_path, 'r', encoding="utf-8") as file:
        for line in file:
            yield line.strip()

# Використання генератора для читання рядків з файлу
for line in read_lines("report7.txt"):
    print(f"Use generator for read lines in document:\n {line}")


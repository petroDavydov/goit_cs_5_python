from collections import UserString
from collections import UserList
from collections import UserDict


class Animal:
    def __init__(self, nickname: str, weight: int):
        self.nickname = nickname  # Виправлено
        self.weight = weight

    def say(self):
        pass


# Створення екземпляра
animal = Animal("Buddy", 10)
print(animal.nickname)  # Перевіримо, чи працює

# ------------------------------------------------------


class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def change_weight(self, new_weight: int):
        self.weight = new_weight


animal = Animal("Simon", 10)

animal.change_weight(12)

print(f"New weight of {animal.nickname}: {animal.weight}")

# ----------------------------------------------------
""""Додайте до класу color змінну класу зі white значенням і
change_color методом (який має змінити значення color змінної класу) Animal.
Створіть екземпляри об’єкта: first_animal і second_animal.
Викличте change_color("red")функцію для будь-якого екземпляра
об’єкта Animalта змініть значення color змінної класу на "red"."""


class Animal:
    color = "white"

    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def change_weight(self, weight):
        self.weight = weight

    @classmethod
    def change_color(my_color, new_color):
        my_color.color = new_color


first_animal = Animal("Buddy", 10)
second_animal = Animal("Milo", 15)

first_animal.change_color("red")

print(f"Class color: {Animal.color}")
print(f"First animal color: {first_animal.color}")
print(f"Second animal color: {second_animal.color}")
# ------------------------------------------
"""Створіть Cat клас, батьківським класом якого є Animal.
У Cat класі перевизначте say метод, щоб він повертав рядок
"Meow"для екземплярів Cat класу.
У цьому випадку ми виконуємо поліморфізм.
Поліморфізм - це здатність програми вибирати різні реалізації
при виклику операцій з однаковими іменами.
Коли ви викликаєте say метод в екземплярі класу Cat ,
викликається нова реалізація. Він не успадковується від Animal класу.
Також створіть змінну cat, яка буде екземпляром класу Cat.
Під час створення cat змінної ім’я кота має бути "Simon",
а вага – 10 одиницями."""


class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def change_weight(self, weight):
        self.weight = weight


class Cat(Animal):
    def say(self):
        return f"Meow"


cat = Cat("Simon", 10)
print(cat.nickname)
print(cat.weight)
print(cat.say())
# ----------------------------------

"""Створіть Dog клас, батьківським класом якого є Animal  один.
У Dog класі перевизначте say метод, щоб він повертав рядок "Woof" 
для екземплярів класу Dog.
У конструкторі класу Dog введіть нову breed властивість.
Усі властивості, успадковані від Animal класу, мають залишитися.
Створіть наступний екземпляр класу Dog в коді.
dog = Dog("Barbos", 23, "labrador")"""


class Animal:
    def __init__(self, nickname: str, weight: str):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def change_weight(self, weight):
        self.weight = weight


class Dog(Animal):
    def __init__(self, nickname: str, weight: str, breed: str):
        super().__init__(nickname, weight)
        self.breed = breed

    def say(self):
        return f"Woof"


dog = Dog("Barbos", 23, "labrador")

print(dog.nickname)
print(dog.weight)
print(dog.breed)
print(dog.say())
# --------------------------------------------------------
"""Для попереднього завдання додамо Owner клас - власника собаки.
Клас має три атрибути: name, age і address.
Вам також потрібно реалізувати info метод,
який повертає словник з ключами 'name', 'age' і 'address',
і значення якого дорівнюють відповідним властивостям екземпляра класу.
Ви повинні реалізувати owner атрибут для Dog класу,
який буде екземпляром класу Owner.
Додайте до Dog класу who_is_owner метод,
який повертає результат виклику info методу екземпляра класу Owner.
Це буде словник з такими ключами: name, age, і address власника."""


class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def change_weight(self, weight):
        self.weight = weight


class Owner:
    def __init__(self, name: str, age: int, address: str):
        self.name = name
        self.age = age
        self.address = address

    def info(self) -> dict:
        return {
            "name": self.name,
            "age": self.age,
            "address": self.address

        }


class Dog(Animal):
    def __init__(self, nickname, weight, breed, owner: Owner):
        super().__init__(nickname, weight)
        self.breed = breed
        self.owner = owner

    def say(self):
        return "Woof"

    def who_is_owner(self):
        return self.owner.info()


dog_owner = Owner("Artur", 45, "England, Oslo 123, Main str.")  # Owner

dog = Dog("Snezhok", 12, "pikines", dog_owner)


print(dog.nickname)
print(dog.weight)
print(dog.breed)
print(dog.say())
print(dog.who_is_owner())
# ---------------------------------------

"""Створіть два класи: CatDog і DogCat.
Ці класи повинні бути успадковані відразу від двох класів: Catі Dog.
Після успадкування від екземпляра класу CatDog батьківський say метод
має повернути Meow, а DogCat клас має повернути "Woof".
Для обох цих класів реалізуйте info метод, який повертає рядок у такому форматі
f"{self.nickname}-{self.weight}"."""


class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass


class Cat(Animal):
    def say(self):
        return "Meow"


class Dog(Animal):
    def say(self):
        return "Woof"


class CatDog(Cat, Dog):
    def info(self):
        return f"{self.nickname}-{self.weight}"


class DogCat(Dog, Cat):
    def info(self):
        return f"{self.nickname}-{self.weight}"


cat_dog = CatDog("VeniaminDog", 5)
dog_cat = DogCat("PickinesCat", 8)

print(cat_dog.say())
print(dog_cat.say())
print(cat_dog.info())
print(dog_cat.info())
# -----------------------------------------------------

"""Створіть LookUpKeyDict клас, батьківським класом якого є UserDict клас.
Встановити lookup_key функцію як метод класу LookUpKeyDict."""


class LookUpKeyDict(UserDict):
    def lookup_key(self, value):
        keys = []
        for key, val in self.data.items():
            if val == value:
                keys.append(key)
        return keys


lookup_dict = LookUpKeyDict({"a": 1, "b": 2, "c": 1})
print(lookup_dict.lookup_key(1))
print(lookup_dict.lookup_key(2))
print(lookup_dict.lookup_key(3))

# ------------------------------------------------

"""Створіть AmountPaymentList клас, який успадковує UserList клас.
Встановити amount_payment функцію як метод класу AmountPaymentList."""


class AmountPaymentList(UserList):
    def amount_payment(self):
        sum = 0
        for value in self.data:
            if value > 0:
                sum = sum + value
        return sum


pay_lst = AmountPaymentList([1, -3, 4])
pay_lst1 = AmountPaymentList([-1, -3, -4])
pay_lst2 = AmountPaymentList([10, -3, -4])
print(f"Payment list: {pay_lst.amount_payment()}")
print(f"Payment list: {pay_lst1.amount_payment()}")
print(f"Payment list: {pay_lst2.amount_payment()}")
# ---------------------------------------------------------

"""Створіть NumberString клас, успадкуйте його від UserString класу
та визначте number_count(self) для нього метод.
Цей метод підрахує кількість цифр у рядку."""


class NumberString(UserString):
    def number_count(self):
        digits = [char for char in self.data if char.isdigit()]
        return len(digits)


num_string = NumberString("abc123def456")

print(f"Count numbers in raw: {num_string.number_count()}")

# ---
# import re
# from collections import UserString

# class NumberString(UserString):
#     def number_count(self):
#         return len(re.findall(r'\d', self.data))

# ---
# ----------------------------

"""Створіть IDException клас, який успадкує Exception клас.
Також реалізуйте add_id(id_list, employee_id) функцію,
яка додає ідентифікатор користувача employee_id до id_list
та повертає вказаний оновлений id_list.
Функція add_id викличе власну функцію, IDException
якщо employee_id не починається з 01,
інакше employee_id буде додано до id_list."""


class IDException(Exception):
    pass


def add_id(id_list, employee_id):
    if not employee_id.startswith("01"):
        raise IDException(
            f"Invalid ID: {employee_id} does not start with '01'")

    if employee_id not in id_list:
        id_list.append(employee_id)
        return id_list


id_list = ["01A", "01B"]

add_id(id_list, "01C")  # Додасть "01C" до списку
print(id_list)  # Виведе: ['01A', '01B', '01C']

# --------------------------------------------------

"""Як ми вже згадували, поліморфізм - це здатність програми вибирати
різні реалізації під час виклику операцій з однаковими іменами.
Однак поліморфізм - це також здатність об'єктів прикидатися чимось іншим.
У наведеному вище прикладі Chupakabra прикинувся собакою та котом.
Вам потрібно реалізувати CatDog клас, не використовуючи успадкування
від Animal класу, але так, щоб екземпляр класу CatDog поводився так само,
як екземпляр класу Cat. Це означає, що він повинен прикидатися Cat класом."""

# class Animal:
#     def __init__(self, nickname, weight):
#         self.nickname = nickname
#         self.weight = weight

#     def say(self):
#         pass

#     def change_weight(self, weight):
#         self.weight = weight


# class Cat(Animal):
#     def say(self):
#         return "Meow"


# class CatDog:
#     def __init__(self, nickname, weight):
#         self.cat = Cat(nickname, weight)  # Внутрішній екземпляр класу Cat

#     def say(self):
#         return self.cat.say()

#     def change_weight(self, weight):
#         self.cat.weight = weight

#     @property
#     def nickname(self):
#         return self.cat.nickname

#     @nickname.setter
#     def nickname(self, value):
#         self.cat.nickname = value

#     @property
#     def weight(self):
#         return self.cat.weight

#     @weight.setter
#     def weight(self, value):
#         self.cat.weight = value


# # Створюємо об'єкт CatDog з псевдонімом "Babay"
# cat_dog = CatDog("Babay", 4)

# # Перевіряємо поведінку
# print(cat_dog.say())         # Виведе: Meow
# print(cat_dog.nickname)      # Виведе: Babay
# print(cat_dog.weight)        # Виведе: 4

# # Змінюємо вагу
# cat_dog.change_weight(5)
# print(cat_dog.weight)        # Виведе: 5


# # Змінюємо вагу
# cat_dog.change_weight(5)
# print(cat_dog.weight)        # Виведе: 5

# -----------------------------------
# 2 variant

class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def change_weight(self, weight):
        self.weight = weight


class Cat(Animal):
    def say(self):
        return "Meow"


class CatDog:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    # Метод, який робить CatDog схожим на Cat
    def say(self):
        return "Meow"

    # Метод для зміни ваги
    def change_weight(self, weight):
        self.weight = weight


# Створюємо екземпляр CatDog
cat_dog = CatDog("Babay", 4)

# Поведінка, схожа на Cat
print(cat_dog.say())         # Виведе: Meow
print(cat_dog.nickname)      # Виведе: Babay
print(cat_dog.weight)        # Виведе: 4

# Зміна ваги
cat_dog.change_weight(5)
print(cat_dog.weight)        # Виведе: 5
# -----------------------------------------------------

# Завдання: Контактна книга, частина перша

"""Реалізуйте клас Contacts, який працюватиме з контактами.
На першому етапі ми додамо два методи.
list_contacts повертає список контактів це змінна contacts з поточного
екземпляра класу add_contacts додає новий контакт до списку, який є змінною
об'єкту - contacts.
Клас Contacts містить змінну класу current_id.
Ми будемо використовувати її при додаванні нового контакту як унікального
ідентифікатора контакту. Коли ми додаємо новий контакт, то передаємо такі
аргументи в метод add_contacts: name, phone, email та favorite.
Метод повинен створити словник із зазначеними ключами та значеннями параметрів
функції.
Також необхідно додати до словника новий ключ id, значенням якого є значення
змінної класу current_id.
Приклад отриманого словника:

{
    "id": 1,
    "name": "Wylie Pope",
    "phone": "(692) 802-2949",
    "email": "est@utquamvel.net",
    "favorite": True,
}

Вказаний словник ми додаємо до списку contacts.
Не забуваймо збільшувати змінну current_id на одиницю після кожного виклику
методу add_contacts для збереження унікальності ключа id для словника.
Примітка: для правильного проходження тесту не створюйте екземпляр класу в коді."""


class Contacts:
    current_id = 1

    def __init__(self):
        self.contacts = []

    def list_contacts(self):
        """Повертає список контактів."""
        return self.contacts

    def add_contacts(self, name, phone, email, favorite):
        new_contact = {
            "id": Contacts.current_id,
            "name": name,
            "phone": phone,
            "email": email,
            "favorite": favorite
        }
        self.contacts.append(new_contact)
        Contacts.current_id += 1
# ----------------------------------------------

# Завдання: Контактна книга, частина друга


"""Продовжуємо розширювати функціональність класу Contacts.
На цьому етапі ми додамо до класу метод get_contact_by_id.
Метод повинен шукати контакт по унікальному id у списку contacts
та повертати словник з нього із зазначеним ключем id.
Якщо словника із зазначеним id у списку contacts не знайдено,
метод повертає None.
Примітка: для правильного проходження тесту не створюйте екземпляр класу в коді."""


class Contacts:
    current_id = 1

    def __init__(self):
        self.contacts = []

    def list_contacts(self):
        return self.contacts

    def add_contacts(self, name, phone, email, favorite):
        self.contacts.append(
            {
                "id": Contacts.current_id,
                "name": name,
                "phone": phone,
                "email": email,
                "favorite": favorite,
            }
        )
        Contacts.current_id += 1

    def get_contact_by_id(self, id):
        for contact in self.contacts:
            if contact["id"] == id:
                return contact
        return None
# ---------------------------------------------

# Завдання: Контактна книга, завершення


"""Завершуємо функціональність класу Contacts.
На цьому етапі ми додамо до класу метод remove_contacts.
Метод винен видаляти контакт по унікальному id у списку contacts.
Якщо словника із зазначеним id у списку contacts не знайдено,
метод жодних дій над списком contacts не робить.

Примітка: для правильного проходження тесту не створюйте екземпляр класу в коді."""


class Contacts:
    current_id = 1

    def __init__(self):
        self.contacts = []

    def list_contacts(self):
        return self.contacts

    def add_contacts(self, name, phone, email, favorite):
        self.contacts.append(
            {
                "id": Contacts.current_id,
                "name": name,
                "phone": phone,
                "email": email,
                "favorite": favorite,
            }
        )
        Contacts.current_id += 1

    def get_contact_by_id(self, id):
        result = list(
            filter(lambda contact: contact.get("id") == id, self.contacts))
        return result[0] if len(result) > 0 else None

    def remove_contacts(self, id):
        result = list(
            filter(lambda contact: contact["id"] != id, self.contacts))
        self.contacts = result

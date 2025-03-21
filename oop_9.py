from typing import Protocol


class User:
    name = "Anonymous"
    age = 15
    weight = 15


user1 = User()
print(
    f"This is user1 - name: {user1.name}, age: {user1.age}, weight: {user1.weight}")


user2 = User()
user2.name = "John"
user2.age = 90
user2.weight = 30

print(
    f"This is user2 - name: {user2.name}, age: {user2.age}, weight: {user2.weight}")
# ------------------

# Атрибут класу


class MyClass:
    class_attribute = "I am a class attribute"
# ---

# Поле класу


class MyClass:
    def __init__(self, value):
        self.instance_field = value  # Поле класу


obj1 = MyClass(5)
obj2 = MyClass(10)

print(obj1)
print(obj2)
# ---
# self завжди має бути першим аргументом


class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def say_name(self) -> None:
        print(f'Hi! I am {self.name} and I am {self.age} years old.')

    def set_age(self, age: int) -> None:
        self.age = age


print()
bob = Person('Boris', 45)

bob.say_name()
bob.set_age(25)
bob.say_name()
# ------------------


class Person:
    count = 0

    def __init__(self, name: str):
        self.name = name
        Person.count += 1

    def how_many_persons(self):
        print(f"Кількість людей зараз {Person.count}")


print()
first = Person('Boris')
first.how_many_persons()
second = Person('Alex')
first.how_many_persons()
# -----------
# OOP as a example use Pokemon


class Pokemon:
    def __init__(self, name, type, health):
        self.name = name
        self.type = type
        self.health = health

    def attack(self, other_pokemon):
        print(f"{self.name} attacks {other_pokemon.name}!")

    def dodge(self):
        print(f"{self.name} dodged the attack!")

    def evolve(self, new_form):
        print(f"{self.name} is evolving into {new_form}!")
        self.name = new_form


# Створення об'єкта Pikachu
pikachu = Pokemon("Pikachu", "Electric", 100)

popkorn = Pokemon("Popkorn", "Waterproof", 100)

# Використання методів
print()
pikachu.attack(Pokemon("Charmander", "Fire", 100))
pikachu.dodge()
pikachu.evolve("Raichu")
print()
popkorn.attack(Pokemon("Pikachu", "Water", 100))
popkorn.dodge()
popkorn.evolve("BIGPOPCORN")
# # ----------------------

# Інкапсуляція


class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def greeting(self) -> str:
        return f"Hi {self.name}"


p = Person("Boris", 34)
# ------------------

# Protected

# Якщо ми хочемо взаємодіяти з захищеними полями об'єкту ззовні,
# необхідно впровадити правильний підхід до інкапсуляції у класі
# Person та слід використовувати методи для взаємодії з такими
# атрибутами об'єкту


class Person:
    def __init__(self, name: str, age: int, is_active: bool):
        self.name = name
        self.age = age
        self._is_active = is_active

    def greeting(self):
        return f"Hi {self.name}"

    def is_active(self):
        return self._is_active

    def set_active(self, active: bool):
        self._is_active = active


p = Person("Boris", 34, True)
print(p.name, p.age, p.is_active())
print(p.greeting())
print()
p1 = Person("Can", 15, False)
print(p1.name, p1.age, p1.is_active())
print(p1.greeting())
# ------------------------------------

# Private


class Person:
    def __init__(self, name: str, age: int, is_active: bool, is_admin: bool):
        self.name = name
        self.age = age
        self._is_active = is_active
        self.__is_admin = is_admin

    def greeting(self):
        return f"Hi {self.name}"

    def is_active(self):
        return self._is_active

    def set_active(self, active: bool):
        self._is_active = active

    def get_is_admin(self):
        return self.__is_admin

    def set_is_admin(self, is_admin: bool):
        # Тут можна додати будь-яку логіку перевірки або обробки
        self.__is_admin = is_admin


p = Person("Boris", 34, True, False)
# print(p._Person__is_admin)
# print(p.__is_admin) # не доступна в такий спосіб
print(p.get_is_admin())
p.set_is_admin(True)
print(p.get_is_admin())

# ---------------------------------------

# НАСЛІДУВАННЯ

# Основний класс


class Animal:
    def __init__(self, nickname: str, age: int):
        self.nickname = nickname
        self.age = age

    def make_sound(self):
        pass


class Cat(Animal):
    def make_sound(self) -> str:
        return "Meow"


class Dog(Animal):
    # розширення класу
    def __init__(self, nickname: str, age: int, breed: str):
        super().__init__(nickname, age)  # виклик Animal
        self.breed = breed  # втановлення породи собаки

    def make_sound(self) -> str:
        return "Woof"

    def chase_tail(self) -> str:
        # додавання особливостей до об'єкту собак
        return f"{self.nickname} is chasing its tail!"


class Cow(Animal):
    def make_sound(self):
        return "Moo"


my_cat = Cat("Simon", 4)
my_cow = Cow("Bessie", 3)

print(my_cat.nickname, my_cat.age)
print(my_cow.nickname, my_cow.age)

print(f"my_cat.make_sound: {my_cat.make_sound()}")  # Виведе "Meow"
print(f"my_cow.make_sound: {my_cow.make_sound()}")  # Виведе "Moo"

my_dog = Dog("Rex", 5, "Golden Boy Retriver")
print(my_dog.nickname, my_dog.age, my_dog.breed)
print(f"my_dog.make_sound: {my_dog.make_sound()}")  # Виведе "Woof"
print(my_dog.chase_tail())  # Виведе "Rex is chasing its tail!"
# ----------------------------------

# Багаторівневе наслідування та Method Resolution Order (MRO)


class Animal:
    def __init__(self, nickname: str, age: int):
        self.nickname = nickname
        self.age = age

    def make_sound(self):
        pass


class Bird(Animal):
    def make_sound(self):
        return "Chirp"


class Parrot(Bird):
    def can_fly(self):
        return True


class TalkingParrot(Parrot):
    def say_phrase(self, phrase):
        return f"The parrot says: '{phrase}'"


my_parrot = TalkingParrot("Alice", 2)
print(my_parrot.make_sound())
print(my_parrot.can_fly())
print(my_parrot.say_phrase("Hello, World!"))
print(f"This is __mro__ for TalkingParrot: {TalkingParrot.__mro__}")
# ------------------

# Ви можете переглянути MRO для будь-якого класу
# використовуючи метод mro() або атрибут __mro__ :


class A:
    pass


class B(A):
    pass


class C(A):
    pass


class D(B, C):
    pass


# Виведе порядок розв'язання методів для класу D
print(f"This is mro for D: {D.mro()}")
# ---------------------------------

# ПОЛІМОРФІЗМ


class Animal:
    def __init__(self, nickname: str, age: int):
        self.nickname = nickname
        self.age = age

    def make_sound(self):
        pass


class Cat(Animal):
    def make_sound(self):
        return "Meow"


class Dog(Animal):
    def make_sound(self):
        return "Woof"


def animal_sounds(animals):
    for animal in animals:
        print(animal.make_sound())


animals = [Cat("Simon", 4), Dog("Rex", 5)]
animal_sounds(animals)
# ----------------------------

# Механізм Python дозволяє використовувати будь-які об'єкти один замість іншого,
# аби в обох були потрібні методи та поля. Інтерпретатор не перевіряє,
# що у функцію або метод був переданий об'єкт потрібного або дочірнього класу,
# достатньо щоб в об'єкта були потрібні методи і все буде працювати.


class Duck:
    def quack(self):
        print("Quack, quack!")


class Person:
    def quack(self):
        print("I'm Quacking Like a Duck!")


def make_it_quack(duck):
    duck.quack()


duck = Duck()
person = Person()

make_it_quack(duck)
make_it_quack(person)

# ---------------------------------

# У Python можна використовувати статичну типізацію для анотації типів
# і одночасно покладатися на качину типізацію для поліморфізму
# та гнучкої поведінки об'єктів.


class Dog:
    def speak(self) -> str:
        return "Woof"


class Cat:
    def speak(self) -> str:
        return "Meow"


class Robot:
    def speak(self) -> str:
        return "Beep boop"


def make_it_speak(speaker) -> None:
    print(speaker.speak())


dog = Dog()
cat = Cat()
robot = Robot()

make_it_speak(dog)  # Виведе: Woof
make_it_speak(cat)  # Виведе: Meow
make_it_speak(robot)  # Виведе: Beep boop
# --------------------------------

# Створимо інтерфейс, використовуючи typing.Protocol,
# для об'єктів, які можуть "говорити".
# Ми хочемо, щоб будь-який об'єкт, який має метод speak,
# вважався сумісним з цим інтерфейсом.

# from typing import Protocol


class Speaker(Protocol):
    def speak(self) -> str:
        pass


class Dog:
    def speak(self) -> str:
        return "Woof"


class Cat:
    def speak(self) -> str:
        return "Meow"


class Robot:
    def speak(self) -> str:
        return "Beep boop"


def make_it_speak(speaker: Speaker) -> None:
    print(speaker.speak())


dog = Dog()
cat = Cat()
robot = Robot()

make_it_speak(dog)  # Виведе: Woof
make_it_speak(cat)  # Виведе: Meow
make_it_speak(robot)  # Виведе: Beep boop
# -----------------------------------

# Упакування у byte-рядки та розпакування із byte-рядків
import pickle


# Об'єкт для серіалізації
my_data = {"key": "value", "num": 42}
print(f"This is my_data:\n {my_data}")
# Серіалізація об'єкта в байтовий рядок
serialized_data = pickle.dumps(my_data)
# Виведе байтовий рядок
print(f"This is serialized_data:\n {serialized_data}")
# ------------

# Десеріалізація об'єкта з байтового рядка
deserialized_data = pickle.loads(serialized_data)
# Виведе вихідний об'єкт Python
print(f"This is deserialized_data:\n {deserialized_data}")

# print(dir(pickle))
# ----------------------------------------------------


# Об'єкт для серіалізації
my_data = {"key": "value", "num": 100}

# Серіалізація об'єкта в файл
with open("data.pickle", "wb") as file:
    serialization_data_file = pickle.dump(my_data, file)

print(f"This is serialization_data_file:\n {serialization_data_file}")


# Десеріалізація об'єкта з файлу
with open('data.pickle', 'rb') as file:
    deserialized_data_file = pickle.load(file)

# Виведе вихідний об'єкт Python
print(
    f" This is deserialized_data_file from file data.pickle:\n {deserialized_data_file}")
# ------------------------------


class Human:  # об'явлення класу
    def __init__(self, name):
        self.name = name


bob = Human("Bob")
with open("instance.pickle", "wb") as file:  # серіалізація
    pickle.dump(bob, file)  # dump()


with open("instance.pickle", "rb") as file:  # десереалізація
    loaded_instance = pickle.load(file)  # load()

print(f"This is work with Human class-object: {loaded_instance.name}")
# ---------------------------------------

# серіалізування налаштування в файл і десеріалізування
# їх при наступному запуску програми для користувача.

# Збереження налаштувань
settings = {'theme': 'dark', 'language': 'ukrainian'}
with open('settings.pickle', 'wb') as f:
    pickle.dump(settings, f)

# Завантаження налаштувань
with open('settings.pickle', 'rb') as f:
    loaded_settings = pickle.load(f)

print(f"Deserialization data from file: {loaded_settings}")
# -------------------------------------------------




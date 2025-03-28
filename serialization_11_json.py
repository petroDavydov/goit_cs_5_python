# Серіалізація об'єктів Python за допомогою JSON

# {
#   "name": "Gupalo Vasyl",
#   "age": 30,
#   "isStudent": true
# }
# ------------------------------------

import json

some_data = {
    "key": "value",
    2: [1, 2, 3],
    "my_tuple": (5, 6),
    "my_dict": {"key": "value"},
}

json_string = json.dumps(some_data)
print(f"This is json_string serialization with dumps():\n {json_string}")
unpacked_some_data = json.loads(json_string)
print(f"This is deserialization unpacked_some_data with loads():\
\n {unpacked_some_data}")
# -----------------------------------------------

# Серіалізація об'єкта Python у рядок формату JSON виконується за допомогою
# методу json.dump(), якщо потрібно записати JSON безпосередньо у файл.


# Python об'єкт (словник)
data = {"name": "Gupalo Vasyl", "age": 30, "isStudent": True}

# Серіалізація у файл
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f)  # serialization


# Десеріалізація з файлу
with open("data.json", "r", encoding="utf-8") as f:
    data_from_file = json.load(f)  # deserialization
    print(f"This is deserialization data_from_file:\n {data_from_file}")
# ---------------------------------------------

# Використання Кирилиці

# Python об'єкт (словник)
data = {"name": "Гупало Василь", "age": 30, "isStudent": True}

# Серіалізація у файл
with open("data.json_kyrylyca", "w", encoding="utf-8") as f:
    # json.dump(data, f)
    json.dump(data, f, ensure_ascii=False, indent=4)

# При вказанні ensure_ascii=False, indent=4 все відображається коректно
# -------------------------------------------------

expenses = {"hotel": 150, "breakfast": 30, "taxi": 15, "lunch": 20}

file_name = "expenses.txt"
with open(file_name, "w") as fh:
    for key, value in expenses.items():
        fh.write(f"{key}|{value}\n")

# ------------------------------------
# experement myself add
expenses_1 = {"hotel": 150, "breakfast": 30, "taxi": 15, "lunch": 20}
house = {"roof": 1, "doore": 8, "windows": 120, "bar": 2}
car_ford = {"whill": 4, "motor": 1, "seat": 6, "handelbar": 1}

file_name_add = "added_one_by_one.txt"
with open(file_name_add, "a+") as fhd:  # запис в документ слідуючим рядком
    for key, value in expenses_1.items():
        fhd.write(f"{key} | {value}\n")

    for key, value in house.items():
        fhd.write(f"{key} | {value}\n")

    for key, value in car_ford.items():
        fhd.write(f"{key} | {value}\n")


# ------------------------------------------

# Якщо потім знадобиться завантажити цей перелік назад у Python,
# завжди є змога це зробити, використовуючи "r":

file_name = "expenses.txt"
expenses = {}

with open(file_name, "r") as fh:
    raw_expenses = fh.readlines()
    for line in raw_expenses:
        key, value = line.split("|")
        expenses[key] = int(value)

print(f"This is raw_expenses: {expenses}")
# ///-----------//
# from experiment code return deserilization:

file_name_add = "added_one_by_one.txt"
edded_file = {}

with open(file_name_add, "r") as fhd_return:
    row_item = fhd_return.readlines()
    for line in row_item:
        key, value = line.split("|")
        edded_file[key] = int(value)

print(f"Deserealization object: \n {edded_file}")
# ------------------------------------------


